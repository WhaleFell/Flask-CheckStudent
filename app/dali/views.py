# -*- coding: utf-8 -*-
# @Time : 2022/1/8 16:45
# @Author : WhaleFall
# @Site : 
# @File : view.py
# @Software: PyCharm
# 大沥高中查人 视图
from . import dali
# from app import models  # 导入模块
from flask import render_template


@dali.route('/dali/')
def dali_index():
    return render_template('dali/index.html')
