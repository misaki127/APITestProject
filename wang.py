#coding=utf8
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

import re
def jsonGetInfo(data,findData,dataName):  #在返回的json数据里查找对应数据,返回对应的值，str格式，data:接口返回的json数据或str数据，endData:查找的value的KEY值，相同的名称可以只填一个,未找到返回一个None，dataName:找到数据后存入的变量名
    #                                                 #数据和变量名按顺序配对
    try:
        resultList = []  #查找结果数据
        if isinstance(data,str):
            pass
        else:
            data=str(data)
        dataList = re.split('[^\w_-]',data)
        dataList = list(filter(None, dataList))
        findDataList = re.split(',',findData)
        dataNameList = re.split(',',dataName)
        for i in dataList:
            for a in findDataList:
                if a == i:
                    index = [c for c, x in enumerate(dataList) if x == i]

                    for b in index:
                        result = dataList[b + 1]
                        resultList.append(a)
                        resultList.append(result)

        resultDict = {}
        endDict = {}
        for f in range(0, len(resultList), 2):
            resultDict[resultList[f]] = resultList[f + 1]
        if len(resultDict) != len(findDataList):
            noList = []
            for k in findDataList:
                if k not in resultDict:
                    noList.append(k)
            print(str(noList) + '值未取到')
        for p in resultDict:
            Pindex = [c for c, x in enumerate(findDataList) if x == p]
            endDict[dataNameList[Pindex[0]]] = resultDict[p]
        return endDict

    except IndexError:
        print('查找' + str(a) + '时，查找到的值为空，请检查输入是否正确！')
    except Exception as e:
        print('jsonGetInfo:' + str(e))

from selenium import webdriver

data = {'state': 200, 'internalErrorCode': '0', 'msg': 'success', 'results': {'villageId': 'cc592d3a2c264389b49c2e547ff6a5ee', 'villageNumber': '3301060050000002', 'villageName': '王汉村', 'regionCode': '330106005000', 'villageTownshipName': None, 'regionCodeName': None, 'townshipName': '华星路99号', 'image': '97a9c35cc7a24c899eb2ccc57cbe7f8b', 'introduction': '<p>测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据测试数据</p>', 'address': '浙江省杭州市西湖区2号线古翠路(地铁站)', 'longitude': 120.120997, 'latitude': 30.278255, 'area': 5000.0, 'perCapitaIncome': 6000.0, 'ext': [{'villageExtId': '861fe2157c7b4e798025f025c2fbab84', 'villageId': 'cc592d3a2c264389b49c2e547ff6a5ee', 'name': '王汉村', 'address': '[[120.119817,30.278977],[120.119978,30.277217],[120.122338,30.277365],[120.122199,30.278088],[120.122156,30.278282],[120.122456,30.278403],[120.122585,30.278588],[120.122521,30.279107]]', 'naturalVillageNumber': 'WHC1606878832176'}], 'naturalVillage': None, 'multiple': 17, 'househoIdIdList': None}}

s = False
b = 200
for A in range(6):

    if b in [100,200,'100','200'] and s:
        print('success')
    elif b not in [100,200,'100','200']  or  s:
        print("fali")

