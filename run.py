# -*- coding: utf-8 -*-
# @Time : 2022/1/2 17:51
# @Author : WhaleFall
# @Deco : 项目入口文件
# @File : run.py
# @Software: PyCharm
import os
from app import create_app
import click  # 命令行参数库

# from app.models import User  # 数据库模型
# 从环境变量读取
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


# 设置数据库批处理使其支持sqlite
# migrate = Migrate(app, db, render_as_batch=True)

# @click.command()
# @click.option("--deploy", help="初始化应用")
@app.cli.command()
def deploy():
    """初始化Flask应用运行配置"""
    # with app.app_context():
    #     db.drop_all()  # 删除原有
    #     db.create_all()  # 创建数据库
    #     if not User.query.filter_by(username="admin").first():
    #         """如果没有管理员账号就新建一个"""
    #         user = User(username='admin',
    #                     email='admin@admin.com', password="admin")
    #         db.session.add(user)
    #         db.session.commit()
    click.echo('数据库初始化成功!')
