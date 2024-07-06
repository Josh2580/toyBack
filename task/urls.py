from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, AutoBotViewSet
# telegram_update, set_telegram_webhook, OrderViewSet
from rest_framework_nested import routers


# router = DefaultRouter()
# router.register(r'', TelegramUserViewSet)


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'all', TaskViewSet, basename='users_task')


router.register(r'bot', AutoBotViewSet, basename='users_bot')



urlpatterns = [
    path('', include(router.urls)),
    # path('', include(user_router.urls)),
    # path('webhook/', set_telegram_webhook, name='telegram_webhook'),
]