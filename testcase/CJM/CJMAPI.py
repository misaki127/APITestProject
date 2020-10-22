#code:utf-8
#author:wanghan
from WriteTestResult import writeResult
from testScripts.Excel_Obj import *
from util.Log import *
from response import getResponse,jsonGetInfo,splitCode,updateVaribleForDict,updateVaribleForStr,sqlGetVarible,getImportInfo,jsonGetFirstInfo,createReportSheet
from VarConfig import *

def getToken(globalVariable,getTokenSheetName):
    try:
        global cookie,tokenSheet
        tokenSheet = getTokenSheetName
        caseStepObj = excelObj.getSheetByName(getTokenSheetName)
        stepNums = excelObj.getRowsNumber(caseStepObj)
        # 执行用例前，先获取一次excel表内的全局变量

        success = 0
        dataName = 'token'
        logging.info("\033[1;32;m测试用例共%s步\033[0m" % stepNums)
        for index in range(2, stepNums + 1):
                #获取步骤sheet中第index行对象
            stepRow = excelObj.getRow(caseStepObj, index)
            url = stepRow[testUrl - 1].value
            if globalVariableSep in url and globalVariable != {}:
                url = updateVaribleForStr(data=url, dict=globalVariable, separtor=globalVariableSep)
            method = stepRow[testMethod - 1].value
            dataType = stepRow[testDataType - 1].value
            data = stepRow[testData - 1].value
            # 检查  入参   是否有变量信息，有的话则去变量字典查找，未找到则不改变，默认为非变量信息
            if data != None and data != '':
            # 检查入参是否有引用全局变量，有就替换
                if globalVariableSep in data and globalVariable != {}:
                    data = updateVaribleForDict(data=data, dict=globalVariable, separtor=globalVariableSep)
            headers = stepRow[testHeaders - 1].value


            if headers == None or headers == '':
                headers = {}
            elif isinstance(headers,str):
                headers = eval(headers)
            headers['Cookie'] = cookie
            endData = splitCode(dataType, data)

            if endData == None:
                logging.info('参数处理失败，请检查是否填写正确！')
                cookie = ''
                break
            else:
                r = eval(
                        'getResponse(' + 'url="' + url + '",method="' + method + '",headers='+str(headers)+',' + endData.replace("'", '"') + ')')
                logging.info('getResponse(' + 'url="' + url + '",method="' + method + '",headers='+str(headers)+',' + endData.replace("'", '"') + ')')
                resultJson = r.json()
                if resultJson['state'] == 200:
                    success +=1

                if 'token' in str(resultJson):
                    token = jsonGetInfo(resultJson,tokenKeyName,dataName)   #获取token
                    cookie = 'super-token='+str(token[dataName])

        if success==stepNums-1:
            logging.info('获取token成功！')

        else:
            logging.info('获取token失败，请重新配置文件！')

            raise ValueError

    except Exception as e:
        logging.info('getToken erroe is {0}'.format(str(e)))



def getGlobalVariable():
    try:
        caseStepObj = excelObj.getSheetByName(globalVariableSheetName)
        stepNums = excelObj.getRowsNumber(caseStepObj)
        colNums = excelObj.getColsNumber(caseStepObj)
        DictGlobalVariable = {}
        if colNums != 2:
            logging.debug("全局变量表内的数据不符合模板，请检查是否填写错误！")
            raise ValueError

        for index in range(2, stepNums + 1):
            stepRow = excelObj.getRow(caseStepObj, index)
            key = stepRow[0].value
            value = stepRow[1].value
            if key=='':
                logging.debug("键的值必须不为空！")
                raise ValueError
            DictGlobalVariable[key] = value

        return DictGlobalVariable
    except Exception as e:
        logging.info("getGlobalVariable error:"+str(e))




def CJMAPI():
    try:
        global cookie,dataIntoExcel,tokenSheet
        #根据Excel文件中的sheet名获取sheet对象
        caseSheet=excelObj.getSheetByName('测试用例')

        #存入开始时间数据
        dataIntoExcel.append({'sheetName':testReportSheetName,'address':'B2','value':str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )})
        startTimeNum = time.time()
        #获取测试用例sheet中是否执行该列对象
        isExecuteColumn=excelObj.getColumn(caseSheet,testCase_isExecute)
        #获取测试用例全部的sheet名
        sheetNames = excelObj.getSheetNames()

        #记录执行成功的测试用例个数
        successfulCase=0

        passNums = 0
        failNums = 0

        #记录需要执行的用例个数
        requiredCase=0

        #执行用例前，先获取一次token存着
        # 执行用例前，先获取一次excel表内的全局变量
        # 执行用例前，先获取一次excel表内的全局变量
        globalVariable = getGlobalVariable()
        logging.info('全局变量为：' + str(globalVariable))
        #getToken(globalVariable)

        row = 3
        for idx,i in enumerate(isExecuteColumn[1:]):

            caseName=excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_testCaseName)


            row +=1
            dataIntoExcel.append({'sheetName':testReportSheetName,'address':'A'+str(row),'value':caseName})

            logging.info('\033[1;32;m-----开始执行%s用例-------\033[0m' % caseName)

            #循环遍历”测试用例“表中的测试用例，执行被设置为执行的用例
            if i.value.strip().lower()=='y':

                requiredCase+=1

                #获取测试用例表中，第idx+1行中用测试执行时所使用的框架类型
                userFrameWorkName=excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_frameWorkName)


                #获取测试用例表中，第idx+1行中执行用例的步骤sheet名
                stepSheetName=excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_testStepSheetName)


                if userFrameWorkName == '关键字':
                    logging.info("\033[1;32;m****调用关键字驱动***\033[0m")

                    caseStepObj = excelObj.getSheetByName(stepSheetName)

                    stepNums = excelObj.getRowsNumber(caseStepObj)

                    #写入报告
                    dataIntoExcel.append(
                        {'sheetName': testReportSheetName, 'address': 'B' + str(row), 'value': stepNums-1})

                    code200Nums = 0   #响应码是200的接口数
                    codeNot200Nums = 0   #响应码不是200的接口数
                    successfulSteps = 0
                    logging.info("\033[1;32;m测试用例共%s步\033[0m" % stepNums)
                    variableDict = {}                 #每一个测试用例sheet会创建一个变量字典，用于存储变量名和值，变量名相同的，晚进入的会覆盖早进入的
                    for index in range(2, stepNums + 1):
                        try:
                            variableDict_ext = {}
                            tokenCheck = 0
                            getTokenCount = 0
                            errorInfo = ''
                            while tokenCheck == 0:
                                if getTokenCount >=3: #同一条用例连续获取三次token报错，说明获取的token错误
                                    logging.info('请求三次token失败，请检查获取token表是否正常！')
                                    raise TimeoutError

                                # 获取步骤sheet中第index行对象
                                stepRow = excelObj.getRow(caseStepObj, index)


                                testCaseNamep = stepRow[testCaseName-1].value
                                url = stepRow[testUrl-1].value
                                #检查url是否使用全局变量
                                if globalVariableSep in url and globalVariable != {}:
                                    url = updateVaribleForStr(data=url, dict=globalVariable, separtor=globalVariableSep)
                                method = stepRow[testMethod-1].value
                                sql = stepRow[testSql - 1].value
                                sqlVarible = stepRow[testSqlVarible - 1].value


                                #检查sql是否有入参，有点话则去变量字典查找，并拼接，未找到就不改变
                                if sql != None and sql != '':

                                    if packVaribleSep in sql and variableDict !={}:
                                        #检查是否引用变量，有的话替换值
                                        sql = updateVaribleForDict(data=sql,dict=variableDict,separtor=packVaribleSep)
                                    #检查是否有引用全局变量，有的话就替换值
                                    if globalVariableSep in sql and globalVariable != {}:
                                        sql = updateVaribleForDict(data=sql, dict=globalVariable,separtor=globalVariableSep)

                                # 对请求参数和数据类型进行处理，处理单参数和多参数情况
                                    variableDict_ext = sqlGetVarible(sql, sqlVarible)

                                if variableDict_ext:
                                    if variableDict_ext != None:
                                        variableDict.update(variableDict_ext)  # 将sql获得 的变量存入变量字典

                                dataType = stepRow[testDataType-1].value

                                data = stepRow[testData-1].value

                                #检查  入参   是否有变量信息，有的话则去变量字典查找，未找到则不改变，默认为非变量信息
                                if data != None and data != '':
                                    #检查入参是否有引用变量，有就替换
                                    if packVaribleSep in data and variableDict != {}:
                                        data = updateVaribleForDict(data=data,dict=variableDict,separtor=packVaribleSep)
                                    #检查入参是否有引用全局变量，有就替换
                                    if globalVariableSep in data and globalVariable != {}:
                                        data = updateVaribleForDict(data=data,dict=globalVariable,separtor=globalVariableSep)


                                    endData = splitCode(dataType, data)
                                else:
                                    endData = ''

                                headers = stepRow[testHeaders-1].value
                                isToken = stepRow[testIsToken-1].value
                                if isToken in sheetNames:
                                #huoqu token
                                    if cookie != None and cookie != '':
                                        if tokenSheet == isToken:
                                            break
                                        elif tokenSheet != isToken:
                                            getToken(globalVariable,isToken)
                                            if headers == None or headers == '':
                                                headers = {'Cookie':cookie}
                                            else:
                                                headers = eval(headers)
                                                headers['Cookie'] = cookie
                                    else:
                                        getToken(globalVariable,isToken)

                                #headers = {'Content-Type':'application/octet-stream','Connection':'keep-alive'}
                                variable = stepRow[testVariable-1].value  #需要传递的参数
                                variableName = stepRow[testVariableName-1].value #需要传递的参数的命名

                                if endData == None:
                                    print('入参错误，请检查重新输入！')
                                    resultJson = False
                                    errorInfo = '入参错误，请检查重新输入！'
                                    result = False
                                else:
                                    try:
                                        if headers !='' and headers!=None:
                                            requestCode = 'getResponse(' +'url="'+url+'",method="' +method+'",headers='+str(headers)+','+ endData.replace("'",'"') +')'
                                            logging.info(
                                                'isHeaders request:' + 'getResponse(' + 'url="' + url + '",method="' + method + '",headers=' + str(
                                                    headers) + ',' + endData.replace("'", '"') + ')')
                                            r = eval(requestCode)

                                        else:
                                            requestCode='getResponse(' +'url="'+url+'",method="' +method+'",'+ endData.replace("'",'"') +')'
                                            logging.info(
                                                'NoHeaders request:' + 'getResponse(' + 'url="' + url + '",method="' + method + '",' + endData.replace(
                                                    "'", '"') + ')')
                                            r = eval(requestCode )

                                        if r ==None:
                                            raise ValueError
                                        if '导出' in testCaseNamep:  # 如果测试用例名称里有导出字样，自动将内容存入excel
                                            logging.info('进入导出程序')
                                            filename= getImportInfo(r)
                                            logging.info('导出数据已写入:'+filename)
                                            resultJson = {'state':200,'msg':'导出成功！'}
                                        else:
                                            resultJson = r.json()
                                        logging.info("Response: " + str(resultJson))
                                    except Exception as e:
                                        errorInfo = str(e)
                                        resultJson = False
                                        logging.info('请求错误！' + str(e))
                                if resultJson['state'] == 401:
                                    getToken(globalVariable,isToken)
                                    getTokenCount +=1
                                    tokenCheck = 0
                                    result = False
                                elif resultJson == False or resultJson == None:
                                    result = False
                                    tokenCheck =1

                                else:
                                    result = True
                                    tokenCheck = 1
                                    ResponceCode = resultJson['state']
                                    if variable =='' or variable == None:
                                        pass
                                    elif variableName == '' or variableName == None:
                                        pass
                                    else:
                                        #onlyFirstVariable 检测
                                        if stepSheetName in list(onlyFirstVariable.keys()):  #检测表名

                                            if index in onlyFirstVariable[stepSheetName]:
                                                variableDict_ext = jsonGetFirstInfo(resultJson,variable,variableName)
                                            else:
                                                variableDict_ext = jsonGetInfo(resultJson, variable, variableName)
                                        else:
                                            variableDict_ext = jsonGetInfo(resultJson, variable,variableName)
                                    if variableDict_ext != None:
                                        variableDict.update(variableDict_ext)

                        except Exception as e:
                            logging.info('error is '+str(e))
                            result = False
                            errorInfo = str(e)

                        row += 1
                        dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'B'+str(row)+':E'+str(row), 'value': 'merge_cells'})

                        if result:
                            successfulSteps += 1
                            logging.info('\033[1;32;m步骤%s成功\033[0m' % stepRow[testCaseName - 1].value)
                            if resultJson['state'] == 200 or resultJson['state']== '200':
                                writeResult(stepSheetName, rowNo=index, colsNo="api-testcase", testResult="pass",ApiResult=str(resultJson),ApiResponceCode=str(ResponceCode),errorInfo=None,errorNumber=testErrorInfo)
                                dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'B' + str(row), 'value': 'pass'})
                                dataIntoExcel.append({'sheetName':testReportSheetName,'address':'F'+str(row),'value':str(resultJson)})
                            elif resultJson['state'] == 500 or resultJson['state']== '500':
                                writeResult(stepSheetName, rowNo=index, colsNo="api-testcase", testResult="faild",
                                            ApiResult=str(resultJson), ApiResponceCode=str(ResponceCode),
                                            errorInfo=None, errorNumber=testErrorInfo)
                                dataIntoExcel.append(
                                    {'sheetName': testReportSheetName, 'address': 'B' + str(row), 'value': 'faild'})
                                dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'F' + str(row),
                                                      'value': str(resultJson)})
                            if resultJson['state'] == 200:
                                code200Nums +=1
                            else:
                                codeNot200Nums +=1
                            logging.info('变量字典为{0}'.format(str(variableDict)))
                        else:
                            logging.info('\033[4;31;m执行步骤%s发生异常\033[0m' % stepRow[testCaseName - 1].value)
                            writeResult(stepSheetName, rowNo=index, colsNo="api-testcase", testResult="faild",errorInfo=errorInfo, errorNumber=testErrorInfo,ApiResult='Error!',ApiResponceCode='Error')
                            dataIntoExcel.append({'sheetName': testReportSheetName, 'address':'B' + str(row), 'value': 'faild'})
                            dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'F'+str(row), 'value': str(errorInfo)})


                        dataIntoExcel.append({'sheetName': testReportSheetName, 'address':'A'+str(row), 'value': testCaseNamep})

                    dataIntoExcel.append({'sheetName': testReportSheetName, 'address':'C'+str(row-stepNums+1), 'value': str(code200Nums)})
                    dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'D'+str(row-stepNums+1), 'value': str(codeNot200Nums)})
                    dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'E'+str(row-stepNums+1), 'value': str(stepNums-1-successfulSteps)})

                    passNums += code200Nums
                    failNums += stepNums-1-code200Nums


                    if successfulSteps == stepNums - 1:
                        successfulCase += 1
                        logging.info('\033[1;32;m用例%s执行通过\033[0m' % caseName)

                        writeResult('测试用例',rowNo=idx + 2, colsNo='testCase', testResult='pass')
                    else:
                        logging.info('\033[4;31;m用例%s执行失败\033[0m' % caseName)

                        writeResult('测试用例', rowNo=idx + 2, colsNo='testCase', testResult='faild')


                else:

                    logging.info('目前仅支持关键字驱动！')


            else:
                '''
                清空不需要执行的执行时间和执行结果，
                异常信息，异常图片单元格
                '''
                logging.info('\033[0;34;m用例%s设置的为不执行，请检查确认。。\033[0m'%caseName)

                writeResult('测试用例',rowNo=idx+2,colsNo='testCase',testResult="")

                logging.info("\033[1;32;m共%d条用例，%d条需要被执行，成功执行%d条\033[0m"%(len(isExecuteColumn)-1,requiredCase,successfulCase))
        endTimeNum = time.time()

        dataIntoExcel.append({'sheetName': testReportSheetName, 'address':'D2', 'value': str(endTimeNum-startTimeNum)})
        dataIntoExcel.append({'sheetName': testReportSheetName, 'address': 'F2', 'value': '成功:'+str(passNums)+' 失败:'+str(failNums)})
        #logging.info('dataIntoExcel: ' + str(dataIntoExcel))
        createReportSheet(filePath=dataFilePath,data=dataIntoExcel)

    except Exception as e:
        logging.debug(traceback.print_exc())