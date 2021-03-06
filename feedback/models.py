# -*- coding: utf-8 -*-

from django.db import models


class Feedback(models.Model):
    name  = models.CharField(u'Имя', max_length=255)
    phone  = models.CharField(u'Телефон', max_length=255)
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заявка'
        verbose_name_plural = u'заявки на обратный звонок'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return self.name

