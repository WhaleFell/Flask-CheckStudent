# -*- coding: utf-8 -*-
# @Time : 2022/1/8 16:44
# @Author : WhaleFall
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
# 大沥高中查人蓝图 集中处理异常
from flask import Blueprint

dali = Blueprint('dali', __name__)

from . import views