import smtplib   #邮箱服务
from email.mime.text import MIMEText   #邮箱模板
import unittest
from Utils.HTMLTestRunner import HTMLTestRunner
import time,os
from email.mime.multipart import MIMEMultipart  #邮箱附件
from email.header import Header   #邮箱头部模板
import configparser
from Utils.page import *
#发送待邮件的函数
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    #基本信息
    smtpserver = Helper().readConfig()[0]
    pwd = Helper().readConfig()[1]
    # 定义邮箱主题
    msg = MIMEMultipart()
    msg['subject']=Header(Helper().readConfig()[-1],'utf-8')
    msg['from'] = Helper().readConfig()[3]
    msg['to'] =Helper().readConfig()[4]
    body = MIMEText(mail_body,"base64","utf-8")
    msg.attach(body)
    att = MIMEText(mail_body,'base64','utf-8')
    att['Content-Type'] ="application/octet-stream"
    att['Content-Disposition'] ='attachment;filename="Interface_report.html"'
    msg.attach(att)
    #链接邮箱服务发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(msg['from'],pwd)
    smtp.sendmail(msg['from'],msg['to'],msg.as_string())
    print("邮件发送成功")
    #查找最新的邮箱
def new_file(test_dir):
    result_dir = test_dir
    # 列出测试报告目录下的所有文件
    lists = os.listdir(result_dir)
    lists.sort()  #排序
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(result_dir,file[-1])
    return file_path

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(base_dir,'testCases')
    test_report = os.path.join(base_dir,'Reports')
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report+'\\'+now +'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'接口自动化框架测试报告',
        description=u'系统环境：win10'
    )
    runner.run(testlist)
    fp.close()
    new_report = new_file(test_report)
    send_mail(new_report)