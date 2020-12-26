import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class UserRegistrationView(APIView):
    """ View for User Signup """

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            confirm_password = request.data['confirm_password']
        except KeyError as e:
            logging.getLogger('root').error(f'KeyError {str(e)}')
            return Response({'error_message': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        if password != confirm_password:
            logging.getLogger('root').error('Passwords do not match')
            return Response({'error_message': 'passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            logging.getLogger('root').error('Username already exists')
            return Response(
                {'error_message': 'username already exists. Try with another username.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            logging.getLogger('root').debug('User created')
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logging.getLogger('root').error(str(e))
            return Response(
                {'error_message': 'some error occurred. User creation failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

