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
현금영수증 상태에 대한 변경이력을 확인합니다.
- https://docs.popbill.com/cashbill/python/api#GetLogs
'''

try:
    print("=" * 15 + " 현금영수증 상태변경 이력 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20220803-001"

    LogList = cashbillService.getLogs(CorpNum, MgtKey)

    i = 1
    for f in LogList:
        print("%d:" % i)
        print("    docLogType(로그타입) : %s" % f.docLogType)
        print("    log(이력정보) : %s" % f.log)
        print("    procType(처리형태) : %s" % f.procType)
        print("    procMemo(처리메모) : %s" % f.procMemo)
        print("    regDT(등록일시) : %s" % f.regDT)
        print("    ip(아이피) : %s" % f.ip)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
