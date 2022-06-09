from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        fields = ('username', 'email', 'password', 'first_name' , 'last_name', 'bio', 'user_permissions', 'is_active', 'is_staff',)
        read_only_fields = ('user_permissions', 'is_active', 'is_staff',)


class FormAttentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAttention
        fields = '__all__'


class FormPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormPersonality
        fields = '__all__'


class FormLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormLearning
        fields = '__all__'

