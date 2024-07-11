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

from blueapps_example.app_control.decorators import function_check
from blueapps_example.app_control.models import FunctionController
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from blueapps.account.decorators import login_exempt


def home(request):
    """
    首页
    """
    _, is_enabled = FunctionController.objects.func_check("func_test")
    return render(request, "app_control/home.html", {"is_enabled": is_enabled})


def switch_func(request):
    """
    功能开关选择
    """
    status = int(request.POST.get("status", 0))
    # 更改功能开关的状态
    FunctionController.objects.update_func_status("func_test", status)
    return JsonResponse({"result": True})


@function_check("func_test")
def execute_func(request):
    """
    执行测试功能
    """
    return JsonResponse({"result": True, "message": _(u"这是一个功能开发样例")})


@login_exempt
def check_failed(request):
    """
    功能开关检查失败
    """
    return render(request, "app_control/func_check_failed.html")


def verify_code(request):
    """验证码后端验证"""
    code = request.POST.get("bk_verify_code")
    check = request.user.verify_code(code)
    if not check:
        # 验证码不正确或过期
        ret = {"result": False, "message": _(u"短信验证码错误，二步验证失败")}
        return JsonResponse(ret)

    return JsonResponse({"result": True, "message": _(u"二步验证通过")})
