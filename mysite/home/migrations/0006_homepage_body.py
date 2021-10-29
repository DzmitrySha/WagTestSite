# Generated by Django 3.2.8 on 2021-10-29 20:55

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211029_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rtfblock', wagtail.core.blocks.RichTextBlock()), ('imgblock', wagtail.images.blocks.ImageChooserBlock()), ('youtubeblock', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
    ]
