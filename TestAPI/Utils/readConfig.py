import os
import configparser
proDir = os.path.dirname(os.path.realpath(__file__))
conf_path = proDir+'\Config'
configPath = os.path.join(conf_path,'config.ini')
print(configPath)
cf = configparser.ConfigParser()
cf.read(configPath,encoding ='utf-8')
class ReadConfig(object):
    def get_http(self, name):
        value = cf.get('HTTP', name)
        return value
if __name__ == '__main__':
    co = ReadConfig()
    print(co.get_http('baseurl'))