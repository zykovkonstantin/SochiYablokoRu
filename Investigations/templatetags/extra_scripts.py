from django import template
from django.utils import timezone
from Investigations.models import BaseForInvestigation

register = template.Library()


@register.filter(name='last_change_time')
def last_change_time(inv):
    last_base = BaseForInvestigation.objects.filter(investigation=inv, published_date__lte=timezone.now()).order_by(
        '-published_date')[:1]
    if last_base:
        last_base_time = last_base.values_list('published_date', flat=True)[0]
        inv.published_date = last_base_time

    return inv.published_date


@register.filter(name='bases_list')
def bases_list(inv):
    return BaseForInvestigation.objects.filter(investigation=inv, published_date__lte=timezone.now()).order_by(
        'published_date')


@register.filter(name='get_status')
def get_status(status):
    status_list = ('Начало расследования', 'Сбор информации', 'Подготовка ответных мер', 'Ожидание результатов',
                   'Анализ полученных результатов', 'Завершено')
    if status == '1':
        return status_list[0]
    elif status == '2':
        return status_list[1]
    elif status == '3':
        return status_list[2]
    elif status == '4':
        return status_list[3]
    elif status == '5':
        return status_list[4]
    elif status == '6':
        return status_list[5]


@register.filter(name='get_type')
def get_type(base_type):
    type_list = ('ИНФОРМАЦИЯ', 'ЖАЛОБА', 'ЗАПРОС', 'ОТВЕТ', 'ИТОГИ')

    if base_type == '1':
        return type_list[0]
    elif base_type == '2':
        return type_list[1]
    elif base_type == '3':
        return type_list[2]
    elif base_type == '4' or base_type == '5':
        return type_list[3]
    elif base_type == '6':
        return type_list[4]
