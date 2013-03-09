# -*- coding: utf-8 -*-

import models

def get_page(page_name):
    try:
        page = models.Page.objects.get(slug=page_name)
        return {'title': page.title,
                'content': page.content,
                'header': page.header_content
                }
    except:
        return None
    
def insert_test_data():
    models.Page.objects.all().delete()
    models.Page(slug=u'about',
                title=u'О компании',
                content="""
                <p>
Автономная некоммерческая организация &laquo;Техническая диагностика и экспертиза&raquo; (АНО &laquo;ДИЭКС&raquo;) - одна из ведущих организаций системы Ростехнадзора в области промышленной безопасности. Более чем семнадцатилетний опыт работы в области экспертизы на объектах, подконтрольных Ростехнадзору. Высокая квалификация специалистов организации по праву обеспечивает АНО &laquo;ДИЭКС&raquo; одно из лидирующих положений среди экспертных организаций и репутацию надежного партнера. 
</p>
<p>
АНО &laquo;ДИЭКС&raquo; действует на рынке экспертных услуг России с 1991 года. В организации работают профессиональные эксперты, опытные высококвалифицированные специалисты неразрушающего контроля, преподаватели по подготовке в области промышленной безопасности системы Ростехнадора и Минобразования. 
</p>
Организация с 1999 года является Территориальным уполномоченным органом Единой системы оценки соответствия в области промышленной, экологической безопасности, безопасности в энергетике и строительстве.
<p>

                """ ).save()
    
    models.Page(slug=u'services',
                title=u'Услуги',
                content="""
                <p>
Автономная некоммерческая организация &laquo;Техническая диагностика и экспертиза&raquo; (АНО &laquo;ДИЭКС&raquo;) предлагает следующие услуги: 
</p>
<br />
<p>
АНО &laquo;ДИЭКС&raquo; проводит экспертизу промышленной безопасности проектной документации на строительство, расширение, реконструкцию, техническое перевооружение, консервацию и ликвидацию опасных производственных объектов. 
</p>
<br />
<p>
Проведение экспертизы промышленной безопасности технических устройств, применяемых на опасных производственных объектах, предусматривает техническое диагностирование и выполнение контроля оборудования и материалов методами неразрушающего контроля. При этом специалисты АНО &laquo;ДИЭКС&raquo; используют радиационный, акустический, магнитный и другие методы неразрушающего контроля на следующих объектах контроля: 
</p>
<ul>
    <li>объекты котлонадзора;</li>
    <li>системы газоснабжения (газораспределения) ;</li>
    <li>подъемные сооружения;</li>
    <li>объекты горнорудной промышленности;</li>
    <li>объектов угольной промышленности;</li>
    <li>оборудование нефтяной и газовой промышленности;</li>
    <li>оборудование металлургической промышленности;</li>
    <li>оборудование нефтехимической и нефтеперерабатывающей промышленности;</li>
    <li>оборудование взрывопожароопасных, химически опасных производств;</li>
    <li>объекты железнодорожного транспорта.</li>
</ul>
<br />
<p>
Проведение экспертизы промышленной безопасности зданий и сооружений на опасных производственных объектах.
</p>
<br />
<p>
Проведение экспертизы промышленной безопасности иных документов, связанных с эксплуатацией опасных производственных объектов.
</p>
<br />
<p>
Аккредитация экспертных организаций, испытательных лабораторий (ЛНК, ЛРК) во всех отраслях надзора.
</p>
<br />
<p>
Кроме этого АНО &laquo;ДИЭКС&raquo; в области котлонадзора, газового надзора, подъемных сооружений осуществляет следующие виды деятельности: 
</p>
<ul>
    <li>аккредитация экспертных организаций; испытательных лабораторий;независимых аттестационно &ndash; методических центров (организаций по подготовке в системе аккредитации в области промышленной безопасности), осуществляющих подготовку специалистов и руководителей в Единой системе оценки соответствия в области промышленной, экологической безопасности, безопасности в энергетике и строительстве;</li>
    <li>аттестация экспертов Единой системы оценки соответствия;</li>
    <li>аттестация лабораторий неразрушающего контроля;</li>
    <li>аттестация (переаттестация) специалистов неразрушающего контроля I и II уровней квалификации;</li>
    <li>аттестация электролабораторий.</li>
</ul>
<br />
<p>
Выполняет работы по сертификации и оформлению разрешения на применение техники, в том числе и импортной, регистрируемой в газовом надзоре, котлонадзоре и надзоре за подъемными сооружениями. 
</p>
<br />
<p>
В области охраны труда АНО &laquo;ДИЭКС&raquo; проводит обучение, повышение квалификации руководителей, специалистов и рабочих, обслуживающих объекты, подконтрольные Ростехнадзору.
</p>
<br />
<p>
На все виды деятельности АНО &laquo;ДИЭКС&raquo; имеет лицензии Ростехнадзора и Департамента образования г. Москвы, свидетельства по аккредитации.
</p>
<br />
<p>
Данные услуги оказывают высококвалифицированные специалисты, аттестованные в установленном порядке.
</p>
                """ ).save()
    
    models.Page(slug=u'proposals',
                title=u'Формы заявок',
                content="""
                <p>
<strong>1. Заявление на выдачу разрешения на применение </strong>(<a href="/media/uploads/proposals/perm_use.doc">Скачать ...</a>); 
</p>
<br />
<p>
<strong>2. Заявка на проведение аттестации руководителей и специалистов организаций, поднадзорных Ростехнадзору </strong>(<a href="/media/uploads/proposals/atest_ruk.doc">Скачать ...</a>); 
</p>
<br />
<p>
<strong>3. Аттестация лабораторий неразрушающего контроля (ЛНК):</strong> 
</p>
<ul>
    <li>Анкета - вопросник с данными о состоянии ЛНК (<a href="/media/uploads/proposals/att_lab_form.doc">Скачать ...</a>);</li>
    <li>Список документов, предоставляемых при аттестации ЛНК (<a href="/media/uploads/proposals/att_lab_doc.doc">Скачать ...</a>);</li>
    <li>Заявка на аттестацию ЛНК (<a href="/media/uploads/proposals/att_lab_form.doc">Скачать ...</a>);</li>
</ul>
<br />
<p>
<strong>4.Подготовка и аттестация персонала в области неразрушающего контроля (НК):</strong> 
</p>
<ul>
    <li>Регистрационная карточка (<a href="/media/uploads/proposals/reg_card1.doc">Скачать ...</a>);</li>
    <li>Заявка на проведение аттестации персонала в области НК (<a href="/media/uploads/proposals/spec-NK-24-12-2010.doc">Скачать ...</a>);</li>
    <li>Анкета специалиста НК (<a href="/media/uploads/proposals/spec-NK-06-08-2009.doc">Скачать ...</a>)</li>
    <li>Приложение 1. Согласие на обработку персональных данных НК (<a href="/media/uploads/proposals/Pril.1. Personalnie dannie NK.doc">Скачать ...</a>)
    </li>
</ul>
<br />
<p>
<strong>5.Подготовка и аттестация экспертов:</strong> 
</p>
<ul>
    <li>Полный перечень областей аккредитации ЭО, НОА и экспертов (<a href="/media/uploads/proposals/Oblasti%20akkreditacii%20EO%20NOA%20ekspertov_1.doc">Скачать ...</a>);</li>
    <li>Аттестация в качестве эксперта в газовом хозяйстве (<a href="/media/uploads/proposals/Zayavka - Gaz.doc">Скачать ...</a>);</li>
    <li>Аттестация в качестве эксперта на объектах котлонадзора (<a href="/media/uploads/proposals/Zayavka - Kotl.doc">Скачать ...</a>);</li>
    <li>Аттестация в качестве эксперта на подъемных сооружениях (<a href="/media/uploads/proposals/Zayavka - PS.doc">Скачать ...</a>);</li>
    <li>Аттестация в качестве специалиста-обследователя 1-го, 2-го и 3-го уровней квалификации на подъемных сооружениях (<a href="/media/uploads/proposals/Zayavka - PS specialist.doc">Скачать ...</a>);</li>
</ul>
<ul>
    <li>Квалификационная карточка (<a href="/media/uploads/proposals/prep_exp_qualification.doc">Скачать ...</a>);</li>
    <li class="text">Аттестация в качестве эксперта осуществляющего экспертизу промышленной безопасности зданий и сооружений (промышленные дымовые и вентиляционные трубы) на ОПО (<a href="/media/uploads/proposals/Zayavka - ZD &amp; Soor.doc">Скачать ...</a>)</li>
    <li>Приложение 2. Согласие на обработку персональных данных экспертов НОА (<a href="/media/uploads/proposals/Pril.2. Personalnie dannie expertov NOA.doc">Скачать ...</a>)</li>
    <li>Соглашение о сотрудничестве между экспертом и НОА
    (<a href="/media/uploads/proposals/soglashenie sotrudnichestvo.doc">Скачать ...</a>)
    <br />
    </li>
</ul>
                """ ).save()
                
    models.Page(slug=u'quality',
                title=u'Политика в области качества',
                content="""
                <strong>Наша основная задача: &laquo;Обеспечение
промышленной безопасности опасных производственных объектов&raquo;</strong>
</p><br /><p>
АНО &laquo;ДИЭКС&raquo;:
</p><br /><p>
Аккредитовано в Единой системе в соответствии с ISO/IEС
17024:2003 &laquo;Оценка соответствия. Общие требования к органам, проводящим
сертификацию персонала&raquo; и Руководства IAF GD 24:2009 по применению стандарта ISO/IEC
17024:2003;
</p><br /><p>
Проводит сертификацию физических лиц в соответствии с
ПБ 03-440-02.
</p><br /><p>
Стратегической целью руководства и всего персонала АНО
&laquo;ДИЭКС&raquo; является устойчивое развитие в области обеспечения промышленной
безопасности.
</p><br /><p>
Мы намерены постоянно подтверждать авторитет АНО &laquo;ДИЭКС&raquo;,
как надёжного партнёра, в области предоставления экспертных и сертификационных
услуг с высоким уровнем качества, для российских и зарубежных предприятий с
целью достижения лидирующего конкурентоспособного положения на рынке.
</p><br /><p>
Политика в области качества разработана с учетом
требований:
</p><br /><p>
-
ФЗ &laquo;О
промышленной безопасности опасных производственных объектов&raquo; № 116-ФЗ;
</p><br /><p>
-
Правил
промышленной безопасности и других документов Ростехнадзора;
</p><br /><p>
-
Системы
документов по аккредитации (СДА) ЕС ОС;
</p><br /><p>
-
ISO/IEС 17024:2003;
</p><br /><p>
-
Стандартов ISO серии 17000, Руководства IAF GD 24:2009 по
применению стандарта ISO/IEC 17024:2003, EN
473:2008 &laquo;Квалификация и сертификация персонала неразрушающего контроля.
Основные принципы&raquo;, ISO 9712:2005 &laquo;Неразрушающий
контроль. Квалификация и сертификация персонала неразрушающего контроля&raquo;
</p><br /><p>
-
Стандартов серии
ГОСТ Р ИСО 9000, 19011;
</p><br /><p>
-
Европейских норм
серии EN 45000
</p><br /><p>
Целью политики в области качества
является:
</p><br /><p>
-
обеспечение
строгого соответствия работ и процедур требованиям законодательства РФ,
национальных и (или) международных стандартов, правил и норм Ростехнадзора;
</p><br /><p>
-
создание у
заказчиков полной уверенности в компетентности, независимости и
беспристрастности АНО &laquo;ДИЭКС&raquo;;
</p><br /><p>
-
гарантии в
сохранении необходимого уровня качества при условии выполнения всех процедур согласно
действующим законодательным актам и нормативным документам;
</p><br /><p>
-
совершенствование
деятельности организации с тем, чтобы заказчики рассматривали АНО &laquo;ДИЭКС&raquo; как
эталон надежности и качества;
</p><br /><p>
-
обеспечение
непрерывного функционирования системы качества и реализации ее требований;
</p><br /><p>
-
повышение
экономической эффективности работы АНО &laquo;ДИЭКС&raquo; за счет рационального
использования имеющихся людских, организационных и экономических ресурсов,
планирование качества своих работ и услуг;
</p><br /><p>
-
разработка и
поддержание в действии организационной структуры и выделение ресурсов,
обеспечивающих выполнение политики в области качества.
</p><br /><p>
В процессе выполнения своих функций АНО &laquo;ДИЭКС&raquo;
проводит экспертизу промышленной безопасности, аттестацию (сертификацию)
специалистов и экспертов в соответствии с установленной процедурой, обеспечивает
конфиденциальность информации, полученной в процессе выполнения работ. АНО
&laquo;ДИЭКС&raquo; не осуществляет деятельность, которая снизила бы доверие к его
компетентности, беспристрастности, честности.
</p><br /><p>
Требования и порядок проведения экспертиз, аттестации (сертификации)
и аккредитации являются одинаковыми и справедливыми для всех клиентов.
</p><br /><p>
Политика и процедуры АНО &laquo;ДИЭКС&raquo; позволяют
устанавливать, обеспечивать, возобновлять и сокращать области сертификации, а
также приостанавливать и отменять действие сертификатов.
</p><br /><p>
АНО &laquo;ДИЭКС&raquo; ограничивает свою деятельность по
сертификации областью сертификации на которую она аккредитована в ЕС ОС.
</p><br /><p>
Политика и процедуры АНО &laquo;ДИЭКС&raquo; обеспечивают защиту
конфиденциальности полученной от заказчика информации, компетентность,
беспристрастность и объективность деятельности Организации по оценке
соответствия.
</p><br /><p>
АНО &laquo;ДИЭКС&raquo; имеет процедуру и организационно готова
независимо и беспристрастно рассматривать жалобы и апелляции по сертификации
физических лиц.
</p><br /><p>
Политика в области
качества должна исполняться персоналом АНО &laquo;ДИЭКС&raquo; полно, по всем разделам и
пунктам, согласно установленным функциям, полномочиям и компетентности. С целью
выполнения этого требования Руководство по качеству доступно для использования
персоналом организации.
</p><br /><p>
Руководство АНО
&laquo;ДИЭКС&raquo; берёт на себя всю ответственность за реализацию Политики в области
качества и обязуется постоянно повышать результативность системы менеджмента качества
и просит всех работников поступать так же.
</p>
                """ ).save()