from django.test import TestCase, Client
from django.urls import reverse

from core import models


class BookModel(TestCase):
    def setUp(self):
        self.book = models.Book.objects.create(name='Test Book')

    def testStr(self):
        self.assertEqual(
            str(self.book),
            #self.book.name,
            'Test Book',
            'Строковое представление объекта должно возвращать название'
        )

class BookSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = models.Book.object.create(name='Test book 1')
        self.book2 = models.Book.object.create(name='Test book 2')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:book_list'))
        self.assertEqual(200, response.status_code)
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Book.objects.all()),
            'При поиске без параметров должны выводиться все книги'
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:book_list'), data={'name' : 'Test Book 1'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Html Css',
            response.context['object_list'].first().name,
        )

#     pass
# Create your tests here.
