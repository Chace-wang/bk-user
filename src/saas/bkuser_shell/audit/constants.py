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
from django.utils.translation import ugettext_lazy as _

# 操作对象展示名
OPERATION_OBJ_NAME_TUPLE = {
    ("DynamicFieldInfo", _("用户字段")),
    ("Profile", _("用户")),
    ("Department", _("组织")),
    ("ProfileCategory", _("用户目录")),
    ("Setting", _("用户目录配置")),
}

OPERATION_OBJ_NAME_MAP = {x[0]: x[1] for x in OPERATION_OBJ_NAME_TUPLE}
OPERATION_OBJ_VALUE_MAP = {x[1]: x[0] for x in OPERATION_OBJ_NAME_TUPLE}

# 操作展示名
OPERATION_NAME_TUPLE = (
    ("create", _("创建")),
    ("update", _("更新")),
    ("delete", _("删除")),
    ("retrieve", _("获取")),
    ("sync", _("同步")),
    ("export", _("导出")),
    ("import", _("导入")),
    ("restoration", _("恢复")),
)

OPERATION_NAME_MAP = {x[0]: x[1] for x in OPERATION_NAME_TUPLE}
OPERATION_VALUE_MAP = {x[1]: x[0] for x in OPERATION_NAME_TUPLE}


LOGIN_FAILED_REASON_TUPLE = (
    ("bad_password", _("密码错误")),
    ("expired_password", _("密码过期")),
    ("too_many_failure", _("密码错误次数过多")),
    ("locked_user", _("用户已锁定")),
    ("disabled_user", _("用户已删除")),
    ("should_change_initial_password", _("需要修改初始密码")),
)
LOGIN_FAILED_REASON_MAP = {x[0]: x[1] for x in LOGIN_FAILED_REASON_TUPLE}
