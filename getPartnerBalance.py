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
    print("파트너 잔여포인트 확인")

    balance = cashbillService.getPartnerBalance(testValue.testCorpNum)

    print("회원잔액 : %f" % balance)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))