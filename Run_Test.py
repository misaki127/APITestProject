import sys
sys.path.append(sys.path[0] + '\\testcase\CJM')
sys.path.append(sys.path[0] + '\\config')
sys.path.append(sys.path[0] + '\\action')
sys.path.append(sys.path[0] + '\\exceptionpictures')
sys.path.append(sys.path[0] + '\\log')
sys.path.append(sys.path[0] + '\\testData/CJMCASE')
sys.path.append(sys.path[0] + '\\testScripts')
sys.path.append(sys.path[0] + '\\util')


from VarConfig import *
from testcase.CJM.CJMAPI import CJMAPI

CJMAPI()


