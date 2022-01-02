# -*- coding: utf-8 -*-
# @Time : 2022/1/3 1:18
# @Author : WhaleFall
# @Site : 
# @File : views.py
# @Software: PyCharm
# 主视图
from . import main

from flask import render_template


@main.route('/')
def index():
    return "Hello Flask"