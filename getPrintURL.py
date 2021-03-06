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
1건의 현금영수증 인쇄(공급자) URL을 반환합니다.
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
- https://docs.popbill.com/cashbill/python/api#GetPrintURL
'''

try:
    print("=" * 15 + " 현금영수증 인쇄 팝업 URL(공급자용)" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20190116-001"

    url = cashbillService.getPrintURL(CorpNum, MgtKey)

    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
