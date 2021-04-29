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
다수건의 현금영수증 인쇄팝업 URL을 반환합니다. (최대 100건)
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
- https://docs.popbill.com/cashbill/python/api#GetMassPrintURL
'''

try:
    print("=" * 15 + " 현금영수증 인쇄 팝업 URL(대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문서번호 배열, 최대 100건
    MgtKeyList = []
    MgtKeyList.append("20190116-001")
    MgtKeyList.append("20190116-002")
    MgtKeyList.append("20190116-003")

    url = cashbillService.getMassPrintURL(CorpNum, MgtKeyList)

    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
