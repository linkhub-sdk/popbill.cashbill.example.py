# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
[발행완료] 상태의 현금영수증을 [발행취소] 합니다.
- 발행취소는 현금영수증을 국세청 신고하기 전까지만 가능하며, 신고된 현금영수증을 취소하기 위해서는 취소현금영수증을 발행해야 합니다.
- 발행취소된 현금영수증에 사용된 문서관리번호를 재사용 하기 위해서는 삭제(Delete API)를 호출하여 해당 현금영수증을 삭제해야 합니다.
'''

try:
    print("=" * 15 + " 현금영수증 발행취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20190116-001"

    # 메모
    Memo = "발행취소 메모"

    result = cashbillService.cancelIssue(CorpNum, MgtKey, Memo)
    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
