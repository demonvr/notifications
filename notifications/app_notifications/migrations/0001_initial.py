# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-23 08:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_at', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440. \u0413\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438.', primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='\u0442\u0435\u043c\u0430')),
                ('start_at', models.DateTimeField(verbose_name='\u0434\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u0442\u0430\u0440\u0442\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438')),
                ('end_at', models.DateTimeField(verbose_name='\u0434\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438')),
            ],
            options={
                'ordering': ('-start_at',),
                'verbose_name': '\u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0430',
                'verbose_name_plural': '\u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='MailingTemplates',
            fields=[
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_at', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440. \u0413\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438.', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438', max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': '\u0448\u0430\u0431\u043b\u043e\u043d \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438',
                'verbose_name_plural': '\u0448\u0430\u0431\u043b\u043e\u043d\u044b \u0440\u0430\u0441\u0441\u044b\u043b\u043e\u043a',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_at', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440. \u0413\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438.', primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Create', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043e'), ('Processing', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0432 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), ('Complete', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e'), ('Repeat', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e\u0439 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438'), ('Expired', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043d\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e, \u0438\u0437-\u0437\u0430 \u0438\u0441\u0442\u0435\u043a\u0448\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'), ('Opened', '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u043e')], default='Create', max_length=20, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('send_at', models.DateTimeField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_notifications.Mailing')),
            ],
            options={
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('created_at', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated_at', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440. \u0413\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438.', primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='\u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430')),
                ('first_name', models.CharField(max_length=30, verbose_name='\u0438\u043c\u044f')),
                ('last_name', models.CharField(max_length=30, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('birthday', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
                'verbose_name': '\u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a',
                'verbose_name_plural': '\u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='subscribers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_notifications.Subscribers'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='messages',
            field=models.ManyToManyField(through='app_notifications.Message', to='app_notifications.Subscribers', verbose_name='\u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mailing_templates', to='app_notifications.MailingTemplates', verbose_name='\u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0430'),
        ),
    ]
