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

import datetime
import json

from blueapps_example.test_celery.constants import TASK
from blueapps_example.test_celery.models import PeriodTaskRecord, TimingTaskRecord
from celery import task
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

from blueapps.utils.logger import logger


@task()
def send_msg(record_id, **kwargs):
    """
    @summary: 改变消息记录内容和状态
    """
    try:
        message = kwargs.get("message")
        schedule_time = kwargs.get("schedule_time")
        record = TimingTaskRecord.objects.get(id=record_id)
        if schedule_time:
            content = u"定时时间：{}\n消息：{}".format(schedule_time, message)
        else:
            content = u"消息：%s" % message
        record.content = content
        record.execute_time = timezone.make_aware(datetime.datetime.now())
        record.is_executed = 1
        record.save()
        res = True
    except Exception as err:  # pylint: disable=broad-except
        logger.error(u"执行（定时）后台任务出错：%s" % err)
        res = False
    return res


@task()
# @periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def add(first_num, second_num):
    """
    @summary: celery 示例任务
    @note: @periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))：每5分钟执行1次任务
              periodic_task 装饰器程序运行时自定触发定时任务
    """
    sums = first_num + second_num
    # 以下操作是保存任务的执行记录
    # 查询任务的对应的周期任务
    try:
        task = TASK
        args = [first_num, second_num]
        args = json.dumps(args)
        periodic_task = PeriodicTask.objects.filter(task=task, args=args)[0]
        periodic_task_id = periodic_task.id
    except Exception:  # pylint: disable=broad-except
        logger.error(u"查询任务的对应的周期任务出错")
        periodic_task_id = 0
    # 将执行记录保存到数据库中
    try:
        execute_param = "first_num:{}, second_num:{}".format(first_num, second_num)
        PeriodTaskRecord.objects.create(
            execute_param=execute_param,
            execute_result=sums,
            periodic_task_id=periodic_task_id,
        )
    except Exception:  # pylint: disable=broad-except
        logger.error(u"保存周期性任务执行记录出错")
    return sums
