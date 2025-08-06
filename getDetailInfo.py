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
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
현금영수증 1건의 상세정보를 확인합니다.
- https://developers.popbill.com/reference/cashbill/python/api/info#GetDetailInfo
"""

try:
    print("=" * 15 + " 현금영수증 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20220803-001"

    cashbill = cashbillService.getDetailInfo(CorpNum, MgtKey)

    print("mgtKey (문서번호) : %s" % cashbill.mgtKey)
    print("confirmNum (국세청승인번호) : %s" % cashbill.confirmNum)
    print("orgConfirmNum (당초 승인 현금영수증 국세청승인번호) : %s" % cashbill.orgConfirmNum)
    print("orgTradeDate (당초 승인 현금영수증 거래일자) : %s" % cashbill.orgTradeDate)
    print("tradeDate (거래일자): %s" % cashbill.tradeDate)
    print("tradeDT (거래일시): %s" % cashbill.tradeDT)
    print("tradeType (문서형태) : %s" % cashbill.tradeType)
    print("tradeUsage (거래구분) : %s" % cashbill.tradeUsage)
    print("tradeOpt (거래유형) : %s" % cashbill.tradeOpt)

    print("taxationType (과세형태) : %s" % cashbill.taxationType)
    print("totalAmount (거래금액) : %s" % cashbill.totalAmount)
    print("supplyCost (공급가액) : %s" % cashbill.supplyCost)
    print("tax (부가세) : %s" % cashbill.tax)
    print("serviceFee (봉사료) : %s" % cashbill.serviceFee)

    print("franchiseCorpNum (가맹점 사업자번호) : %s" % cashbill.franchiseCorpNum)
    print("franchiseTaxRegID (가맹점 종사업장 식별번호) : %s" % cashbill.franchiseTaxRegID)
    print("franchiseCorpName (가맹점 상호) : %s" % cashbill.franchiseCorpName)
    print("franchiseCEOName (가맹점 대표자 성명) : %s" % cashbill.franchiseCEOName)
    print("franchiseAddr (가맹점 주소) : %s" % cashbill.franchiseAddr)
    print("franchiseTEL (가맹점 연락처) : %s" % cashbill.franchiseTEL)

    print("identityNum (식별번호) : %s" % cashbill.identityNum)
    print("customerName (구매자 성명) : %s" % cashbill.customerName)
    print("itemName (주문상품명) : %s" % cashbill.itemName)
    print("orderNumber (주문번호) : %s" % cashbill.orderNumber)
    print("email (구매자 메일) : %s" % cashbill.email)
    print("hp (구매자 휴대폰) : %s" % cashbill.hp)

    print("smssendYN (SMS 전송여부) : %s" % cashbill.smssendYN)
    print("cancelType (취소사유) : %s" % cashbill.cancelType)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
