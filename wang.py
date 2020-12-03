#coding=utf8
#测试用文件
import requests,re

def jsonGetInfo(data,findData,dataName):  #在返回的json数据里查找对应数据,返回对应的值，str格式，data:接口返回的json数据或str数据，endData:查找的value的KEY值，相同的名称可以只填一个,未找到返回一个None，dataName:找到数据后存入的变量名
    #                                                 #数据和变量名按顺序配对
    try:
        resultList = []  #查找结果数据
        if isinstance(data,str):
            pass
        else:
            data=str(data)
        data = data.strip()
        findData = findData.strip()
        dataName = dataName.strip()
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

a = None
if a != None and a != '':
    print('success')
else:
    print('fail')
