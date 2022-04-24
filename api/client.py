import requests
import json
import allure
from urllib.parse import urlencode
import  time
from common.logger import *
from common.read_yaml import get_yaml_filepath
from common.readCofig import env
from common.readCofig import Environ

# data = ReadYamlConfigs("data.yaml").get_yaml_data()#读取数据
data = get_yaml_filepath(Environ=Environ)
class HttpClient :
    def __init__(self):
        self.host = data['admin_host']

    default_header = {
      "Content-Type":"application/json"
    }
    def send(self,url,body = {},method= {},headers = {},sessions = '',x_token = ''):

        headers.update(self.default_header)
        # print(headers)
        if x_token :
          headers["Authorization"] = "Bearer " +  x_token.strip('"')  #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
          print("token:",headers)
        if sessions :
          headers["Session"] = "Bearer " + sessions


        if method == "get":
          result =  requests.get(url,params = body,headers = headers)
        elif method == "post":
          # result =  requests.post(url,data = json.dumps(body),headers=headers)
          result =  requests.post(url,json = body,headers=headers)
        elif method == "patch":
          result = requests.patch(url,data = json.dumps(body),headers=headers)

        self.create_response_log(result.status_code,result.json())
        self.create_request_log(url,method,body,headers)
        # print("result.json()",result.json()['code'])
        assert result.status_code or result.code == 200
        # return {"status_code":result.status_code,"data":result.json()}
        # print("result.json()result.json()",result.json())
        # print("result.status_code",result.status_code)
        return result.json()


    def get_full_url(self,url,etc= {},replace = {},h=""):
        if h:
          host = h.rstrip('/')   #rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
        else:
          host = self.host.rstrip('/')

        url = url.lstrip('/')       #lstrip() 方法用于截掉字符串左边的空格或指定字符。
        full_url = host + "/" + url
        full_url += "?platform={}&time=".format(env) + str(int(round(time.time() * 1000)))
        if etc:
          s = urlencode(etc)      #urlencode  urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
          full_url += "&" +s
        if replace:
          full_url = str.format(full_url,replace) #str.format() 方法通过字符串中的花括号 {} 来识别替换字段 replacement field，从而完成字符串的格式化。
        return full_url

    @allure.step("请求日志")
    def create_request_log(self,url,method,body,headers):
        pass
      # print("请求日志",url,method,body,headers)
    @allure.step('响应日志')
    def create_response_log(self,status_code,text):
        # pass
      print("响应日志",status_code,text)

if __name__ == '__main__':
    clent = HttpClient()
    re = clent.send(url='http://121.37.169.128:8201/mall-member/sso/login?platform=test&time=1633935913596&password=123456&username=admin',
                       body = {},method= 'post',headers = {'Content-Type': 'application/json'})
