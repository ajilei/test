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

from django.conf.urls import include, url

urlpatterns = [
    # 应用功能开关控制
    url(r"^app_control/", include("blueapps_example.app_control.urls")),
    # 组件样例
    url(r"^test_component/", include("blueapps_example.test_component.urls")),
    # 后台任务样例
    url(r"^test_celery/", include("blueapps_example.test_celery.urls")),
    # 通用Tags/ajax异步请求样例
    url(r"^test_app_tags/", include("blueapps_example.test_app_tags.urls")),
]
