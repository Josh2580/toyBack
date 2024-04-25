from django.urls import include, path
from rest_framework import routers
from toycoin import views


router = routers.DefaultRouter()
router.register(r'', views.ToyCoinViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
