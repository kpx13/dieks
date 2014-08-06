# -*- coding: utf-8 -*-

REGISTRATION_ALERT_TO = 'annkpx@gmail.com'

from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
import datetime
from django.core.mail import send_mail

from pages.models import Page
from slideshow.models import Slider
from feedback.forms import FeedbackForm
from request.forms import RequestForm
from review.models import Review
from partners.models import Partner
import contacts.views
import certificates.views
import forms

import config
from livesettings import config_value
from django.conf import settings


def send_mail_to_emploee(data, mail_to):
    text= u'Имя: ' + data['name'] + u"\n" + u'email: ' + data['email'] + '\n' + u'Телефон: ' + data['phone'] + '\n' + u'Письмо: ' + data['text'] + '\n'
    send_mail('Вам новое сообщение с сайта dieks.ru', text , 'noreply@dieks.ru', [mail_to], fail_silently=False)
    
def get_common_context(request):
    c = {}
    
    callform = FeedbackForm()
    requestform = RequestForm()
    if request.method == 'POST':
        if request.POST['action'] == 'call':
            callform = FeedbackForm(request.POST)
            if callform.is_valid():
		if request.POST.get('phone') != '123456':
	            callform.save()
                c['msg'] = u'Спасибо! Ваша заявка принята, в ближайшее время с Вами свяжутся.'
                callform = FeedbackForm()
            else:
                c['msg'] = u'Необходимо ввести имя и телефон.'
            c['show_callform'] = True
        elif request.POST['action'] == 'request':
            requestform = RequestForm(request.POST)
            if requestform.is_valid():
		if request.POST.get('phone') != '123456':
                    requestform.save()
                c['msg'] = u'Спасибо! Ваша заявка принята, в ближайшее время с Вами свяжутся.'
                requestform = RequestForm()
            else:
                c['msg'] = u'Необходимо ввести имя и телефон.'
            c['show_requestform'] = True

    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['callform'] = callform
    c['requestform'] = requestform
    c['request_url'] = request.path
    c['title'] = u'АНО Диэкс: промышленная безопасность, экспертиза, неразрушающий контроль'
    c['slideshow'] = Slider.objects.all()
    c['reviews'] = Review.objects.all()[:3]
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['is_home'] = 'true'
    page = Page.get_by_slug('home')
    if page:
        c.update(page)
        c['page_header'] = c['title']
        c['title'] = c['title'] + u' | АНО Диэкс: промышленная безопасность, экспертиза, неразрушающий контроль'
        return render_to_response('page.html', c)
    else:
        return HttpResponseNotFound('not found page')

def licenses_page(request):
    c = get_common_context(request)
    c['certificates'] = certificates.views.get_licenses()
    c['page_header'] = u'Лицензии'
    c['content'] = Page.get_by_slug('certificates')['content']
    return render_to_response('certificates.html', c)

def evidences_page(request):
    c = get_common_context(request)
    c['certificates'] = certificates.views.get_evidences()
    c['page_header'] = u'Свидетельства'
    c['content'] = Page.get_by_slug('certificates')['content']
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

def partners_page(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('partners'))
    c['documents'] = Review.objects.all()
    c['partners'] = Partner.objects.all()
    c['page_header'] = u'Партнеры'
    return render_to_response('partners.html', c)

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
