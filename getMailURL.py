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
현금영수증 안내메일의 상세보기 링크 URL을 반환합니다.
- 함수 호출로 반환 받은 URL에는 유효시간이 없습니다.
- https://docs.popbill.com/cashbill/python/api#GetMailURL
'''

try:
    print("=" * 15 + " 현금영수증 메일링크 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20220803-001"

    url = cashbillService.getMailURL(CorpNum, MgtKey)

    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
