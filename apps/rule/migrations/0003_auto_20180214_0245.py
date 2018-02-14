# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-14 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0002_auto_20180213_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_type',
            field=models.CharField(choices=[('SEC', '절'), ('SUPPL', '부칙'), ('CHAP', '장'), ('PRE', '전문')], max_length=8, verbose_name='종류'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule_type',
            field=models.CharField(choices=[('BYLAW', '세칙'), ('ETC', '기타규정'), ('CONST', '회칙'), ('RULE', '규칙')], max_length=8, verbose_name='종류'),
        ),
    ]