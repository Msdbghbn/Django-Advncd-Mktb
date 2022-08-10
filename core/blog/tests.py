from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .views import IndexView
# Create your tests here.
class TestUrl(TestCase):

    def test_blog_index_url_resolver(self):
        url=reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class,IndexView)