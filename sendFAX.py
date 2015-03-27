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
    print("현금영수증 팩스 전송")

    MgtKey = "20150326-01" # 현금영수증 문서관리번호
    Sender = "07075103710" # 발신번호
    Receiver = "010111222" # 수신번호
    UserID = testValue.testUserID

    result = cashbillService.sendFAX(testValue.testCorpNum,MgtKey,Sender,Receiver,UserID)
    
    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))