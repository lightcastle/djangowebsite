from django.utils import unittest
from website.models import blog
from website.management.commands.update_database import Command
import re



class BlogTestCase(unittest.TestCase):
    def setUp(self):
#        self.b = Blog()
        c = Command()
        c.handle()



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





