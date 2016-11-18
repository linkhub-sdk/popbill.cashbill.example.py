# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService =  CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

'''
다수건의 현금영수증 인쇄팝업 URL을 반환합니다.
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
'''

try:
    print("=" * 15 + " 현금영수증 인쇄 팝업 URL(대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문서관리번호 배열, 최대 100건
    MgtKeyList = []
    MgtKeyList.append("20161118-01")
    MgtKeyList.append("20161118-02")
    MgtKeyList.append("20161118-03")

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    url = cashbillService.getMassPrintURL(testValue.testCorpNum,MgtKeyList,UserID)

    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
