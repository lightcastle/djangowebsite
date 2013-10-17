import datetime, markdown, re, os
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings
from .models import blog

def get_posts(request):
  b = blog.format_for_posts_index(blog.Blog.objects.all())
  cont = Context({'title': 'Blog', 'all_posts': b, 'current_time': 'current_time'})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(request))

def get_latest_blog(request):
  b = blog.Blog.objects.latest('id')
  cont = Context({'title': 'Blog', 'latest_post': b, 'blog_id': b.id})
  return render_to_response('index.html', cont, context_instance=RequestContext(request))

def get_specific_post(request, post_id):
  blog_post = blog.format_blog_post(blog.Blog.objects.get(id=post_id))
  context = Context({'title': 'Blog', 'blog_post': blog_post})
  return render_to_response('blog_post.html', context, context_instance=RequestContext(request))


