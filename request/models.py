# -*- coding: utf-8 -*-

from django.db import models


class Request(models.Model):
    name  = models.CharField(u'ФИО', max_length=255)
    phone  = models.CharField(u'Телефон', max_length=255)
    text = models.TextField(u'Текст заявки', blank=True)
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заявка'
        verbose_name_plural = u'online заявки'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return str(self.name)

