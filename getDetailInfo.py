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

    print ("mgtKey (현금영수증 문서관리번호) : %s" % (cashbill.mgtKey))
    print ("confirmNum (국세청승인번호) : %s" % (cashbill.confirmNum))
    print ("tradeDate (거래일자): %s" % (cashbill.tradeDate))
    print ("tradeUsage (거래유형) : %s" % (cashbill.tradeUsage))
    print ("tradeType (현금영수증 형태) : %s" % (cashbill.tradeType))
    print ("taxationType (과세형태) : %s" % (cashbill.taxationType))
    print ("supplyCost (공급가액) : %s" % (cashbill.supplyCost))
    print ("tax (세액) : %s" % (cashbill.tax))
    print ("serviceFee (봉사료) : %s" % (cashbill.serviceFee))
    print ("totalAmount (거래금액) : %s" % (cashbill.totalAmount))

    print ("franchiseCorpNum (발행자 사업자번호) : %s" % (cashbill.franchiseCorpNum))
    print ("franchiseCorpName (발행자 상호) : %s" % (cashbill.franchiseCorpName))
    print ("franchiseCEOName (발행자 대표자 성명) : %s" % (cashbill.franchiseCEOName))
    print ("franchiseAddr (발행자 주소) : %s" % (cashbill.franchiseAddr))
    print ("franchiseTEL (발행자 연락처) : %s" % (cashbill.franchiseTEL))

    print ("identityNum (거래처 식별번호) : %s" % (cashbill.identityNum))
    print ("customerName (고객명) : %s" % (cashbill.customerName))
    print ("itemName (상품명) : %s" % (cashbill.itemName))
    print ("orderNumber (주문번호) : %s" % (cashbill.orderNumber))
    print ("email (고객 이메일) : %s" % (cashbill.email))
    print ("hp (고객 휴대폰번호) : %s" % (cashbill.hp))
    print ("smssendYN (알림문자 전송여부) : %s" % (cashbill.smssendYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
