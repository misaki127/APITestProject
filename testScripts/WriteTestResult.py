
#往Excel中写入测试结果信息的公共方法

from testScripts import *
from testScripts.Excel_Obj import *
# from . import *
import time


wordList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def writeResult(sheetName,rowNo,colsNo,testResult,errorInfo=None,picPath=None,errorNumber=None,ApiResult=None,ApiResponceCode =None):
    global dataIntoExcel
    colsDict={
        "testCase":[testCase_runTime,testCase_testResult],     #测试用例执行表
        "api-testcase":[testApiTime,testRunResult]       #接口测试用例表
    }


    try:
        #在测试步骤sheet中，写入测试结果,testResult为pass或faild
        dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[colsDict[colsNo][1]-1]+ str(rowNo), 'value': testResult})
        if testResult=="":
            #清空时间单元格内容

            dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[colsDict[colsNo][0]-1]+ str(rowNo), 'value': ''})

        else:
            #在测试步骤sheet中，写入测试时间

            startTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
            dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[colsDict[colsNo][0]-1] + str(rowNo), 'value': startTime})

        if errorInfo:
            #在测试步骤sheet中，写入异常信息

            dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[testErrorInfo-1]+ str(rowNo), 'value': errorInfo})
        elif picPath:
            #在测试步骤sheet中，写入异常截图路径

            dataIntoExcel.append({'sheetName':sheetName,'address':wordList[testStep_errorPic-1]+str(rowNo),'value':picPath})
        else:
            # if colsNo=="caseStep":
            #     #在测试步骤sheet中，清空异常信息单元格

            dataIntoExcel.append({'sheetName':sheetName,'address':wordList[testErrorInfo-1]+str(rowNo),'value':''})
                # 在测试步骤sheet中，清空异常图片路径单元格

        if ApiResult != None and ApiResult !='':

            dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[testApiResult-1] + str(rowNo), 'value': ApiResult})
        if ApiResponceCode != None and ApiResponceCode != '':

            dataIntoExcel.append({'sheetName': sheetName, 'address': wordList[testResponseCode-1] + str(rowNo), 'value': str(ApiResponceCode)})

    except Exception as e:
        print('写excel时发生错误')
        print(traceback.print_exc())

