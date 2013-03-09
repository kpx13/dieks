# -*- coding: utf-8 -*-

import models

def insert_test_data():
    models.Certificate.objects.all().delete()
    models.Certificate(name=u'Лицензия на проведение экспертизы промышленной безопасности (дж)',
                       image='uploads/certificates/pic28.jpg',
                       document='uploads/certificates/pdf28.pdf',
                       is_license=True).save()
    models.Certificate(name=u'НОАЛ',
                       image='uploads/certificates/pic27.jpg',
                       document='uploads/certificates/pdf27.pdf',
                       is_license=False).save()
    
def get_licenses():
    return [ {'id': a.id,
              'name': a.name,
              'image': a.image,
              'document': a.document
              } for a in models.Certificate.objects.filter(show=True).filter(is_license=True)]
    
def get_evidences():
    return [ {'id': a.id,
              'name': a.name,
              'image': a.image,
              'document': a.document
              } for a in models.Certificate.objects.filter(show=True).filter(is_license=False)]     