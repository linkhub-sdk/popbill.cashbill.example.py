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
    print("파트너 관리번호 사용여부 확인")
    
    MgtKey = "20150326-01" # 현금영수증 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성

    bIsInUse = cashbillService.checkMgtKeyInUse(testValue.testCorpNum,MgtKey)
    print("사용여부 : %s" % "사용중" if bIsInUse else '미사용중')
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))