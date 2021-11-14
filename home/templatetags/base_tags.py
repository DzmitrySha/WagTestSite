# Импортируем нашу модель Footer и специальный модуль из джанго
from home.models import Footer
from django import template

from wagtail.core.models import Site

# создаем декоратор
register = template.Library()

# Cоздаем тег футера - функцию которая будет брать параметр context и
# возвращать объект (словарь) footer, содержащий сам запрос request по-умолчанию
# и данные, которые будем использовать в шаблоне -
# - (первую запись из базы данных от модели Footer)
# Украшаем нашу тег footer_tag() декоратором, который будет принимать два параметра
# имя файла шаблона (filename) и контекст (takes_context) устанавливаем в True

@register.inclusion_tag(filename='home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first()
    }

# создаем теги МЕНЮ на основе меню из bakerydemo

# 1. берем тег get_site_root из bakerydemo, c помощью которого
# мы можем получить корневую страницу сайта,
# для этого импортируем также модель Site из wagtail.core.models

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page


# Извлекает пункты верхнего меню - непосредственные дочерние элементы родительской страницы.
# Метод has_menu_children необходим, потому что меню Foundation требует,
# чтобы класс выпадающего списка применялся к родителю.
@register.inclusion_tag(filename='tags/top_menu.html', takes_context=True)
def top_menu(context, parent):
    menuitems = parent.get_children().live().in_menu()
    return {
        'menuitems': menuitems,
        # требуется для тега pageurl, который мы хотим использовать в этом шаблоне
        'request': context['request'],
    }
