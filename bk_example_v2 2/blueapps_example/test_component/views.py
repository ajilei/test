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

from blueking.component.shortcuts import get_client_by_request
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    """
    组件样例页面
    """
    return render(request, "test_component/index.html")


def app_list(request):
    """
    获取业务
    """
    # 默认从django settings中获取APP认证信息：应用ID和应用TOKEN
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 组件参数
    kwargs = {}
    result = client.cc.search_business(kwargs)
    if result["result"] is False:
        result["data"] = []
    else:
        result["data"] = [
            {
                "ApplicationID": i["bk_biz_id"],
                "ApplicationName": i["bk_biz_name"],
                "Creator": i["bk_biz_productor"],
                "Maintainers": i["bk_biz_maintainer"],
                "ProductPm": i["operator"],
            }
            for i in result["data"]["info"]
        ]
    return JsonResponse(result)
