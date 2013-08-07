from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import os
from django.conf import settings
import datetime
import markdown
import re


def get_posts(request):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  all_posts = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  _remove_wordpress_markup(all_posts)

  current_time = datetime.datetime.now()
  cont = Context({'title': 'Blog', 'all_posts': parsed_content, 'current_time': current_time})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(request))

def get_specific_post(request, post_id):
  post_id = int(post_id) - 1
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  blog_post = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  blog_post = blog_post[post_id]
  _remove_wordpress_markup(blog_post)
  context = Context({'title': 'Blog', 'blog_post': parsed_content})
  return render_to_response('blog_post.html', context, context_instance=RequestContext(request))


def _remove_wordpress_markup(source):
  language = re.search(r'[sourcecode language="(.*)"]', source)
  parsed_content = re.sub(r'[sourcecode language=.*]', "<code class="+str(language.group())+">", source)
#  remove [caption]
  return parsed_content
  
  
  
  
