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

from blueapps_example.app_control.models import FunctionController
from django.utils.translation import gettext_lazy


def func_check(func_code):
    """
    @summary: 检查功能是否开放
    @param func_code: 功能ID
    @return (1/2/3, message)
            #如下 (0, 功能未开启)
                  (1, 功能已开启)
    """
    _, enabled = FunctionController.objects.func_check(func_code)
    return enabled, gettext_lazy(u"功能已开启") if enabled else gettext_lazy(u"功能未开启")
