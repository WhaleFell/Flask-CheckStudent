# -*- coding: utf-8 -*-
# @Time : 2022/1/3 0:02
# @Author : WhaleFall
# @Site : 
# @File : models.py
# @Software: PyCharm
# 存放 `sqlmodel` 数据库模型
from . import login_manager


# 提供一个 user_loader 回调函数,用于通过 session 中存储的用户 ID 重新加载用户对象。
# 它应该接收用户的 unicode ID,并返回相应的用户对象。
# 如果 ID 无效，函数应该返回 None (而不是唤起异常),
# 这样 ID 将从 session 中被手动移除且程序可以继续执行.
@login_manager.user_loader
def load_user(user_id):
    return None
