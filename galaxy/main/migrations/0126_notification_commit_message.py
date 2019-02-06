# -*- coding: utf-8 -*-
# Generated by Django 2.1.5 on 2019-01-31 18:31

from django.db import migrations
import galaxy.main.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0125_community_score_question_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='commit_message',
            field=galaxy.main.fields.TruncatingCharField(
                blank=True,
                default='',
                max_length=256),
        ),
    ]
