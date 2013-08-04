from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import os
from django.conf import settings


def get_posts(req):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  all_posts = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  cont = Context({'title': 'Blog', 'all_posts': all_posts})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(req))

def get_specific_post(request, post_id):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
  post = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'})
  context = Context({'title': 'Blog', 'blog_post': post[post_id-1]})
  print post_id, post
  return render_to_response('blog_post.html', context, context_instance=RequestContext(request))





