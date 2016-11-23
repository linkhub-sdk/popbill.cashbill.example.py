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
[발행완료] 상태의 현금영수증을 [발행취소] 합니다.
- 발행취소는 국세청 전송전에만 가능합니다.
- 발행취소된 형금영수증은 국세청에 전송되지 않습니다.
'''

try:
    print("=" * 15 + " 현금영수증 발행취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20150326-01"

    # 메모
    Memo = "발행취소 메모"

    result = cashbillService.cancelIssue(CorpNum, MgtKey, Memo)
    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
