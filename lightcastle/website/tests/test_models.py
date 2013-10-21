import re
import os
from django.utils import unittest
from website.models import blog
from website.management.commands.update_database import Command
from django.conf import settings
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetAuthors


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
        self.all_posts = wp.call(GetPosts({'number': 100, 'post_status': 'publish'}))
        self.authors = wp.call(GetAuthors())
        self.all_posts = self.all_posts[::-1] #reverse the list of posts so that the most recent are last in the list
        for post in self.all_posts: 
            for author in self.authors:
                if author.id == post.user:
                    post.author = author.display_name
#          following line sets the image variable so the posts index can display right
            if blog._get_first_image(post.content) != "None":
                post.image = blog._get_first_image(post.content)
            else:
              post.image = ""

            b = blog.Blog( title = post.title, author = post.author, initial_image = post.image, date = post.date, content = post.content)
            b.save()



#        self.b = Blog()
#        os.system("pwd")#python manage.py update_database")#c = Command()
#        c.handle()



    def test_orm_queries(self):
        """test the orm language to get objects"""
        self.assertEqual(blog.Blog.objects.get(id=1).title, "Python -- It's Classy!")
        self.assertEqual(blog.Blog.objects.get(id=10).title, "Continuous Deployment a la Agile Richmond")
        self.assertEqual(blog.Blog.objects.get(id=15).title, "Graph ALL THE THINGS with matplotlib")

    def test_format_for_posts_index(self):
        """first blog title in index should be Python -- It's Classy! when using the format for posts index method"""
        posts = blog.format_for_posts_index(blog.Blog.objects.all())
        self.assertEqual(posts[0].title, "Python -- It's Classy!")



    def test_get_first_image(self):
        """_get_first_image method should return the first <img> tag of the first blog entry, in this case, a python image"""
        post = blog.Blog.objects.get(id=1)
        self.assertEqual(blog._get_first_image(post.content), '<img alt="Python Logo" class="size-medium wp-image-37 alignright" height="79" src="http://lightcastletech.files.wordpress.com/2012/08/486px-python_logo-svg.png?w=300" title="486px-Python_logo.svg" width="269"/>')


    def test_remove_html_tags(self):
        """"content should be without any html tags in it"""
        html = re.compile('<\w*>')
        self.assertEqual(html.findall(blog._remove_html_tags(blog.Blog.objects.get(id=15).content)), [])
        self.assertEqual(html.findall(blog._remove_html_tags(blog.Blog.objects.get(id=22).content)), [])
        self.assertEqual(html.findall(blog._remove_html_tags(blog.Blog.objects.latest('id').content)), [])


    def test_remove_wordpress_markup(self):
        """"content should be without any wordpress tags in it"""
        wordpress = re.compile('\[sourcecode\]')
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(blog.Blog.objects.get(id=15).content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(blog.Blog.objects.get(id=22).content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(blog.Blog.objects.latest('id').content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(blog.Blog.objects.latest('id').content)), [])





