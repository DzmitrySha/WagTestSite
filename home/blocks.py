# импортируем зависимости StructBlock, CharBlock, ImageChooserBlock
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

# создаем блок для вставки изображения с текстом, наследуем от StructBlock

class FigCaptionBlock(StructBlock):
    # текст
    figure = ImageChooserBlock(label='Картинка')
    # изображение
    caption = CharBlock(label='Описание картинки')

    class Meta:
        # иконка блока
        icon = 'image'
        # шаблон для рендеринга блока mysite/templates/blocks/fig_caption_block.html
        template = 'blocks/fig_caption_block.html'
        # название блока
        label = 'Картинка с текстом'
