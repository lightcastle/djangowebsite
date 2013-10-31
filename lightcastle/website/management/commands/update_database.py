from optparse import make_option
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
    option_list = BaseCommand.option_list + (
        make_option("--find-new-post",
            action='store_true',
            dest='find-new-post',
            default=False,
            help='Delete poll instead of closing it'),
        )

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
        self.all_posts = wp.call(GetPosts({'number': 100, 'post_status': 'publish'}))
        self.authors = wp.call(GetAuthors())
        self.all_posts = self.all_posts[::-1] #reverse the list of posts so that the most recent are last in the list


    def handle(self, *args, **options):

        if options['find-new-post']:
            #pass
            # potential code to update database
            for author in self.authors:
                if author.id == self.all_posts[-1].user:
                    self.all_posts[-1].author = author.display_name

            if blog._get_first_image(self.all_posts[-1].content) != "None":
                self.all_posts[-1].image = blog._get_first_image(self.all_posts[-1].content)
            else:
                self.all_posts[-1].image = ""


            if len(self.all_posts) == len(blog.Blog.objects.order_by('id')) + 1:
                new_post = blog.Blog(title=self.all_posts[-1].title, author=self.all_posts[-1].author,content=self.all_posts[-1].content,initial_image=self.all_posts[-1].image, date = self.all_posts[-1].date)
                new_post.save()

#http://stackoverflow.com/questions/4769004/learning-python-from-ruby-differences-and-similarities
        else:
#          this and the nested for-loop sets the author's display name because it isnt handled already by xmlrpc library
            for post in self.all_posts: 
                for author in self.authors:
                    if author.id == post.user:
                        post.author = author.display_name
#              following line sets the image variable so the posts index can display right
                if blog._get_first_image(post.content) != "None":
                    post.image = blog._get_first_image(post.content)
                else:
                    post.image = ""

                b = blog.Blog( title = post.title, author = post.author, initial_image = post.image, date = post.date, content = post.content)
                b.save()
#               self.stdout.write('wrote %r to the database\n' % b.title)







