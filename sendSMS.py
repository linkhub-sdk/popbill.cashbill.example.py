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
    print("현금영수증 알림문자 전송")

    MgtKey = "20150326-01" # 현금영수증 문서관리번호
    Sender = "07075103710" # 발신번호
    Receiver = "010111222" # 수신번호
    Contents = "현금영수증 문자메시지 전송 테스트" # 메시지내용, 메시지 길이가 90Byte 초과시 길이가 조정되어 전송됨
    UserID = testValue.testUserID

    result = cashbillService.sendSMS(testValue.testCorpNum,MgtKey,Sender,Receiver,Contents,UserID)
    
    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))