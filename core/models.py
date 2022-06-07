from django.contrib.auth.models import User
from django.db import models

from .choices import *



class FormAttention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questao1 = models.CharField(max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False)
    questao2 = models.CharField(max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False)
    questao3 = models.CharField(max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False)
    questao4 = models.CharField(max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False)
    questao5 = models.CharField(max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False)


class FormPersonality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questao1 = models.CharField(max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False)
    questao2 = models.CharField(max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False)
    questao3 = models.CharField(max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False)


class FormLearning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questao1 = models.CharField(max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False)
    questao2 = models.CharField(max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False)
    questao3 = models.CharField(max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False)
    questao6 = models.CharField(max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False)
    questao5 = models.CharField(max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False)