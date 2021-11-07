from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel


class EquipmentPage(Page):
    ''' Страница с информацией о единице оборудования '''

    description = RichTextField(
        blank=True,
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'hr', 'bold', 'italic', 'ol', 'ul', 'link'],
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    subpage_types = []
    parent_page_types = ['equipment.EquipmentIndexPage']

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class EquipmentIndexPage(Page):
    '''Страница для выведения списка всего оборудования'''

    max_count = 1

    subpage_types = ['equipment.EquipmentPage']
    parent_page_types = ['home.HomePage']
