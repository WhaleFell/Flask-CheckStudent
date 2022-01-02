# -*- coding: utf-8 -*-
# @Time : 2022/1/3 1:17
# @Author : WhaleFall
# @Site : 
# @File : errors.py
# @Software: PyCharm
# 捕获web的所有异常
from . import main
from flask import render_template, make_response


@main.app_errorhandler(404)
def page_not_found(e):
    """处理404错误"""
    return "404", 404


# @main.app_errorhandler(500)
# def service_error(e):
#     """处理500服务器错误"""
#     return "500", 500
#
#
# @main.app_errorhandler(Exception)
# def unknown_error(e):
#     """处理未知错误"""
#     return f"{e}"
