# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
팝빌 사이트를 통해 발행하여 문서번호가 할당되지 않은 현금영수증에 문서번호를 할당합니다.
- https://developers.popbill.com/reference/cashbill/python/api/etc#AssignMgtKey
"""

try:
    print("=" * 15 + " 현금영수증 문서번호 할당 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 현금영수증 아이템키, 문서 목록조회(Search) API의 반환항목중 ItemKey 참조
    ItemKey = "022071216010000001"

    # 할당할 문서번호, 숫자, 영문 '-', '_' 조합으로 1~24자리까지
    # 사업자번호별 중복없는 고유번호 할당
    MgtKey = "20220803-003"

    result = cashbillService.assignMgtKey(CorpNum, ItemKey, MgtKey)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
