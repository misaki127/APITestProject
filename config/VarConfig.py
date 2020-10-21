import os
import time
# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 全局变量
cookie = ''           #存放cookie
dataIntoExcel = []   #存放测试结果报告数据

# 测试数据文件中，测试用例表中部分列对应的数字序号
#测试用例表
testCase_testCaseName = 2
testCase_frameWorkName = 4
testCase_testStepSheetName = 5
testCase_dataSourceSheetName = 6
testCase_isExecute = 7
testCase_runTime = 8
testCase_testResult = 9

# 需要每次执行传入随机数的sheet名和元素位置行号（暂废弃）
# randomDict = {'物料管理': 8}  # {表名：行号}

# 接口自动化测试用例表中，部分列对应的序号
#接口信息表/token表
testCaseName = 2
testUrl = 3
testMethod = 4
testDataType = 5
testData = 6
testHeaders = 7
testIsToken = 8
testVariable = 9
testVariableName = 10
testSql = 11
testSqlVarible = 12
testRunResult = 13
testApiTime = 14
testApiResult = 15
testResponseCode = 16
testErrorInfo = 17







#--------------上方代码勿动----------------------------------------------------------------------
#下方代码可进行配置







# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testData\\CJMCASE\\数字乡村接口自动化.xlsx"
#dataFilePath = parentDirPath + "\\testData\\CJMCASE\\平台中心接口自动化.xlsx"

# mysql查询参数
# 测试环境数据库
host = '192.168.2.214'
user = 'jgw'
password = 'Jgw*31500-2018.6'
database = 'hydra_digital_village'

# 接口自动化获得token测试表表名
tokenSheetName = 'token'
#接口自动化获取全局变量的表名
globalVariableSheetName = '全局变量表'
#生成报告的sheet名
testReportSheetName = 'report'
# 接口返回token的key名：
tokenKeyName = 'token'

# 多参数分隔符设定
dataSep = '\$\@\@\$'  # 请求参数   隔开多个入参
dataTypeSep = ','  # 请求方式  隔开多个请求参数类型
varibleSep = ','  # 参数变量   隔开多个变量名，需要获取的变量
packVaribleSep = '$$$'  # 包裹变量格式 如$$$householdId$$$   包裹放入入参和sql的变量
sqlSeq = '@@@'  # 多条sql执行时的分隔符
globalVariableSep = '&&&'  #需要引用全局变量时，用此符号包裹变量键名即可，如&&&orgId&&&
#导出数据文件名
importFilePath = parentDirPath + '\\report\\'
#返回的json里有多个ID，只取第一个ID时，配置表名和行号，配置后，此行的变量只取找到的第一个ID，未找到仍会报错
onlyFirstVariable = {"党组织管理":(3,),"一村一码":(3,),"一户一码":(2,3,5,13,),"租户管理":(2,4,),"景点管理":(3,),"酒店管理":(2,4,),"一户一码码关联":(2,4,),
                     "一户一码活动":(3,4,6,),"阳光村务":(3,8,10,16,22,28,35,42,49,55,57,64,71,74,76,80,),"数字党建":(2,4,10,17,23,28,32,34,38,41,44,46,),"村民积分":(2,7,),
                     "信息发布":(3,5,9,11,15,17,21,23,27,29,),"数字乡村H5":(2,6,8,28,32,),'数字乡村':(3,8,11,)}  #{表名：(行号,)}

