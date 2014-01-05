# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Feedback


class OrderAdmin(admin.ModelAdmin):
    list_display = ('request_date', 'name', 'phone', )

admin.site.register(Feedback, OrderAdmin)