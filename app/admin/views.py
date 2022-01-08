# -*- coding: utf-8 -*-
# @Time : 2022/1/8 16:45
# @Author : WhaleFall
# @Site : 
# @File : view.py
# @Software: PyCharm
# 系统后台 视图
from . import admin
# from app import models  # 导入模块
from flask import render_template

@admin.route('/admin/')
def admin_index():
    return render_template('admin/login.html')
