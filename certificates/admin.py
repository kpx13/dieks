# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_license', 'show')
    ordering = ('name', )
    list_filter = ('is_license', 'show', )

admin.site.register(models.Certificate, CertificateAdmin)