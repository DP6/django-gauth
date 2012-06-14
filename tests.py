#coding:utf-8

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class AuthenticationViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_should_response_200(self):
        response = self.client.get('/gauth/')
        self.assertEquals(response.status_code, 200)
