from django.test import TestCase
from django.core.urlresolvers import resolve
from tdd.views import home_page
from django.http import HttpRequest
# Create your tests here.

from django.template.loader import  render_to_string
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        expected_html=render_to_string('home.html')#获取页面内容
        self.assertEqual(response.content.decode(),expected_html)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

