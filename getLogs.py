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

try:
    print("=" * 15 + " 현금영수증 상태변경 이력 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20190116-001"

    LogList = cashbillService.getLogs(CorpNum, MgtKey)

    i = 1
    for f in LogList:
        print("%d:" % i)
        print("    docLogType(이력유형) : %s" % f.docLogType)
        print("    log(문서이력 설명) : %s" % f.log)
        print("    procType(처리유형) : %s" % f.procType)
        print("    procCorpName(회사명) : %s" % f.procCorpName)
        print("    procMemo(처리메모) : %s" % f.procMemo)
        print("    regDT(처리일시) : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
