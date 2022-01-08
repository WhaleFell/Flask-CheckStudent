# -*- coding: utf-8 -*-
# @Time : 2022/1/3 0:02
# @Author : WhaleFall
# @Site : 
# @File : models.py
# @Software: PyCharm
# 存放 `sqlmodel` 数据库模型
from . import login_manager
from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


# 提供一个 user_loader 回调函数,用于通过 session 中存储的用户 ID 重新加载用户对象。
# 它应该接收用户的 unicode ID,并返回相应的用户对象。
# 如果 ID 无效，函数应该返回 None (而不是唤起异常),
# 这样 ID 将从 session 中被手动移除且程序可以继续执行.
@login_manager.user_loader
def load_user(user_id):
    return None


class User(SQLModel, table=True):
    """用户类"""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    reg_time: datetime = datetime.now()

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
