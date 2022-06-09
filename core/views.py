from rest_framework import viewsets
from .models import FormAttention, FormPersonality, FormLearning
from django.http import HttpResponseForbidden
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FormAttentionViewSet(viewsets.ModelViewSet):
    queryset = FormAttention.objects.all()
    serializer_class = FormAttentionSerializer


class FormPersonalityViewSet(viewsets.ModelViewSet):
    queryset = FormPersonality.objects.all()
    serializer_class = FormPersonalitySerializer


class FormLearningViewSet(viewsets.ModelViewSet):
    queryset = FormLearning.objects.all()
    serializer_class = FormLearningSerializer
