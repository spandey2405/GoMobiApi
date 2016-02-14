from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from src.api.v1.views.userview import UserView
from src.api.v1.views.tokenview import TokenView
from src.api.v1.views.brandview import BrandView


urlpatterns = [
     url(r'^admin/v1/user/$', UserView.as_view()),
     url(r'^admin/v1/login/$', TokenView.as_view()),
     url(r'^gomobi/v1/brands/$', BrandView.as_view()),
     ]

