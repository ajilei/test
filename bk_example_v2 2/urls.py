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
from django.contrib import admin

"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

urlpatterns = [
    # Django后台数据库管理
    url(r"^admin/", admin.site.urls),
    # 用户登录鉴权--请勿修改
    url(r"^account/", include("blueapps.account.urls")),
    # 在home_application(根应用)里开发你的应用的主要功能
    url(r"^", include("home_application.urls")),
    # 如果你习惯使用 mako 模板，可在mako_application开发你的应用的主要功能
    url(r"^mako/", include("mako_application.urls")),
    # 样例功能
    url(r"^example/", include("blueapps_example.urls")),
    url(r"^i18n/", include("django.conf.urls.i18n")),
]


# 添加版本日志功能
try:
    import version_log.config as config
    
    urlpatterns += [
        url(r'^{}'.format(config.ENTRANCE_URL), include('version_log.urls')),
    ]
except ImportError:
    pass

