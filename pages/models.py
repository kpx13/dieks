# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'заголовок')
    content = RichTextField(blank=True, verbose_name=u'html-содержимое')
    slug = models.SlugField(max_length=200, blank=True, verbose_name=u'url страницы')
    header_content = models.TextField(blank=True, verbose_name=u'header-содержимое')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            page = Page.objects.get(slug=page_name)
            return {'title': page.title,
                'content': page.content,
                'header': page.header_content
                }
        except:
            return None
    
    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'
        
    def __unicode__(self):
        return self.slug
