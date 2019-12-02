from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class Goole_book_api_UnitTest(TestCase):
    def test_home_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_using_index_function(self):
        response = resolve('/')
        self.assertEqual(response.url_name, 'index')

    def test_home_contain_title(self):
        response = Client().get('/')
        title = "Book List"
        html_response = response.content.decode('utf8')
        self.assertIn(title, html_response)
