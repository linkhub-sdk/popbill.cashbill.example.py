# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

'''
발행 안내메일을 재전송합니다.
'''

try:
    print("=" * 15 + " 현금영수증 안내메일 재전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20161123-01"

    # 수신 메일주소
    Receiver = "test@test.com"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = cashbillService.sendEmail(CorpNum, MgtKey, Receiver, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
