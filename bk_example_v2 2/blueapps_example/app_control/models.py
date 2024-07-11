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
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from blueapps.utils.logger import logger


class FunctionManager(models.Manager):
    def func_check(self, func_code):
        """
        @summary: 检查改功能是否开放
        @param func_code: 功能ID
        @return: (True/False, 'message')
        """
        try:
            enabled = self.get(func_code=func_code).enabled
            return True, int(enabled)
        except Exception as err:  # pylint: disable=broad-except
            logger.error(u"检查改功能是否开放发生异常，错误信息：%s" % err)
            return False, 0

    def update_func_status(self, func_code, status):
        """
        更新功能开关的状态
        """
        self.filter(func_code=func_code).update(enabled=status)
        return True, ""


class FunctionController(models.Model):
    """
    功能开启控制器
    """

    func_code = models.CharField(_(u"功能code"), max_length=64, unique=True)
    func_name = models.CharField(_(u"功能名称"), max_length=64)
    enabled = models.BooleanField(
        _(u"是否开启该功能"), help_text=_(u"控制功能是否对外开放，若选择，则该功能将对外开放"), default=False
    )
    create_time = models.DateTimeField(_(u"创建时间"), default=timezone.now)
    func_developer = models.TextField(
        _(u"功能开发者"), help_text=_(u"多个开发者以分号分隔"), null=True, blank=True
    )
    objects = FunctionManager()

    def __unicode__(self):
        return self.func_name

    class Meta:
        app_label = "app_control"
        verbose_name = _(u"功能控制器")
        verbose_name_plural = _(u"功能控制器")
