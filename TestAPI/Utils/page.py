import os
import requests
import logging
import time
import configparser
class Helper(object):
    def get(self,url,headers=''):
        """
        重构get方法
        :param url:
        :param headers:
        :return:
        """
        if url:
            r = requests.get(url=url,headers=headers)
            return r
        else:
            try:
                print("接口错误")
            except Exception as e:
                print("错误原因 %s " %e)
    def post(self,url,data,headers=''):
        """
        重构post方法
        :param url:
        :param data:
        :param headers:
        :return:
        """
        if url:
            r = requests.post(url=url,json=data,headers=headers)
            return r
        else:
            try:
                print("接口地址错误")
            except Exception as e:
                print("错误原因 %s" %e)

    def dirname(self,fileName='',filePath='Data'):
        """
        新增参数文件
        :param fileName: 文件名
        :param filePath: 写入的文件目录
        :return:
        """
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,fileName)

    def Createlog(self,log_content):
        """
        日志
        :param log_content:
        :return:
        """
        # 定义日志文件
        logfiler = logging.FileHandler(self.dirname('log.txt','Log'),'a',encoding='utf-8')
        fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        logfiler.setFormatter(fmt)
        # 定义日志
        logger1 = logging.Logger('LogTest',level=logging.DEBUG)
        logger1.addHandler(logfiler)
        logger1.info(log_content)
        logfiler.close()

    def readConfig(self):
        """
        读取配置文件的内容
        :return:
        """
        savedata =[]
        config = configparser.ConfigParser()
        config.read(self.dirname('config.ini','Config'),encoding='utf-8')
        email_host = config.get('EMAIL',"mail_host")
        email_pass = config.get('EMAIL','mail_pass')
        email_sender = config.get('EMAIL','sender')
        email_user = config.get('EMAIL','mail_user')
        email_receiver = config.get('EMAIL', 'receiver')
        email_subject = config.get('EMAIL', 'subject')
        savedata.append(email_host)
        savedata.append(email_pass)
        savedata.append(email_user)
        savedata.append(email_sender)
        savedata.append(email_receiver)
        savedata.append(email_subject)
        return savedata

if __name__ == '__main__':
    print(Helper().readConfig())

