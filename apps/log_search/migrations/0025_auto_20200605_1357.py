# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
License for BK-LOG 蓝鲸日志平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
We undertake not to change the open source license (MIT license) applicable to the current version of
the project delivered to anyone in the future.
"""
# Generated by Django 1.11.23 on 2020-06-05 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("log_search", "0024_logindexset_fields_snapshot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesssourceconfig",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="accesssourceconfig",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="logindexset",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="logindexset",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="logindexsetdata",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="logindexsetdata",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="projectinfo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="projectinfo",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="resourcechange",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="resourcechange",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="userindexsetconfig",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="userindexsetconfig",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="userindexsetsearchhistory",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="userindexsetsearchhistory",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间"),
        ),
    ]
