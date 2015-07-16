# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService,PopbillException

cashbillService =  CashbillService(testValue.LinkID,testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
  
try:
    print("현금영수증 상태정보 확인 - 대량")
    
    #현금영수증 문서관리번호 배열, 최대 1000건
    MgtKeyList = ["20150707-01","20150706-01"]
   
    InfoList = cashbillService.getInfos(testValue.testCorpNum,MgtKeyList)

    # 상태정보 구성은 getInfo() 예제 확인.
    for info in InfoList:
        print("info : %s" % info.mgtKey)
        for key, value in info.__dict__.items():
            if not key.startswith("__"):
                print("     %s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))