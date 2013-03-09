# -*- coding: utf-8 -*-
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'имя')
    position= models.CharField(max_length=128, verbose_name=u'должность')
    code= models.IntegerField(blank=True, null=True, verbose_name=u'добавочный код')
    email = models.EmailField(blank=True, null=True, verbose_name=u'email')
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'параметр для сортировки')
    class Meta:
        verbose_name = u'сотрудник'
        verbose_name_plural = u'сотрудники'
    def __unicode__(self):
        return self.name