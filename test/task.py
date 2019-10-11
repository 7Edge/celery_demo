#! /usr/bin/env python
# coding:utf-8

import time
from celery import Celery

# app = Celery(__name__, broker='pyamqp://localhost/test')  # 第一个参数是当前模块的名字
# 第二个参数是broker的url，这里是rabbitmq的，也是默认的。
# 如果是redis则使用'redis://localhost'

app = Celery(__name__, broker='pyamqp://localhost/test', backend='rpc://localhost/test')  # backend


@app.task
def add(x, y):
    """
    定义定一个任务，一个函数就是一个任务，执行任务需要提供任务参数
    :param x:
    :param y:
    :return:
    """
    time.sleep(5)
    return x + y
