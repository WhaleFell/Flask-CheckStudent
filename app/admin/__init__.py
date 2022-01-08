# -*- coding: utf-8 -*-
# @Time : 2022/1/8 18:12
# @Author : WhaleFall
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
# 系统后台
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views