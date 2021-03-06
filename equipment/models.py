from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
# импортируем админ-панели wagtail
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


# создаем класс EquipmentImage для сортировки оборудования
class EquipmentImage(Orderable):
    """ Изображение оборудования """
    # параметры сниппета
    caption = models.CharField(max_length=200, verbose_name="Текст слайда")
    figure = models.ForeignKey('wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Картинка')

    # параметр для установки связей со страницей в базе данных
    equipment = ParentalKey(
        'equipment.EquipmentPage',
        on_delete=models.CASCADE,
        related_name='slides')

    panels = [
        FieldPanel('caption'),
        ImageChooserPanel('figure'),
    ]


# создаем класс EquipmentOperator для создания сниппета
class EquipmentOperator(models.Model):
    """ Оператор оборудования (сниппет) """

    # параметры сниппета имя и имейл
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()

    # параметр для установки связей сниппета со страницей в базе данных
    equipment = ParentalKey(
        'equipment.EquipmentPage',
        on_delete=models.CASCADE,
        related_name='operators')


class EquipmentPage(Page):
    """ Страница с информацией о единице оборудования """

    description = RichTextField(
        blank=True,
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'hr', 'bold', 'italic', 'ol', 'ul', 'link'],
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        # добавляем возможность добавления поля EquipmentOperator на страницу в панель админки
        # используем related_name нашего сниппета EquipmentOperator и специальную панель InlinePanel
        MultiFieldPanel(
            [InlinePanel('slides', label="слайд")],
            heading="Слайды"
        ),
        # добавляем возможность добавления поля EquipmentImage на страницу в панель админки
        # используем related_name нашего сниппета EquipmentImage и специальную панель InlinePanel
        MultiFieldPanel(
            [InlinePanel('operators', label="оператора")],
            heading="Операторы"
        ),
    ]

    subpage_types = []
    parent_page_types = ['equipment.EquipmentIndexPage']

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class EquipmentIndexPage(Page):
    """ Страница для выведения списка всего оборудования """

    max_count = 1

    subpage_types = ['equipment.EquipmentPage']
    parent_page_types = ['home.HomePage']
