# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-用户管理(Bk-User) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging
import re

from bkuser_shell.account.components.bk_token.forms import AuthenticationForm
from bkuser_shell.account.conf import ConfFixture
from bkuser_shell.account.handlers.response import ResponseHandler
from django.conf import settings
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view, args, kwargs):
        """
        Log into PaaS via two ways
        1. views decorated with 'login_exempt' keyword
        2. User has logged in calling auth.login
        """
        if hasattr(request, "is_wechat") and request.is_wechat():
            return None

        if hasattr(request, "is_bk_jwt") and request.is_bk_jwt():
            return None

        if getattr(view, "login_exempt", False):
            return None

        for white_url in settings.LOGIN_EXEMPT_WHITE_LIST:
            if re.search(white_url, request.path):
                logger.info("%s path in white_url<%s>, exempting login", request.path, white_url)
                return None

        form = AuthenticationForm(request.COOKIES)
        if form.is_valid():
            bk_token = form.cleaned_data[settings.TOKEN_COOKIE_NAME]
            user = auth.authenticate(request=request, bk_token=bk_token)
            if user:
                # Succeed to log in, recall self to exit process
                if user.username != request.user.username:
                    auth.login(request, user)
                return None

        handler = ResponseHandler(ConfFixture, settings)
        if request.is_ajax():
            return handler.build_401_response(request)

        return handler.build_302_response(request)

    def process_response(self, request, response):
        return response
