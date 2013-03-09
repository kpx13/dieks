# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'code', 'email', 'show')
    search_fields = ('name', 'position', 'email')
    ordering = ('sort_parameter', )

admin.site.register(models.Employee, EmployeeAdmin)