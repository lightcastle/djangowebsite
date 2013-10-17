from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.conf import settings
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetAuthors
from bs4 import BeautifulSoup
from website.models import blog

class Command(BaseCommand):
    help = "updates the database of blog entries with the most current information"


    def handle(self, *args, **options):
        wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
        all_posts = wp.call(GetPosts({'number': 100, 'post_status': 'publish'}))
        authors = wp.call(GetAuthors())
        all_posts = all_posts[::-1] #reverse the list of posts so that the most recent are last in the list

        for post in all_posts: #this and the nested for-loop sets the author's display name because it isnt handled already by xmlrpc library
            for author in authors:
                if author.id == post.user:
                    post.author = author.display_name
#       following line sets the image variable so the posts index can display right
            if blog._get_first_image(post.content) != "None":
                post.image = blog._get_first_image(post.content)
            else:
              post.image = ""


            b = blog.Blog( title = post.title, author = post.author, initial_image = post.image, date = post.date, content = post.content)
            b.save()
#            self.stdout.write('wrote %r to the database\n' % b.title)

