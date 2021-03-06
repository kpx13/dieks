# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'text')

admin.site.register(models.Page, PageAdmin)