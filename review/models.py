# -*- coding: utf-8 -*-
from django.db import models
from pytils import dt, translit
import pytils

class Review(models.Model):
    name  = models.CharField(u'название', max_length=255)
    logo = models.ImageField(upload_to=lambda instance, filename: 'uploads/reviews/' + pytils.translit.translify(filename), max_length=256, verbose_name=u'лого')
    text = models.TextField(u'текст')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-request_date']

    def __unicode__(self):
        return self.name
