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
from bkuser_core.apis.v2.viewset import AdvancedListAPIView, AdvancedModelViewSet

from . import serializers as local_serializers
from .models import GeneralLog, LogIn, ResetPassword


class GeneralLogViewSet(AdvancedModelViewSet, AdvancedListAPIView):
    queryset = GeneralLog.objects.all()
    serializer_class = local_serializers.GeneralLogSerializer
    lookup_field = "id"


class LoginLogViewSet(AdvancedModelViewSet, AdvancedListAPIView):
    queryset = LogIn.objects.all()
    serializer_class = local_serializers.LoginLogSerializer
    lookup_field = "id"


class ResetPasswordLogViewSet(AdvancedModelViewSet, AdvancedListAPIView):
    queryset = ResetPassword.objects.all()
    serializer_class = local_serializers.ResetPasswordLogSerializer
    lookup_field = "id"
