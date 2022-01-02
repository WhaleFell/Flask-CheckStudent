# -*- coding: utf-8 -*-
# @Time : 2022/1/2 17:50
# @Author : WhaleFall
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
# Flask 应用初始化,工厂函数
from flask import Flask
from flask_login import LoginManager
from config import config

# 实例化一个登录组件
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # 登录的蓝图


def create_app(config_name):
    """
    工厂函数,指定一个配置类型
    程序入口文件千万不能和 `app` 重名,惨痛教训!!
    """
    app = Flask(__name__)  # 实例化
    app.config.from_object(config[config_name])  # 从配置类读取配置
    config[config_name].init_app(app)  # 调用静态方法初始化组件

    # 注册组件
    login_manager.init_app(app)  # 登录组件
    # db.init_app(app)
    # pagedown.init_app(app)
    # moment.init_app(app)

    # 注册蓝图
    from .main import main
    app.register_blueprint(main)

    return app
