# -*- coding: utf-8 -*-
# @Time : 2022/1/2 17:50
# @Author : WhaleFall
# @Site : 
# @File : config.py
# @Software: PyCharm
# 项目主配置
import os
import platform
from datetime import timedelta
from pathlib import Path
from sqlmodel import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))  # 项目的绝对目录


class Config(object):
    """主配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lovehyy123456hjl'  # 密钥
    # SQLALCHEMY_TRACK_MODIFICATIONS = False  # 数据库
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置 session 的过期时间.
    BASEDIR = basedir  # 项目目录
    FLASK_DEBUG = True  # 调试模式
    # 判断操作系统拼接数据库路径
    if platform.system() == "Windows":
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'data.db')
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'db', 'data.db')

    @staticmethod
    def init_app(app):
        """静态方法,用于其他组件初始化"""
        Path.mkdir(Path(basedir, 'db'), exist_ok=True)  # 新建数据库文件夹
        from dotenv import load_dotenv
        load_dotenv()  # 从 .env 文件加载环境变量


class DevelopmentConfig(Config):
    """开发环境,继承于Config主配置"""
    FLASK_DEBUG = True
    # 判断操作系统
    if platform.system() == "Windows":
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'data.db')
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'db', 'data.db')


# 开发环境选择字典
config = {
    "default": Config,
    "development": DevelopmentConfig,
}
