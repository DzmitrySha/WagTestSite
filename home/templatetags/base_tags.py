# Импортируем нашу модель Footer и специальный модуль из джанго
from home.models import Footer
from django import template

# создаем декоратор
register = template.Library()

# Cоздаем тег, функцию которая будет брать параметр context и
# возвращать объект (словарь) footer, содержащий сам запрос request по-умолчанию и
# данные, которые будем использовать в шаблоне -
# - (первую запись из базы данных от модели Footer)
# Украшаем нашу тег footer_tag() декоратором, который будет принимать два параметра
# имя файла шаблона (filename) и контекст (takes_context) устанавливаем в True

@register.inclusion_tag(filename='home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first()
    }
