from django.conf.urls import re_path, include
from listings import views
from rest_framework_mongoengine.routers import DefaultRouter

router = DefaultRouter()
router.register(r'listings', views.AdvListingViewSet)

urlpatterns = [
    re_path('^', include(router.urls))
]
