# -*- coding: utf-8 -*-
from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'название')
    image = models.FileField(upload_to= 'uploads/certificates',max_length=128, verbose_name=u'изображение')
    document = models.FileField(upload_to= 'uploads/certificates',max_length=128, verbose_name=u'документ')
    is_license = models.BooleanField(verbose_name=u'это лицензия? (да) или свидетельство (нет)')
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?')
    class Meta:
        verbose_name = u'сертификат'
        verbose_name_plural = u'сертификаты'
    def __unicode__(self):
        return self.name
