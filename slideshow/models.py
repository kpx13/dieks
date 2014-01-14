# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Slider(models.Model):
    image = models.ImageField(upload_to=lambda instance, filename: 'uploads/slider/' + pytils.translit.translify(filename), max_length=256, verbose_name=u'картинка')
    content = RichTextField(blank=True, verbose_name=u'контент')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й .. 5й')
    
    class Meta:
        verbose_name = u'слайдер'
        verbose_name_plural = u'слайдшоу'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return str(self.id)