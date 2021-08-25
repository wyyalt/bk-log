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
"""
from apps.log_databus.constants import EtlConfig
from apps.log_databus.handlers.etl_storage import EtlStorage


class BkLogTextEtlStorage(EtlStorage):
    """
    直接入库
    """

    etl_config = EtlConfig.BK_LOG_TEXT

    def etl_preview(self, data, etl_params) -> list:
        """
        字段提取预览
        :param data: 日志原文
        :param etl_params: 字段提取参数
        :return: 字段列表 list
        """
        return data

    def get_result_table_config(self, fields, etl_params, built_in_config, es_version="5.X"):
        """
        配置清洗入库策略，需兼容新增、编辑
        """
        built_in_fields = built_in_config.get("fields", [])
        return {
            "option": built_in_config.get("option", {}),
            "field_list": built_in_fields
            + [built_in_config["time_field"]]
            + [
                {
                    "field_name": "log",
                    "field_type": "string",
                    "tag": "metric",
                    "alias_name": "data",
                    "description": "original_text",
                    "option": {"es_type": "text", "es_include_in_all": True}
                    if es_version.startswith("5.")
                    else {"es_type": "text"},
                }
            ],
            "time_alias_name": built_in_config["time_field"]["alias_name"],
            "time_option": built_in_config["time_field"]["option"],
        }
