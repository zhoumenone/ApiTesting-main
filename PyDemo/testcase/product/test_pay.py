# -*- coding:utf-8 -*-
# @Time    : 2023/4/19
# @Author  : zhoumen
# @File    : test_pay.py
# ****************************
import os
# 操作文件和目录的模块
import allure
# 测试报告生成工具
import pytest
# 测试框架
from comm.utils import get_case
# 导入自定义模块中的函数
from comm.unit.initializePremise import init_premise
# 导入自定义模块中的函数
from comm.unit.apiSend import send_request
# 导入自定义模块中的函数
from comm.unit.checkResult import check_result
# 导入自定义模块中的函数
case_path, case_data = get_case(os.path.realpath(__file__))
@allure.feature(case_data["test_info"]["title"])
class TestProduct:

    @pytest.mark.parametrize("test_case", case_data["test_case"])
    @allure.story("test_pay")
    def test_pay(self, test_case):
        # 初始化请求：执行前置接口+替换关联变量
        test_info, test_case = init_premise(case_data["test_info"], test_case, case_path)
        # 发送当前接口
        code, data = send_request(test_info, test_case)
        # 校验接口返回
        check_result(test_case, code, data)
