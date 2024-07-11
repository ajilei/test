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
    return render(request, "test_app_tags/index.html")


def cc_app_select(request):
    """
    @summary: 业务选择框（下拉）
    """
    # 获取前端参数，默认宽度为200
    px = request.GET.get("px", 200)
    # 创建调用组件的通用client
    client = get_client_by_request(request)
    # 组件参数
    result = client.cc.search_business({})
    data = result.get("data", {"info": []})
    app_list = [{"id": i["bk_biz_id"], "text": i["bk_biz_name"]} for i in data["info"]]
    width_px = "%spx" % px
    ctx = {
        "app_list": app_list,
        "app_message": result["message"],
        "width_px": width_px,
    }
    return JsonResponse(ctx)
