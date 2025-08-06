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
다수건의 현금영수증 상태 및 요약 정보를 확인합니다. (1회 호출 시 최대 1,000건 확인 가능)
- 리턴값 'CashbillInfo'의 변수 'stateCode'를 통해 현금영수증의 상태코드를 확인합니다.
- 현금영수증 상태코드 : [https://developers.popbill.com/reference/cashbill/python/response-code#state-code]
- https://developers.popbill.com/reference/cashbill/python/api/info#GetInfos
"""

try:
    print("=" * 15 + " 현금영수증 상태/요약 정보 확인(대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호 배열, 최대 1000건
    MgtKeyList = []
    MgtKeyList.append("20250806-01")

    InfoList = cashbillService.getInfos(CorpNum, MgtKeyList)

    for cashbillInfo in InfoList:
        print("itemKey (팝빌 식별번호) : %s" % cashbillInfo.itemKey)
        print("mgtKey (문서번호) : %s" % cashbillInfo.mgtKey)
        print("tradeDate (거래일자) : %s" % cashbillInfo.tradeDate)
        print("tradeDT (거래일시) : %s" % cashbillInfo.tradeDT)
        print("tradeType (문서형태) : %s" % cashbillInfo.tradeType)
        print("tradeUsage (거래구분) : %s" % cashbillInfo.tradeUsage)
        print("tradeOpt (거래유형) : %s" % cashbillInfo.tradeOpt)
        print("taxationType (과세형태) : %s" % cashbillInfo.taxationType)

        print("totalAmount (거래금액) : %s" % cashbillInfo.totalAmount)
        print("supplyCost (공급가액) : %s" % cashbillInfo.supplyCost)
        print("tax (부가세) : %s" % cashbillInfo.tax)
        print("serviceFee (봉사료) : %s" % cashbillInfo.serviceFee)

        print("issueDT (발행일시) : %s" % cashbillInfo.issueDT)
        print("regDT (등록일시) : %s" % cashbillInfo.regDT)
        print("stateCode (상태코드) : %s" % cashbillInfo.stateCode)
        print("stateDT (상태변경일시) : %s" % cashbillInfo.stateDT)

        print("identityNum (식별번호) : %s" % cashbillInfo.identityNum)
        print("itemName (주문상품명) : %s" % cashbillInfo.itemName)
        print("orderNumber (주문번호) : %s" % cashbillInfo.orderNumber)
        print("email (구매자 메일) : %s" % cashbillInfo.email)
        print("hp (구매자 휴대폰) : %s" % cashbillInfo.hp)
        print("customerName (구매자 성명) : %s" % cashbillInfo.customerName)

        print("confirmNum (국세청 승인번호) : %s" % cashbillInfo.confirmNum)
        if cashbillInfo.tradeType == "취소거래":
            print("orgConfirmNum (당초 승인 현금영수증 국세청 승인번호) : %s" % cashbillInfo.orgConfirmNum)
            print("orgTradeDate (당초 승인 현금영수증 거래일자) : %s" % cashbillInfo.orgTradeDate)
        print("ntssendDT (국세청 전송일시) : %s" % cashbillInfo.ntssendDT)
        print("ntsresultDT (국세청 처리결과 수신일시) : %s" % cashbillInfo.ntsresultDT)
        print("ntsresultCode (국세청 결과코드) : %s" % cashbillInfo.ntsresultCode)
        print("ntsresultMessage (국세청 결과메시지) : %s" % cashbillInfo.ntsresultMessage)

        print("printYN (인쇄여부) : %s" % cashbillInfo.printYN)
        print("interOPYN (연동문서 여부) : %s" % cashbillInfo.interOPYN)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
