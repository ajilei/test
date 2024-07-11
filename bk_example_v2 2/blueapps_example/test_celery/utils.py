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

from blueapps_example.test_celery.constants import TASK
from django_celery_beat.models import PeriodicTask


def get_period_task_detail(task_id):
    """
    @summary: 查询周期任务和相关参数
    @param task_id:  周期任务id
    @return: {
           'task_args': 任务args参数,
           'task_kwargs': 任务kwargs参数,
           'cron_schedule':CrontabSchedule
           }
    """
    #  查询周期任务的信息
    try:
        period_task = PeriodicTask.objects.get(id=task_id)
        task = period_task.task
        task_args = period_task.args
        task_kwargs = period_task.kwargs
        cron_schedule = period_task.crontab  # 周期时间参数
    except Exception:  # pylint: disable=broad-except
        task = TASK
        task_args = "[]"
        task_kwargs = "{}"
        cron_schedule = None
    task_info = {
        "task_id": task_id,
        "task": task,
        "task_args": task_args,
        "task_kwargs": task_kwargs,
        "cron_schedule": cron_schedule,
    }
    return task_info
