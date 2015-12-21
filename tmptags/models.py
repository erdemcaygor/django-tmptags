# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Deneme(models.Model):

    is_active = models.BooleanField(default=False, verbose_name='Aktif mi?')
    name = models.CharField(max_length=50, verbose_name='İsim')
    is_deleted = models.BooleanField(default=False, verbose_name='Silindi Mi?')
    salary = models.IntegerField(verbose_name='Gelir')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Deneme'
