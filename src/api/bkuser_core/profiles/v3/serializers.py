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
from bkuser_core.apis.v3.serializers import StringArrayField
from bkuser_core.departments.serializers import SimpleDepartmentSerializer
from bkuser_core.profiles.v2.serializers import LeaderSerializer
from rest_framework.fields import BooleanField, CharField, IntegerField, JSONField
from rest_framework.serializers import Serializer


class ProfileSerializer(Serializer):
    """列出用户的 profile"""

    id = CharField(required=False, help_text="用户ID")
    username = CharField(required=False, help_text="用户名")
    qq = CharField(required=False, help_text="QQ")
    email = CharField(required=False, help_text="邮箱")
    telephone = CharField(required=False, help_text="电话")
    wx_userid = CharField(required=False, help_text="微信用户id")
    domain = CharField(required=False, help_text="域")
    display_name = CharField(required=False, help_text="中文名")
    status = CharField(required=False, help_text="账户状态")
    staff_status = CharField(required=False, help_text="在职状态")
    position = CharField(required=False, help_text="职位")
    enabled = BooleanField(required=False, help_text="是否启用", default=True)
    extras = JSONField(required=False, help_text="扩展字段")


# ------------
# Request
# ------------
class QueryProfileSerializer(ProfileSerializer):
    ordering = CharField(required=False, help_text="排序字段", default="id")
    cursor = CharField(required=False, help_text="游标")
    # 暂不支持 fields 限制返回字段
    # fields = StringArrayField(required=False, help_text="返回字段")
    departments = StringArrayField(required=False, help_text="部门id列表")
    leaders = StringArrayField(required=False, help_text="上级id列表")

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        if "leaders" in data:
            data["leader"] = data.pop("leaders")

        return data


# ------------
# Response
# ------------
class ResultProfileSerializer(ProfileSerializer):
    """返回用户 profile"""

    departments = SimpleDepartmentSerializer(many=True, required=False, help_text="部门列表")
    leaders = LeaderSerializer(many=True, required=False, help_text="上级列表", source="leader")


class PaginatedProfileSerializer(Serializer):
    count = IntegerField(required=False, help_text="总数")
    next = CharField(required=False, help_text="下一页游标")
    previous = CharField(required=False, help_text="上一页游标")
    results = ResultProfileSerializer(many=True, help_text="结果")
