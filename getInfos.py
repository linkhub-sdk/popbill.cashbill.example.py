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
다수건의 현금영수증 상태/요약 정보를 확인합니다. (최대 1000건)
- 응답항목에 대한 자세한 정보는 "[현금영수증 API 연동매뉴얼] > 4.2.
  현금영수증 상태정보 구성"을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 현금영수증 상태/요약 정보 확인(대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호 배열, 최대 1000건
    MgtKeyList = []
    MgtKeyList.append("20161118-01")
    MgtKeyList.append("20161118-02")
    MgtKeyList.append("20161118-03")

    InfoList = cashbillService.getInfos(CorpNum, MgtKeyList)

    for info in InfoList:
        print("info : %s" % info.mgtKey)
        for key, value in info.__dict__.items():
            if not key.startswith("__"):
                print("     %s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
