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

from blueapps_example.test_celery import views
from django.conf.urls import url

urlpatterns = (
    # 'test_celery.views',
    # 普通任务也没
    url(r"^$", views.index),
    # 执行普通任务
    url(r"^execute_general_task/$", views.execute_general_task),
    # 轮询普通任务执行结果
    url(r"^poll_general_task_status/$", views.poll_general_task_status),
    # 周期任务页面
    url(r"^periodic_task/$", views.periodic_task),
    # 周期任务列表
    url(r"^periodic_task_list/$", views.periodic_task_list),
    # 新增或编辑周期任务
    url(r"^periodic_task_edit/(?P<task_id>\d+)/", views.periodic_task_edit),
    # 检查周期任务配置正确性
    url(r"^check_period_task/$", views.check_period_task),
    # 保存周期任务配置
    url(r"^save_task/$", views.save_task),
    # 删除周期任务
    url(r"^del_period_task/$", views.del_period_task),
    # 周期任务 执行记录
    url(r"^periodic_task_record/(?P<task_id>\d+)/$", views.periodic_task_record),
    url(
        r"^get_periodic_task_records/(?P<periodic_task_id>\d+)/$",
        views.get_periodic_task_records,
    ),
)
