# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

# Generated by Django 1.11.23 on 2019-08-06 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("test_celery", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="PeroidTaskRecord", new_name="PeriodTaskRecord"),
        migrations.AlterModelOptions(name="periodtaskrecord",
                                     options={
                                         "ordering": ["-execute_time"],
                                         "verbose_name": "周期性任务执行记录",
                                         "verbose_name_plural": "周期性任务执行记录",
                                     }),
        migrations.RenameField(model_name="periodtaskrecord", old_name="excute_param", new_name="execute_param"),
        migrations.RenameField(model_name="periodtaskrecord", old_name="excute_result", new_name="execute_result"),
        migrations.RenameField(model_name="periodtaskrecord", old_name="excute_time", new_name="execute_time"),
        migrations.RenameField(model_name="timingtaskrecord", old_name="excute_time", new_name="execute_time"),
        migrations.RenameField(model_name="timingtaskrecord", old_name="is_excuted", new_name="is_executed"),
    ]