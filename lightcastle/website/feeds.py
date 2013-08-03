from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import os


def get_posts(req):
  wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', os.environ.get("WORDPRESS_PASS", ""))
  all_posts = wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
  cont = Context({'title': 'Blog', 'all_posts': all_posts})
  return render_to_response('blog_home.html', cont, context_instance=RequestContext(req))

