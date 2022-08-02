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
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
삭제 가능한 상태의 현금영수증을 삭제합니다.
- ※ 삭제 가능한 상태: "임시저장", "발행취소", "전송실패"
- 현금영수증을 삭제하면 사용된 문서번호(mgtKey)를 재사용할 수 있습니다.
- https://docs.popbill.com/cashbill/python/api#Delete
'''

try:
    print("=" * 15 + " 현금영수증 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20220803-001"

    result = cashbillService.delete(CorpNum, MgtKey)
    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
