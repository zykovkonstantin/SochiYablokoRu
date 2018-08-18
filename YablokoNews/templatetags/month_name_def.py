from django import template

register = template.Library()


@register.filter(name='month_name')
def month_name(number):
    if int(number) == 1:
        return 'Января'
    elif int(number) == 2:
        return 'Февраля'
    elif int(number) == 3:
        return 'Марта'
    elif int(number) == 4:
        return 'Апреля'
    elif int(number) == 5:
        return 'Мая'
    elif int(number) == 6:
        return 'Июня'
    elif int(number) == 7:
        return 'Июля'
    elif int(number) == 8:
        return 'Августа'
    elif int(number) == 9:
        return 'Сентября'
    elif int(number) == 10:
        return 'Октября'
    elif int(number) == 11:
        return 'Ноября'
    elif int(number) == 12:
        return 'Декабря'
