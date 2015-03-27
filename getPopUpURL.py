# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService =  CashbillService(testValue.LinkID,testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

try:
    print("현금영수증 팝업 URL 확인")

    MgtKey = "20150326-01" # 전자명세서 문서관리번호
    UserID = testValue.testUserID

    url = cashbillService.getPopUpURL(testValue.testCorpNum,MgtKey,UserID)
    print("URL: %s" % url)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))