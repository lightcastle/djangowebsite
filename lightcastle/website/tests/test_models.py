from django.utils import unittest
from website import blog



class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.b = blog.Blog()
        self.b.setup_posts_index()


    def test_first_blog_title_is_correct(self):
        """The first blog ever published should be Python -- It's Classy """
        self.assertEqual(self.b.all_posts[-1].title, "Python -- It's Classy!")



