# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Request


class OrderAdmin(admin.ModelAdmin):
    list_display = ('request_date', 'name', 'phone', 'text')

admin.site.register(Request, OrderAdmin)