# -*- coding: utf-8 -*-
from django import forms

class MailForm(forms.Form):
    name = forms.CharField(max_length=256, label = u'ФИО')
    email = forms.EmailField(required=False, label = u'e-mail')
    phone = forms.CharField(max_length=20, required=False, label = u'телефон')
    text = forms.CharField(max_length=500, label = u'сообщение', widget=forms.widgets.Textarea)