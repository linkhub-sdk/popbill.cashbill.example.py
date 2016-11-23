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
1건의 현금영수증 상태/요약 정보를 확인합니다.
- 응답항목에 대한 자세한 정보는 "[현금영수증 API 연동매뉴얼] > 4.2. 현금영수증 상태정보 구성"을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 현금영수증 상태/요약 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20161118-01"

    cashbillInfo = cashbillService.getInfo(CorpNum, MgtKey)

    print ("itemKey : %s" % (cashbillInfo.itemKey))
    print ("mgtKey : %s" % (cashbillInfo.mgtKey))
    print ("tradeDate : %s" % (cashbillInfo.tradeDate))
    print ("issueDT : %s" % (cashbillInfo.issueDT))
    print ("regDT : %s" % (cashbillInfo.regDT))
    print ("taxationType : %s" % (cashbillInfo.taxationType))
    print ("totalAmount : %s" % (cashbillInfo.totalAmount))
    print ("tradeUsage : %s" % (cashbillInfo.tradeUsage))
    print ("tradeType : %s" % (cashbillInfo.tradeType))
    print ("identityNum : %s" % (cashbillInfo.identityNum))
    print ("itemName : %s" % (cashbillInfo.itemName))
    print ("customerName : %s" % (cashbillInfo.customerName))
    print ("stateCode : %s" % (cashbillInfo.stateCode))
    print ("stateDT : %s" % (cashbillInfo.stateDT))
    print ("printYN : %s" % (cashbillInfo.printYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
