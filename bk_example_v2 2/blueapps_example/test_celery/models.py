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

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimingTaskRecord(models.Model):
    """
    定时任务执行记录
    """

    username = models.CharField(_(u"用户"), max_length=64)
    title = models.TextField(_(u"消息标题"), blank=True, null=True)
    content = models.TextField(_(u"消息内容"), blank=True, null=True)
    create_time = models.DateTimeField(_(u"任务创建时间"), blank=True, null=True)
    execute_time = models.DateTimeField(_(u"执行时间"), blank=True, null=True)
    is_executed = models.IntegerField(_(u"是否执行"), default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"定时任务执行记录")
        verbose_name_plural = _(u"定时任务执行记录")


class PeriodTaskRecord(models.Model):
    """
    周期任务纪录
    """

    execute_param = models.TextField(_(u"任务执行参数"))
    execute_result = models.TextField(_(u"任务执行结果"))
    execute_time = models.DateTimeField(_(u"任务执行时间"), auto_now_add=True)
    periodic_task_id = models.IntegerField(_(u"周期性任务的id"), default=0)

    def __unicode__(self):
        return "{}--{}--{}".format(
            self.periodic_task_id, self.execute_param, self.execute_time
        )

    class Meta:
        verbose_name = _(u"周期性任务执行记录")
        verbose_name_plural = _(u"周期性任务执行记录")
        ordering = ["-execute_time"]
