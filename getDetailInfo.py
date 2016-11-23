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
현금영수증 1건의 상세정보를 조회합니다.
- 응답항목에 대한 자세한 사항은 "[현금영수증 API 연동매뉴얼] > 4.1. 현금영수증 구성" 을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 현금영수증 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호
    MgtKey = "20161118-01"

    cashbill = cashbillService.getDetailInfo(CorpNum, MgtKey)

    print ("mgtKey : %s" % (cashbill.mgtKey))
    print ("orgConfirmNum : %s" % (cashbill.orgConfirmNum))
    print ("tradeDate : %s" % (cashbill.tradeDate))
    print ("tradeUsage : %s" % (cashbill.tradeUsage))
    print ("tradeType : %s" % (cashbill.tradeType))
    print ("taxationType : %s" % (cashbill.taxationType))
    print ("supplyCost : %s" % (cashbill.supplyCost))
    print ("tax : %s" % (cashbill.tax))
    print ("serviceFee : %s" % (cashbill.serviceFee))
    print ("totalAmount : %s" % (cashbill.totalAmount))

    print ("franchiseCorpNum : %s" % (cashbill.franchiseCorpNum))
    print ("franchiseCorpName : %s" % (cashbill.franchiseCorpName))
    print ("franchiseCEOName : %s" % (cashbill.franchiseCEOName))
    print ("franchiseAddr : %s" % (cashbill.franchiseAddr))
    print ("franchiseTEL : %s" % (cashbill.franchiseTEL))

    print ("identityNum : %s" % (cashbill.identityNum))
    print ("customerName : %s" % (cashbill.customerName))
    print ("itemName : %s" % (cashbill.itemName))
    print ("orderNumber : %s" % (cashbill.orderNumber))
    print ("email : %s" % (cashbill.email))
    print ("hp : %s" % (cashbill.hp))
    print ("fax : %s" % (cashbill.fax))

    print ("smssendYN : %s" % (cashbill.smssendYN))
    print ("faxsendYN : %s" % (cashbill.faxsendYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
