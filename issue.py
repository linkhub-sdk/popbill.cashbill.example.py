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

'''
1건의 임시저장 현금영수증을 발행처리합니다.
- 발행일 기준 오후 5시 이전에 발행된 현금영수증은 다음날 오후 2시에 국세청 전송결과를 확인할 수 있습니다.
- 현금영수증 국세청 전송 정책에 대한 정보는 "[현금영수증 API 연동매뉴얼] > 1.4. 국세청 전송정책" 을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 현금영수증 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20190116-001"

    # 메모
    Memo = "발행 메모"

    result = cashbillService.issue(CorpNum, MgtKey, Memo)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
