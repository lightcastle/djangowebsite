import datetime, markdown, re, os
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings
from . import blog

def get_posts(request):
  b = blog.Blog()
  b.setup_posts_index()

  cont = Context({'title': 'Blog', 'all_posts': b.all_posts, 'current_time': 'current_time'})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(request))

def get_latest_blog(request):
  b = blog.Blog()
  b.latest_blog = b.all_posts[-1]
  cont = Context({'title': 'Blog', 'latest_post': b.latest_blog})
  return render_to_response('index.html', cont, context_instance=RequestContext(request))

def get_specific_post(request, post_id):
  b = blog.Blog()
  blog_post = b.get_specific_post(post_id)
  context = Context({'title': 'Blog', 'blog_post': blog_post})
  return render_to_response('blog_post.html', context, context_instance=RequestContext(request))


