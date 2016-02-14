import hashlib
from django.core import exceptions as django_exc
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.helpers import validators
from src.common.libraries.constants import *
from src.common.models import User , Token
import requests
class UserLib():

    def password_hashing(self, password_hash, salt=None):
        if not salt:
            salt = User.objects.generate_salt()
        salted_client_hash = str(password_hash + salt)
        hash_library = hashlib.new(HASH_METHOD_USER_ADD)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    def is_unique_email(self, email):
        if not User.objects.filter(email=email).exists():
           return True
        raise django_exc.ValidationError('email address already exists', code=HTTP_400_BAD_REQUEST)

    def add_user(self, user_details):
        response = dict()
        if validators.validate_user_details(user_details) and  self.is_unique_email(user_details[KEY_EMAIL_ID]):
            server_hash, salt = self.password_hashing(user_details[KEY_PASSWORD_HASH])
            user_details[KEY_SALT] = salt
            user_details[KEY_PASSWORD_HASH] = server_hash
            AddRequest =  User.objects.create(**user_details)
            return "User Added"

    def authenticate_user(self, signin_details):
        print signin_details
        email = signin_details[KEY_EMAIL_ID]
        password_hash = signin_details[KEY_PASSWORD_HASH]
        validators.validate_signin_details(signin_details=signin_details)
        try:
            user = User.objects.get(email=email)
            print "success"
        except Exception as e:
            raise django_exc.ValidationError('Invalid Email Address', code=HTTP_400_BAD_REQUEST)
        hashed_salted_client_hash, salt = self.password_hashing(password_hash=password_hash, salt=user.salt)
        hash_stored_in_db = user.password_hash
        if hash_stored_in_db == hashed_salted_client_hash:
            token, created = Token.objects.get_or_create(user=user)
            return (token. access_token, created)
        raise django_exc.ValidationError('Invalid Password', code=HTTP_400_BAD_REQUEST)


    def authenticate(self, request):
        token = request['auth']
        id = request['id']
        URL = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={0}'.format(token)
        data = requests.get(URL)
        data = data.json()
        email = data['email']
        try:
            user = User.objects.get(email=email)
            token, created = Token.objects.get_or_create(user=user)
            return (token. access_token, created)
        except Exception as e:
            print "Not A Valid Email"
