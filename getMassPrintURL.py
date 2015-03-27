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
    print("현금영수증 다량 인쇄 URL")

    MgtKeyList = ["20150326-01","20150326-02","20150326-03"] # 인쇄하고자 하는 문서관리번호 배열
    UserID = testValue.testUserID

    url = cashbillService.getMassPrintURL(testValue.testCorpNum,MgtKeyList,UserID)
    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))