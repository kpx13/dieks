# -*- coding: utf-8 -*-

import models

def insert_test_data():
    models.Employee.objects.all().delete()
    models.Employee(name=u'Крханбаров Рубен Оганесович', 
                    position=u'генеральный директор', 
                    code=103, 
                    email='ruben@dieks.ru',
                    sort_parameter=0).save()
    models.Employee(name=u'Зыков Александр Константинович', 
                    position=u'советник руководителя', 
                    email='zykov@dieks.ru',
                    sort_parameter=1).save()
    models.Employee(name=u'Еремин Борис Михайлович', 
                    position=u'технический директор', 
                    code=113, 
                    email='eremin@dieks.ru',
                    sort_parameter=3).save()                  
    models.Employee(name=u'Ториков Геннадий Иванович', 
                    position=u'исполнительный директор', 
                    code=111, 
                    email='torikov@dieks.ru',
                    sort_parameter=4).save()
    models.Employee(name=u'Кобелева Ольга Викторовна', 
                    position=u'главный бухгалтер', 
                    code=108, 
                    email='kobeleva@dieks.ru',
                    sort_parameter=5).save()
    models.Employee(name=u'Лысиков Александр Николаевич', 
                    position=u'заместитель технического директора, начальник аттестационного центра, аттестация экспертов', 
                    code=112, 
                    email='a.lysikov@dieks.ru',
                    sort_parameter=6).save()
    models.Employee(name=u'Золотаренко Юрий Васильевич', 
                    position=u'начальник группы, аттестация и аккредитация лабораторий, экспертных организаций и инспекционный контроль, разрешение на промышленное применение', 
                    code=105, 
                    email='zolotarenko@dieks.ru',
                    sort_parameter=7).save()
    models.Employee(name=u'Постовалов Владимир Александрович', 
                    position=u'аккредитация НАМЦ, оформление результатов аттестации специалистов НК, ведение Реестра', 
                    code=102, 
                    email='postovalov@dieks.ru',
                    sort_parameter=8).save()
    models.Employee(name=u'Агиевич Иван Васильевич', 
                    position=u'аккредитация НАМЦ, предаттестационная подготовка руководителей и специалистов по промышленной безопасности, экспертиза промышленной безопасности объектов горнорудной и угольной промышленности', 
                    code=110, 
                    email='agievich@dieks.ru',
                    sort_parameter=9).save()          
    models.Employee(name=u'Данилов Валерий Николаевич', 
                    position=u'экспертиза промышленной безопасности, техническая диагностика (К, П, С, М, Г, У, Н), аттестация лабораторий НК', 
                    code=106, 
                    email='danilov@dieks.ru',
                    sort_parameter=10).save()
    models.Employee(name=u'Ундаков Михаил Вячеславович', 
                    position=u'экспертиза промышленной безопасности, техническая диагностика (К, П, С, М, Г, У, Н)', 
                    code=114, 
                    email='undakov@dieks.ru',
                    sort_parameter=11).save()         
    models.Employee(name=u'Дерунов Алексей Николаевич', 
                    position=u'экспертиза промышленной безопасности, техническая диагностика (К, П, С, М, Г, У, Н), аттестация лабораторий НК', 
                    code=106, 
                    email='derunov@dieks.ru',
                    sort_parameter=12).save()
    models.Employee(name=u'Дорофеенков Евгений Николаевич', 
                    position=u'экспертиза промышленной безопасности объектов газораспределения и газопотребления', 
                    code=104, 
                    email='dorofeenkov@dieks.ru',
                    sort_parameter=13).save()
    models.Employee(name=u'Блохина Ольга Юрьевна', 
                    position=u'оформление документов', code=109, 
                    email='blohina@dieks.ru',
                    sort_parameter=14).save()
    models.Employee(name=u'Андреева Светлана Анатольевна', 
                    position=u'инспектор по делопроизводству и персоналу', 
                    code=107, 
                    email='andreeva@dieks.ru',
                    sort_parameter=15).save()
    models.Employee(name=u'Лысиков Владислав Александрович', 
                    position=u'аккредитация лабораторий и экспертных организаций, аттестация экспертов', 
                    code=116, 
                    email='v.lysikov@dieks.ru',
                    sort_parameter=16).save()
    models.Employee(name=u'Аня', 
                    position=u'администратор сайта', 
                    code=116, 
                    email='annkpx@gmail.com',
                    sort_parameter=16).save()

    
def get_staff():
    return [ {'id': a.id,
              'name': a.name,
              'position': a.position,
              'code': a.code,
              'email': a.email,
              } for a in models.Employee.objects.filter(show=True).order_by('sort_parameter')]    