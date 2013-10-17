import datetime, markdown, re, os
from django.db import models
from django.conf import settings
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, GetPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetAuthors
from bs4 import BeautifulSoup


class Blog(models.Model):
    class Meta():
        app_label = "website"

    initial_image = models.TextField()
    author = models.CharField(max_length=1000)
    content = models.TextField()
    date = models.DateField()
    title = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id

def _set_markdown_language(source):
  #FIXME: need to set this so that it will register if there are multiple sourcecode languages in a blog. currently doesn't do that. Example of this would be in "Learning my way around gspread" blog.
  # set an empty variable here because you'll get errors on the blog index page if the variable isn't set
  language = ""

  ### this if/else group is to set match variable  so that it doesnt screw up the blog_index page, which also uses this logic
  if re.search('\[sourcecode language="(.*)"\]', source): 
    language = re.search('\[sourcecode language="(.*)"\]', source)
    #the following line catches any language names that are camel cased and lowercases them since our code highlighting parser needs all lower case
    language = language.group(1).lower() 
  return language

def _remove_wordpress_markup(source):
  #this method changes all the markup from wordpress into the right format for our syntax highlighter to recognize it.
  pattern_one = re.compile(r'\[sourcecode language="(.*)"\]|\[sourcecode\]')
  pattern_two = re.compile(r'\[caption.*\]')
  pattern_three = re.compile(r'\[/sourcecode\]')
  pattern_four = re.compile(r'\[/caption\]')

  parsed_content = pattern_one.sub(r'<pre class="brush:'+_set_markdown_language(source)+'">', source)
  parsed_content = pattern_two.sub(r'<caption>', parsed_content)
  parsed_content = pattern_three.sub(r'</pre>', parsed_content)
  parsed_content = pattern_four.sub(r'</caption>', parsed_content)
  return parsed_content
  
def _remove_html_tags(source):
  html_tags = re.compile(r'<.*?>')
  parsed_content = html_tags.sub(r'', source)
  return parsed_content

def _get_first_image(source):
  soup = BeautifulSoup(source.encode('ascii', 'ignore'))
  return str(soup.img)


def format_for_posts_index(all_posts):
  for blog in all_posts:
    blog.content = _remove_wordpress_markup(blog.content)
    blog.content = _remove_html_tags(blog.content)
  return all_posts


def format_blog_post( blog_post ):
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
      # here we add line to new_content before setting needs_highlighting to false because otherwise it will
      # add a <p></p> tag to the line that needs highlighting. We don't want that because it's sloppy.
      new_content += line+"\n"
      needs_highlighting = False
      # Now we need to have the line we just added not show up in the loop, or the last line of the code
      # will be duplicated OUTSIDE of the highlighted section. Again, something we don't want because it's sloppy.
      line = ""

    if needs_highlighting:
      new_content += line+"\n"
    else:
      new_content += "<p>"+line+"</p>\n"
  blog_post.content=new_content

  return blog_post

