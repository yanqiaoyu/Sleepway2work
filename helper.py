'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-29 23:21:57
@LastEditors: YanQiaoYu
@LastEditTime: 2020-07-01 17:48:11
@FilePath: /Sleepway2work/helper.py
'''
import time
import logging, logging.handlers
import os
from sql import mysql

'''
@description: 由于UIAutomator也使用了logging这个库,需要重新定义自己的log类,才能输出到自己想要的文件里面
@param {type} 
@return: 
'''
class LogMgr:
    def __init__ (self):
        '''
        self.LOG = logging.getLogger('log')
        loghdlr1 = logging.handlers.RotatingFileHandler(logpath,"a", 0, 1)
        fmt1 = logging.Formatter("%(asctime)s %(threadName)-10s %(message)s", "%Y-%m-%d %H:%M:%S")
        loghdlr1.setFormatter(fmt1)
        self.LOG.addHandler(loghdlr1)
        self.LOG.setLevel(logging.INFO)
        '''
        self.MARK = logging.getLogger('mark')
        loghdlr2 = logging.handlers.RotatingFileHandler('./sleepway2work.log',"a", 0, 1)
        fmt2 = logging.Formatter("[%(asctime)s] - %(levelname)s: %(message)s")
        loghdlr2.setFormatter(fmt2)
        self.MARK.addHandler(loghdlr2)
        self.MARK.setLevel(logging.INFO)
    def error(self, msg):
        if self.MARK is not None:
            self.MARK.error(msg)
    def info(self, msg):
        if self.MARK is not None:
            self.MARK.info(msg)
    def debug(self, msg):
        if self.MARK is not None:
            self.MARK.debug(msg)
    def mark(self, msg):
        if self.MARK is not None:
            self.MARK.info(msg)

log_mgr = LogMgr()


def logdeco(func):
    def wrapper(*args, **kw):
        log_mgr.info('[{}]Begin'.format(func.__qualname__ ))

        local_time = time.time()

        dicResult = func(*args, **kw)

        if dicResult:
            sql = mysql()
            log_mgr.info('[{}]Result:{}'.format(func.__qualname__, dicResult))
            if True == sql.UpdateMyData(dicResult):
                log_mgr.info('[{}]Update Data Successfully!'.format(func.__qualname__))
                sql.CommitAndClose()
            else:
                log_mgr.error('[{}]Update Data Fail!'.format(func.__qualname__))
                sql.RollBackAndClose()
        log_mgr.info('[{}]Finish'.format(func.__qualname__ ))

        log_mgr.info('[{}]Running Time:{}'.format(func.__qualname__, time.time() - local_time))
        
        return dicResult
    return wrapper