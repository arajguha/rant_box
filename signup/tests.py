import logging

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import UserRegistrationView
from django.contrib.auth.models import User


class UserSignupTest(TestCase):
    """ Test class for User registration """

    def test_user_signup(self):
        """ create a new user """
        factory = APIRequestFactory()
        user = {
            "username": "test123",
            "password": "random",
            "confirm_password": "random"
        }
        request = factory.post('signup/', user)
        view = UserRegistrationView.as_view()
        response = view(request)

        logging.getLogger('test').debug(f'[test_user_signup] result: {response.status_code} expected: {201}')
        self.assertEqual(response.status_code, 201)


    def test_user_different_pwd(self):
        """ passwords do not match """
        factory = APIRequestFactory()
        user = {
            "username": "test123",
            "password": "random",
            "confirm_password": "random123"
        }
        request = factory.post('signup/', user)
        view = UserRegistrationView.as_view()
        response = view(request)

        logging.getLogger('test').debug(f'[test_user_different_pwd] result: {response.status_code} expected: {400}')
        self.assertEqual(response.status_code, 400)


    def test_user_no_confirm_pwd(self):
        """ no confirm password provided """
        factory = APIRequestFactory()
        user = {
            "username": "test123",
            "password": "random",
        }
        request = factory.post('signup/', user)
        view = UserRegistrationView.as_view()
        response = view(request)

        logging.getLogger('test').debug(f'[test_user_no_confirm_pwd] result: {response.status_code} expected: {400}')
        self.assertEqual(response.status_code, 400)


    def test_same_user_signup(self):
        """ user already exists """
        user = User.objects.create_user(username='test123', password='random')
        factory = APIRequestFactory()
        user = {
            "username": "test123",
            "password": "random",
            "confirm_password": "random"
        }
        request = factory.post('signup/', user)
        view = UserRegistrationView.as_view()
        response = view(request)

        logging.getLogger('test').debug(f'[test_same_user_signup] result: {response.status_code} expected: {400}')
        self.assertEqual(response.status_code, 400)
