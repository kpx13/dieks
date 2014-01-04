# -*- coding: utf-8 -*-

REGISTRATION_ALERT_TO = 'annkpx@gmail.com'

from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
import datetime

from pages.models import Page
import contacts.views
import news.views
import certificates.views
import forms

def send_mail_to_emploee(data, mail_to):
    from django.core.mail import send_mail
    text= u'Имя: ' + data['name'] + u"\n" + u'email: ' + data['email'] + '\n' + u'Телефон: ' + data['phone'] + '\n' + u'Письмо: ' + data['text'] + '\n'
    send_mail('Вам новое сообщение с сайта dieks.ru', text , 'noreply@dieks.ru', [mail_to], fail_silently=False)
    
def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['title'] = u'АНО Диэкс: промышленная безопасность, экспертиза, неразрушающий контроль'
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    return render_to_response('home.html', c)

def news_page(request):
    c = get_common_context(request)
    c['news'] = news.views.get_news()
    c['page_header'] = u'Новости'
    c['is_home'] = 'true'
    return render_to_response('news.html', c)

def licenses_page(request):
    c = get_common_context(request)
    c['certificates'] = certificates.views.get_licenses()
    print c['certificates']
    c['page_header'] = u'Лицензии'
    return render_to_response('certificates.html', c)

def evidences_page(request):
    c = get_common_context(request)
    c['certificates'] = certificates.views.get_evidences()
    print c['certificates']
    c['page_header'] = u'Свидетельства'
    return render_to_response('certificates.html', c)

def contacts_page(request, contact_id=0):
    c = get_common_context(request)
    c['contacts'] = contacts.views.get_staff()
    c['page_header'] = u'Контакты'
    
    if request.method == 'POST':
        form = forms.MailForm(request.POST)
        if form.is_valid():
            send_mail_to_emploee(form.cleaned_data, request.POST['mail_to'])
            return HttpResponseRedirect('/contacts')
        else:
            c['mail_form'] = form
            c['contact_id'] = int(contact_id)
    else:
        c['mail_form'] = forms.MailForm()
    
    
    return render_to_response('contacts.html', c)

def get_page(request, page_name):
    c = get_common_context(request)
    page = Page.get_by_slug(page_name)
    if page:
        c.update(page)
        c['page_header'] = c['title']
        c['title'] = c['title'] + u' | АНО Диэкс: промышленная безопасность, экспертиза, неразрушающий контроль'
        return render_to_response('page.html', c)
    else:
        return HttpResponseNotFound('not found page')
