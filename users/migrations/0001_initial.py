# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0039_collectionviewrestriction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('clubname', models.CharField(choices=[('automobile', 'Automobile'), ('robotics', 'robotics'), ('aeromodelling', 'aeromodelling'), ('electronics', 'electronics'), ('prakriti', 'prakriti'), ('edc', 'EntrepreneurshipDevelopmentCell'), ('fnc', 'FinanceandEconomics'), ('coding', 'CodingClub'), ('astronomy', 'Astronomy'), ('acumen', 'Acumen'), ('radiog', 'RadioG')], max_length=20)),
                ('rollno', models.PositiveIntegerField(default=1)),
                ('phoneno', models.PositiveIntegerField(default=1)),
                ('display_picture', models.ImageField(upload_to=b'')),
                ('birth_date', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(max_length=250)),
                ('clubname', models.CharField(choices=[('automobile', 'Automobile'), ('robotics', 'robotics'), ('aeromodelling', 'aeromodelling'), ('electronics', 'electronics'), ('prakriti', 'prakriti'), ('edc', 'EntrepreneurshipDevelopmentCell'), ('fnc', 'FinanceandEconomics'), ('coding', 'CodingClub'), ('astronomy', 'Astronomy'), ('acumen', 'Acumen'), ('radiog', 'RadioG')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
