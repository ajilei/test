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
from django.utils import timezone
from django_celery_beat.models import CrontabSchedule, PeriodicTask


"""
celery 周期任务封装
"""


def add_period_task(
    task,
    name=None,
    minute="*",
    hour="*",
    day_of_week="*",
    day_of_month="*",
    month_of_year="*",
    args="[]",
    kwargs="{}",
    tz=None,  # pylint: disable=invalid-name
):
    """
    @summary: 添加一个周期任务
    @param task: 该task任务的模块路径名, 例如celery_sample.crontab_task
    @param name: 用户定义的任务名称, 具有唯一性
    @note: PeriodicTask有很多参数可以设置，这里只提供简单常用的
    """
    cron_param = {
        "minute": minute,
        "hour": hour,
        "day_of_week": day_of_week,
        "day_of_month": day_of_month,
        "month_of_year": month_of_year,
        "timezone": timezone.get_current_timezone() if tz is None else tz,
    }
    if not name:
        name = task
    try:
        cron_schedule = CrontabSchedule.objects.get(**cron_param)
    except CrontabSchedule.DoesNotExist:
        cron_schedule = CrontabSchedule(**cron_param)
        cron_schedule.save()
    try:
        PeriodicTask.objects.create(
            name=name,
            task=task,
            crontab=cron_schedule,
            args=args,
            kwargs=kwargs,
        )
    except Exception as err:  # pylint: disable=broad-except
        return False, "%s" % err
    else:
        return True, ""


def edit_period_task_by_name(
    name,
    minute="*",
    hour="*",
    day_of_week="*",
    day_of_month="*",
    month_of_year="*",
    args="[]",
    kwargs="{}",
):
    """
    @summary: 更新一个周期任务
    @param name: 用户定义的任务名称, 具有唯一性
    """
    try:
        period_task = PeriodicTask.objects.get(name=name)
    except PeriodicTask.DoesNotExist:
        return False, "PeriodicTask.DoesNotExist"
    cron_param = {
        "minute": minute,
        "hour": hour,
        "day_of_week": day_of_week,
        "day_of_month": day_of_month,
        "month_of_year": month_of_year,
    }
    try:
        cron_schedule = CrontabSchedule.objects.get(**cron_param)
    except CrontabSchedule.DoesNotExist:
        cron_schedule = CrontabSchedule(**cron_param)
        cron_schedule.save()
    period_task.crontab = cron_schedule
    period_task.args = args
    period_task.kwargs = kwargs
    period_task.save()
    return True, ""


def edit_period_task_by_id(
    task_id,
    minute="*",
    hour="*",
    day_of_week="*",
    day_of_month="*",
    month_of_year="*",
    args="[]",
    kwargs="{}",
):
    """
    @summary: 更新一个周期任务
    @param name: 用户定义的任务名称, 具有唯一性
    """
    try:
        period_task = PeriodicTask.objects.get(id=task_id)
    except PeriodicTask.DoesNotExist:
        return False, "PeriodicTask.DoesNotExist"
    cron_param = {
        "minute": minute,
        "hour": hour,
        "day_of_week": day_of_week,
        "day_of_month": day_of_month,
        "month_of_year": month_of_year,
    }
    try:
        cron_schedule = CrontabSchedule.objects.get(**cron_param)
    except CrontabSchedule.DoesNotExist:
        cron_schedule = CrontabSchedule(**cron_param)
        cron_schedule.save()
    period_task.crontab = cron_schedule
    period_task.args = args
    period_task.kwargs = kwargs
    period_task.save()
    return True, ""


def del_period_task_by_name(name):
    """
    @summary: 根据周期任务的name删除该任务
    @param name: 用户定义的任务名称, 具有唯一性
    """
    try:
        PeriodicTask.objects.filter(name=name).delete()
        return True, ""
    except Exception as err:  # pylint: disable=broad-except
        return False, "%s" % err


def del_period_task_by_id(task_id):
    """
    @summary: 根据周期任务的id删除该任务
    @param task_id: PeriodicTask库中记录的id
    """
    try:
        PeriodicTask.objects.filter(id=task_id).delete()
        return True, ""
    except Exception as err:  # pylint: disable=broad-except
        return False, "%s" % err
