from django.urls import path
from .views import *
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='User')
router.register('permissions', LGPDPermissionsViewSet, basename='LGPDPermissions')
router.register('formattention', FormAttentionViewSet, basename='FormAttention')
router.register('formpersonality', FormPersonalityViewSet, basename='FormPersonality')
router.register('formlearning', FormLearningViewSet, basename='FormLearning')


urlpatterns = [
    path('', include(router.urls) ),
]
