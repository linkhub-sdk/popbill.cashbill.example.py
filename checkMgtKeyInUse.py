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
파트너가 현금영수증 관리 목적으로 할당하는 문서번호 사용여부를 확인합니다.
- 이미 사용 중인 문서번호는 중복 사용이 불가하고, 현금영수증이 삭제된 경우에만 문서번호의 재사용이 가능합니다.
- https://developers.popbill.com/reference/cashbill/python/api/info#CheckMgtKeyInUse
'''

try:
    print("=" * 15 + " 문서번호 사용여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
    MgtKey = "20220803-001"

    bIsInUse = cashbillService.checkMgtKeyInUse(CorpNum, MgtKey)

    print("사용여부 : 사용중" if bIsInUse else "사용여부 : 미사용중")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
