# -*- coding: utf-8 -*-
# @Time : 2022/1/3 1:16
# @Author : WhaleFall
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
# 主蓝图 集中处理异常
from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors, views
