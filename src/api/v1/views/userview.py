from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK
from src.api.v1.libraries import permissions
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from src.api.v1.serializers.usersserializer import UsersSerializer
from src.common.libraries.user.userlib import UserLib
from src.common.models.user import User
from src.common.libraries.constants import *
user_lib = UserLib()
from django_mysqlpool import auto_close_db
from src.common.helpers.Query2Dict import Query2DictConverter

'''
{
    "name": "Name Here",
    "email": "Email",
    "password_hash": "PASSWORD",
}
'''

class UserView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = User
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrCreate, )

    @auto_close_db
    def post(self, request):
        user_details = request.data.copy()
        user_details = Query2DictConverter(user_details, SIGNUP_FIELDS)
        payload = user_lib.add_user(user_details)
        return CustomResponse(message='User added', payload=payload, code=HTTP_201_CREATED)


