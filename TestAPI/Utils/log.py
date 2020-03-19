import os
import logging
import time
class Log:
    def __init__(self):
        self.logPath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Log')
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        self.logPath = os.path.join(self.logPath,time.strftime('%Y%m%d%H%M',time.localtime(time.time())))
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        # 初始化
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.INFO)
        # 写入日志文件
        fmt = logging.FileHandler(os.path.join(self.logPath,'log.txt'))
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s - '
                                      '%(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')
        fmt.setFormatter(formatter)
        # loggers = logging.Logger('lo')
        self.logger.addHandler(fmt)
    def get_logger(self):
        return self.logger