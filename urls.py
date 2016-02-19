from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from src.api.v1.views.userview import UserView
from src.api.v1.views.tokenview import TokenView
from src.api.v1.views.brandview import BrandView
from src.api.v1.views.mobileview import MobilesView
from src.api.v1.views.viewmobile import MobileView


urlpatterns = [
     url(r'^gomobi/admin/v1/user/$', UserView.as_view()),
     url(r'^gomobi/admin/v1/login/$', TokenView.as_view()),
     url(r'^gomobi/web/v1/brands/$', BrandView.as_view()),
     url(r'^gomobi/web/v1/mobiles/$', MobilesView.as_view()),
     url(r'^gomobi/web/v1/mobile/$', MobileView.as_view()),
     ]

