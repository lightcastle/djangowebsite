import datetime, markdown, re, os
from django.conf import settings
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetAuthors
from bs4 import BeautifulSoup

def _remove_wordpress_markup(source):
  pattern_one = re.compile(r'\[sourcecode language="(.*)"\]|\[sourcecode\]')
  pattern_two = re.compile(r'\[caption.*\]')
  pattern_three = re.compile(r'\[/sourcecode\]')
  pattern_four = re.compile(r'\[/caption\]')

  if re.search('\[sourcecode language="(.*)"\]', source): ### this if/else group is to set match so that it doesnt interfere with the blog_index page, which also calls this function. could break this out into a separate method. TODO clean this up
    match = re.search('\[sourcecode language="(.*)"\]', source)
    match = match.group(1).lower() #this catches anything that is camel cased and lowercases it since our code highlighting parser needs all lower case
  else:
    match = "" # set an empty variable here because you'll get errors on the blog index page if there is no sourcecode language found
    
  parsed_content = pattern_one.sub(r'<pre class="brush:'+match+'">', source)
  parsed_content = pattern_two.sub(r'<caption>', parsed_content)
  parsed_content = pattern_three.sub(r'</pre>', parsed_content)
  parsed_content = pattern_four.sub(r'</caption>', parsed_content)
  return parsed_content
  
def _remove_html_tags(source):
  pattern_three = re.compile(r'<.*?>')
  parsed_content = pattern_three.sub(r'', source)
  return parsed_content

def _get_first_image(source):
  soup = BeautifulSoup(source.encode('ascii', 'ignore'))
  return str(soup.img)


class Blog():
  def __init__(self):
    self.wp = Client('http://lightcastletech.wordpress.com/xmlrpc.php', 'brownj@lightcastletech.com', settings.WORDPRESS_PASS)
    self.all_posts = self.wp.call(GetPosts({'orderby': 'post_modified', 'number': 100, 'post_status': 'publish'}))
    self.authors = self.wp.call(GetAuthors())
    for post in self.all_posts: #this and the nested for-loop sets the author's display name because it isnt handled already by xmlrpc library
      for author in self.authors:
        if author.id == post.user:
          post.author = author.display_name 
      if _get_first_image(post.content) != "None": #sets the image variable so the posts index can display right
        post.image = _get_first_image(post.content)

  def setup_posts_index(self):
    for blog in self.all_posts:
      blog.content = _remove_wordpress_markup(blog.content)
      blog.content = _remove_html_tags(blog.content)
    return self.all_posts

  def get_specific_post(self, post_id):
    post_id = int(post_id) - 1
    blog_post = self.all_posts[post_id]
    blog_post.content = _remove_wordpress_markup(blog_post.content)

    ##TODO: this section should be changed to use beautifulsoup html parser because regex doesnt quite do the job. changing it should clean the code up a bit
    needs_highlighting = False
    pre = re.compile(r'<pre.*?>')# these 2 lines used to determine where code highlighting is needed
    closing_pre = re.compile(r'</pre>')
  
    new_content = ""
    for line in blog_post.content.split("\n"):
      if pre.search(line):
        needs_highlighting = True
      elif closing_pre.search(line):
        needs_highlighting = False

      if needs_highlighting:
        new_content += line+"\n"
      else:
        new_content += "<p>"+line+"</p>\n"
    blog_post.content=new_content

    return blog_post



