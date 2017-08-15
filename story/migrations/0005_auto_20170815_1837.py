# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 18:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20170815_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('images', wagtail.wagtailcore.blocks.StructBlock([('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock())], icon='image')), ('gist', wagtail.wagtailcore.blocks.TextBlock(help_text='Go to gist.github.com to write code and copy the embed Link.')), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())]),
        ),
    ]
