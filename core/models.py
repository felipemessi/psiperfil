import json
from django.contrib.auth.models import User
from django.db import models

from .choices import *


class FormAttention(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao4 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao5 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )

    def __str__(self):
        return json.dumps({
            "user": self.user.username,
            "questao1": self.questao1,
            "questao2": self.questao2,
            "questao3": self.questao3,
            "questao4": self.questao4,
            "questao5": self.questao5,
        })


class FormPersonality(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )

    def __str__(self):
        return json.dumps({
            "user": self.user.username,
            "questao1": self.questao1,
            "questao2": self.questao2,
            "questao3": self.questao3,
        })


class FormLearning(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao4 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao5 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )

    def __str__(self):
        return json.dumps({
            "user": self.user.username,
            "questao1": self.questao1,
            "questao2": self.questao2,
            "questao3": self.questao3,
            "questao6": self.questao6,
            "questao5": self.questao5,
        })
