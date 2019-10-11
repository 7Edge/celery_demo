#! /usr/bin/env python
# coding:utf-8
"""
call celery task任务
"""
import time
from task import add

rv = add.delay(10, 20)
print(rv.id)
for i in range(3):
    time.sleep(3)
    print(rv.ready())
    if rv.ready:
        print(rv.get())

rv2 = add.delay(1, 20)
print(rv2.get())  # get相当于是一个同步获取一般不会发起了任务立即就获取结果，而是先通过ready返回True后才回去获取结果。
# 也可以通过timeout设置同步超时时间。设置propagate=False可以不跑出异常

# 对于使用了backend占存任务结果，需要显示的get或者forget来从backend中释放结果。避免内存泄漏
