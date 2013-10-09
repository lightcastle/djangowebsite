from django.utils import unittest
from website import blog
import re



class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.b = blog.Blog()



    def test_setup_posts_index_method(self):
        """Last blog title in index should be Python -- It's Classy! when using the setup posts index class method"""
        self.b.setup_posts_index()
        self.assertEqual(self.b.all_posts[0].title, "Python -- It's Classy!")

    def test_get_specific_post_method(self):
        self.assertEqual(self.b.get_specific_post(1).title, "Python -- It's Classy!")


    def test_get_first_image_method(self):
        """_get_first_image method should return the first <img> tag of the first blog entry, in this case, a python image"""
        self.assertEqual(blog._get_first_image(self.b.all_posts[-1].content), '<img alt="Python Logo" class="size-medium wp-image-37 alignright" height="79" src="http://lightcastletech.files.wordpress.com/2012/08/486px-python_logo-svg.png?w=300" title="486px-Python_logo.svg" width="269"/>')


    def test_remove_html_tags(self):
        """"content should be without any html tags in it"""
        html = re.compile('<\w*>')
        self.assertEqual(html.findall(blog._remove_html_tags(self.b.all_posts[15].content)), [])
        self.assertEqual(html.findall(blog._remove_html_tags(self.b.all_posts[22].content)), [])
        self.assertEqual(html.findall(blog._remove_html_tags(self.b.all_posts[-1].content)), [])
        self.assertEqual(html.findall(blog._remove_html_tags(self.b.all_posts[0].content)), [])



    def test_remove_wordpress_markup(self):
        """"content should be without any wordpress tags in it"""
        wordpress = re.compile('\[sourcecode\]')
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(self.b.all_posts[15].content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(self.b.all_posts[22].content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(self.b.all_posts[-1].content)), [])
        self.assertEqual(wordpress.findall(blog._remove_wordpress_markup(self.b.all_posts[0].content)), [])





