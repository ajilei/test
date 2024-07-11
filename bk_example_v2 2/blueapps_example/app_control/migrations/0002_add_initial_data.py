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

from __future__ import unicode_literals

from django.core import serializers
from django.db import migrations


def initial_app_control_data(apps, schema_editor):
    try:
        # 初始化功能开关数据
        func_data = [
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "func_test", "func_name": "示例功能"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "create_task", "func_name": "创建任务"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "execute_task", "func_name": "执行任务"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "tasks", "func_name": "任务列表"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "task", "func_name": "任务详情"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "pause_task", "func_name": "任务暂停"},
            },
            {
                "model": "app_control.FunctionController",
                "fields": {"func_code": "terminate_task", "func_name": "任务终止"},
            },
        ]
        func_obj = serializers.deserialize("python", func_data, ignorenonexistent=True)
        for obj in func_obj:
            obj.save()
    except Exception:  # pylint: disable=broad-except
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("app_control", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(initial_app_control_data),
    ]
