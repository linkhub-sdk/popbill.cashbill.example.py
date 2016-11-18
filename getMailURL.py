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

'''
공급받는자 메일링크 URL을 반환합니다.
- 메일링크 URL은 유효시간이 존재하지 않습니다.
'''

try:
    print("=" * 15 + " 현금영수증 메일링크 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20161118-01"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    url = cashbillService.getMailURL(CorpNum, MgtKey, UserID)

    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
