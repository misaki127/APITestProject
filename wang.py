
import requests

url = "http://system.nine.kf315.net/apiInterface/interface/hydra-open-thirdpart-service/hydra-open-third-party/api/v1/file/open/upload"

payload = {'name': '一户一码导入模板.xlsx'}
files = {'file': ('file', open('C:/Users/Dell/Desktop/一户一码导入模板.xlsx','rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',{'Expires': '0'})}
headers = {
  'Cookie': 'super-token=ef5a1a0276134a69ab45b9fbd69527be; JSESSIONID=69B196A4ACCBA0E9E3EE9AD64EC37277; super-token=e59c318bd7b54a2caaef978f0c42a166'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

















# import requests
#
# url = 'http://system.nine.kf315.net/apiInterface/interface/hydra-open-thirdpart-service/hydra-open-third-party/api/v1/file/open/upload'
# url2 = 'http://system.nine.kf315.net/apiInterface/interface/digital-village/hydra-digital-village/api/v1/family-information/importFamily'
# payload = {'name': '一户一码导入模板.xlsx'}
# files = [
#   ('file', open('C:/Users/Dell/Desktop/一户一码导入模板.xlsx','rb'))
# ]
# headers = {'Cookie':'super-token=e59c318bd7b54a2caaef978f0c42a166'}
# response = requests.request("POST", url, headers=headers, data = payload, files = files)
# print(response.text.encode('utf8'))
# #
# code = response.json()['results']
# data2 = {"fileName":"一户一码导入模板.xlsx","uniqueCode":'65bde79d90964f44baf76ca8d339f2d1'}
# #
#
#
# def getResponse(url,method, **kwargs):
#         # """封装request方法"""
#         # # 获取请求参数
#     params = kwargs.get("params")
#     data = kwargs.get("data")
#     json = kwargs.get("json")
#     headers = kwargs.get('headers')
#     cookies = kwargs.get('cookies')
#     files = kwargs.get('files') #{name ,(filename,fileobj,'content_type', custom_headers) }
#     auth = kwargs.get('auth')  #自定义身份验证
#     timeout = kwargs.get('timeout') #超时
#     allow_redirects = kwargs.get('allow_redirects')#boolen 是否运行重定向
#     proxies = kwargs.get('proxies')#代理
#     verify = kwargs.get('verify')#boolen 它控制我们是否验证服务器的TLS证书或字符串，在这种情况下，它必须是路径要使用的CA包。默认为“True”。
#     stream = kwargs.get('stream')#如果``False``，则立即下载响应内容。
#     cert = kwargs.get('cert') #如果是字符串，就是证书路径，如果是元组就是（证书，密钥）
#     hooks = kwargs.get('hooks')#信号事件处理  传递一个 {hook_name: callback_function} 字典给 hooks 请求参数若执行你的回调函数期间发生错误，系统会给出一个警告。若回调函数返回一个值，默认以该值替换传进来的数据。若函数未返回任何东西， 也没有什么其他的影响
#
#     try:
#         r = requests.request(method=method,url=url,params=params,data=data,json=json,headers=headers,cookies=cookies
#                                      ,files=files,auth=auth,timeout=timeout,allow_redirects=allow_redirects,proxies=proxies
#                                      ,verify=verify,stream=stream,cert=cert,hooks=hooks)
#         return r
#     except Exception as e:
#         print("请求错误: %s" % e)
#
#
#
# r2 =getResponse(url=url2,method='post',json=data2,headers=headers)
# #
# print(r2.json())
# # url3 = 'http://system.nine.kf315.net/apiInterface/interface/digital-village/hydra-digital-village/api/v1/family-information/delete'
# # data = {'householdID':'3f64d1a5250c45fc978f1a868fbfde9f'}
# # r = requests.post(url3,data=data,headers=headers)
# # print(r.json())

