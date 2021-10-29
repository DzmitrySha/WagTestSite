from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    # поля в базе данных
    subtitle = models.CharField(max_length=150, blank=True, null=True, verbose_name='Подзаголовок')

    # поля в админке для ввода данных
    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]
