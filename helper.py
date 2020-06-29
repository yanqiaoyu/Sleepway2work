'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-29 23:21:57
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-29 23:47:50
@FilePath: /Sleepway2work/helper.py
'''
import time

def logdeco(func):
    def wrapper(*args, **kw):
        print('[{}][{}]Begin'.format(func.__qualname__, time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time()))))
        func(*args, **kw)
        print('[{}][{}]Finish'.format(func.__qualname__, time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time()))))
    return wrapper