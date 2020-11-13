#code:utf-8
#测试用文件
import requests

def getResponse(url,method, **kwargs):
        # """封装request方法"""
        # # 获取请求参数
    params = kwargs.get("params")
    data = kwargs.get("data")
    json = kwargs.get("json")
    headers = kwargs.get('headers')
    cookies = kwargs.get('cookies')
    files = kwargs.get('files') #{name ,(filename,fileobj,'content_type', custom_headers) }
    auth = kwargs.get('auth')  #自定义身份验证
    timeout = kwargs.get('timeout') #超时
    allow_redirects = kwargs.get('allow_redirects')#boolen 是否运行重定向
    proxies = kwargs.get('proxies')#代理
    verify = kwargs.get('verify')#boolen 它控制我们是否验证服务器的TLS证书或字符串，在这种情况下，它必须是路径要使用的CA包。默认为“True”。
    stream = kwargs.get('stream')#如果``False``，则立即下载响应内容。
    cert = kwargs.get('cert') #如果是字符串，就是证书路径，如果是元组就是（证书，密钥）
    hooks = kwargs.get('hooks')#信号事件处理  传递一个 {hook_name: callback_function} 字典给 hooks 请求参数若执行你的回调函数期间发生错误，系统会给出一个警告。若回调函数返回一个值，默认以该值替换传进来的数据。若函数未返回任何东西， 也没有什么其他的影响

    try:
        r = requests.request(method=method,url=url,params=params,data=data,json=json,headers=headers,cookies=cookies
                                     ,files=files,auth=auth,timeout=timeout,allow_redirects=allow_redirects,proxies=proxies
                                     ,verify=verify,stream=stream,cert=cert,hooks=hooks)
        return r
    except Exception as e:
        print("请求错误: %s" % e)
from selenium import webdriver

