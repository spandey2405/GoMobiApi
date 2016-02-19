from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK
from src.api.v1.libraries import permissions
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from src.api.v1.serializers import BrandSerializer
from src.common.libraries.mobiles.mobilelib import MobileLib
from src.common.models.mobiles import Mobiles
from django_mysqlpool import auto_close_db
api_lib = MobileLib()

'''
{
    "name": "Saurabh Pandey",
    "email": "scoder91@gmail.com",
    "password_hash": "gomobiSearch@admin@api@1121",
}
'''

class MobilesView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Mobiles
    serializer_class = BrandSerializer
    # permission_classes = (permissions.IsAuthenticated, )

    @auto_close_db
    def get(self,request):
        Query = request.GET.copy()
        payload = api_lib.get_mobile(mobilename=Query)
        return CustomResponse(message='User added', payload=payload, code=HTTP_200_OK)



