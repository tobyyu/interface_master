from Utils.page import *
import unittest
import os
# from Utils.log import *

class Totasks(unittest.TestCase,Helper):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def test_code(self):
        """
        注册验证码接口
        :return:
        """
        url = 'http://rebuildb.hhyp58.com/api'
        datas = {
                "action": "api/User/sendPhoneCode",
                "data": {
                    "mobile": "17800000002",
                    "scene": "login"
                },
                "authorization": {
                    "timestamp": 1874048920,
                    "sign": "215E7FC1248455B8244683B41D996526",
                    "api_key": "88po72c85f96d9d418d5bd064fd116cbfa11d889"
                }
            }
        r =self.post(url,datas)
        self.assertEqual(r.status_code,200)
        self.Createlog("接口断言")
    def test_register(self):
        """
        登录接口
        :return:
        """
        url = 'http://rebuildb.hhyp58.com/api'
        data ={
                "action": "api/User/login",
                "data": {
                    "mobile": 17800000002,
                    "verify_code": "1234"
                },
                "authorization": {
                    "timestamp": 1874048920,
                    "sign": "ACFB7380EF8DB6B82B45512049384BBB",
                    "api_key": "88po72c85f96d9d418d5bd064fd116cbfa11d889"
                }
            }
        r = self.post(url,data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['msg'],'登录成功')
        # print(r.json()['data']['access_token'])
        with open(self.dirname('Token.md'),'w') as f:
            f.write(r.json()['data']['access_token'])
    # def writeToken(self):
    #     url = "http://rebuildb.hhyp58.com/api"
    #     data = {
    #         "action": "api/User/login",
    #         "data": {
    #             "mobile": 17800000002,
    #             "verify_code": "1234"
    #         },
    #         "authorization": {
    #             "timestamp": 1874048920,
    #             "sign": "ACFB7380EF8DB6B82B45512049384BBB",
    #             "api_key": "88po72c85f96d9d418d5bd064fd116cbfa11d889"
    #         }
    #     }
    #     r = self.post(url,data)
    #     with open(self.dirname('Token.md'),'wb') as f:
    #         f.write(r.json()['data']['access_token'])
    def readToken(self):
        with open(self.dirname('Token.md'),'r') as f:
            return f.read()
    def test_assessment(self):
        """
        商品评估
        :return:
        """
        url ='http://rebuildb.hhyp58.com/api'
        data = {
                "action": "api/Good/getAssessment",
                "data": {
                    "goods_id": 1
                },
                "authorization": {
                    "timestamp": 1874048920,
                    "sign": "98B87FF568A9ACE96E512FEC99BF7BF7",
                    "api_key": "88po72c85f96d9d418d5bd064fd116cbfa11d889"
                }
            }
        headers = {
            'Content-Type':'application/json',
            'Authorization':self.readToken()
        }
        r = self.post(url,data,headers)
        self.assertEqual(r.status_code,100)
        # print(r.json())
        self.assertEqual(r.json()['msg'],'ok')
if __name__ == '__main__':
    unittest.main(verbosity=2)