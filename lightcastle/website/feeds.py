from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetAuthors
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import os
from django.conf import settings
import datetime
import markdown
import re
from bs4 import BeautifulSoup


def get_posts(request):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  all_posts = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  authors = wp.call(GetAuthors())
  for blog in all_posts:
    if _get_first_image(blog.content) != None:
      blog.image = _get_first_image(blog.content)
    blog.content = _remove_wordpress_markup(blog.content)
    blog.content = _remove_html_tags(blog.content)
    for index in authors:
      if index.id == blog.user:
        blog.author = index.display_name 

  current_time = datetime.datetime.now()
  cont = Context({'title': 'Blog', 'all_posts': all_posts, 'current_time': current_time})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(request))


def get_specific_post(request, post_id):
  post_id = int(post_id) - 1
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  blog_post = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  authors = wp.call(GetAuthors())
  blog_post = blog_post[post_id]
  blog_post.content = _remove_wordpress_markup(blog_post.content)

  new_content = ""
  for line in blog_post.content.split("\n"):
    new_content += "<p>"+line+"</p>\n"

  blog_post.content=new_content

  for index in authors:
    if index.id == blog_post.user:
      blog_post.author = index.display_name 


  context = Context({'title': 'Blog', 'blog_post': blog_post})
  return render_to_response('blog_post.html', context, context_instance=RequestContext(request))


def get_latest_blog(request):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  all_posts = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  latest_post = all_posts[0]
  authors = wp.call(GetAuthors())
  for index in authors:
    if index.id == latest_post.user:
      latest_post.author = index.display_name 

  latest_post.content = _remove_wordpress_markup(latest_post.content)
  latest_post.content = _remove_html_tags(latest_post.content)

  cont = Context({'title': 'Blog', 'latest_post': latest_post})
  return render_to_response('index.html', cont, context_instance=RequestContext(request))





def _remove_wordpress_markup(source):
  pattern_one = re.compile(r'\[sourcecode language="(.*)"\]')
  pattern_two = re.compile(r'\[caption.*?\]')
  pattern_three = re.compile(r'\[/sourcecode\]')

  parsed_content = pattern_one.sub(r'[code class="\1"]', source)
  parsed_content = pattern_two.sub(r'', parsed_content)
  parsed_content = pattern_three.sub(r'[/code]', parsed_content)

  return parsed_content
  

def _remove_html_tags(source):
  pattern_three = re.compile(r'<.*?>')
  parsed_content = pattern_three.sub(r'', source.encode('ascii', 'ignore')
  return parsed_content

def _get_first_image(source):
  soup = BeautifulSoup(source)
  return soup.a

