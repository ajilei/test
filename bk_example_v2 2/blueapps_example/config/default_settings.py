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

import importlib

from django.conf import settings
from django.utils.translation import gettext_lazy as _

ver_settings = importlib.import_module(
    "blueapps_example.config.sites.%s.ver_settings" % settings.RUN_VER
)

for _setting in dir(ver_settings):
    if _setting.upper() == _setting:
        locals()[_setting] = getattr(ver_settings, _setting)

# 常量定义 英文字符 转换为 中文名称
CC_ROLES = [
    (ver_settings.CC_MAINTAINERS_ROLE, _(u"运维人员")),
    (ver_settings.CC_PRODUCTPM_ROLE, _(u"产品人员")),
    (ver_settings.CC_DEVELOPER_ROLE, _(u"开发人员")),
    (ver_settings.CC_TESTER_ROLE, _(u"测试人员")),
]
