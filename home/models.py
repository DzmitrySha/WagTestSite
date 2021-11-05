from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from .blocks import FigCaptionBlock

from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(models.Model):
    bodytext = RichTextField(
        blank=True, null=True,
        verbose_name='Текст подвала сайта'
    )
    # поля в админке для ввода данных для
    panels = [
        FieldPanel('bodytext')
    ]

    class Meta:
        verbose_name = "Подвал сайта"
        verbose_name_plural = "Подвалы сайта"

    # магическая функция для правильного отображения названия
    def __str__(self):
        return "Подвал сайта"


class NewsPage(Page):
    # задаем название шаблона вручную (по-умолчанию подхватывается шаблон 'home/news_page.html' написанный в camel-case)
    template = 'home/newspage.html'
    # поля в базе данных
    pass


class HomePage(Page):

    subpage_types = ['home.NewsPage']
    # parent_subpage_types = []

    # поля в базе данных
    subtitle = models.CharField(
        blank=True, null=True,
        max_length=150,
        verbose_name='Подзаголовок'
    )
    rtf_body = RichTextField(
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic'],
        blank=True, null=True,
        verbose_name='Основной текст'
    )
    bg_image = models.ForeignKey(
        to='wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Фоновая картинка'
    )

    body = StreamField([
        ('figcaptureblock', FigCaptionBlock()),
        ('rtfblock', RichTextBlock(
            features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'ol', 'ul'],
            label='Текст',
            help_text='Введите ваш текст')),
        ('imgblock', ImageChooserBlock(
            label='Изображение',
            help_text='Добавьте изображение',
            template='blocks/imgblock.html')),
        ('youtubeblock', EmbedBlock(
            label='Видео',
            help_text='Встаьте ссылку на видео с Youtube',
            icon='link')),
    ],
        block_counts={
            'rtfblock': {'min_num': 1},
            'imgblock': {'max_num': 3},
        },
        blank=True,
        verbose_name='Создание и редактирование статьи',
        help_text='Добавляйте и редактируйте необходимые блоки - текст, изображения, видео...'
    )

    # поля в админке для ввода данных
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        RichTextFieldPanel('rtf_body'),
        ImageChooserPanel('bg_image'),
        StreamFieldPanel('body'),
    ]
