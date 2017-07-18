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
    MgtKeyList.append("20170718-04")
    MgtKeyList.append("20161118-02")
    MgtKeyList.append("20161118-03")

    InfoList = cashbillService.getInfos(CorpNum, MgtKeyList)

    for cashbillInfo in InfoList:
        print ("itemKey (아이템키) : %s" % (cashbillInfo.itemKey))
        print ("mgtKey (문서관리번호) : %s" % (cashbillInfo.mgtKey))
        print ("tradeDate (거래일자) : %s" % (cashbillInfo.tradeDate))
        print ("issueDT (발행일시) : %s" % (cashbillInfo.issueDT))
        print ("regDT (등록일시) : %s" % (cashbillInfo.regDT))
        print ("taxationType (과세형태) : %s" % (cashbillInfo.taxationType))
        print ("totalAmount (거래금액) : %s" % (cashbillInfo.totalAmount))
        print ("tradeUsage (거래용도) : %s" % (cashbillInfo.tradeUsage))
        print ("tradeType (현금영수증형태) : %s" % (cashbillInfo.tradeType))
        print ("stateCode (상태코드) : %s" % (cashbillInfo.stateCode))
        print ("stateDT (상태변경일시) : %s" % (cashbillInfo.stateDT))

        print ("identityNum (거래처 식별번호) : %s" % (cashbillInfo.identityNum))
        print ("itemName (상품명) : %s" % (cashbillInfo.itemName))
        print ("customerName (고객명) : %s" % (cashbillInfo.customerName))

        print ("confirmNum (국세청 승인번호) : %s" % (cashbillInfo.confirmNum))
        print ("ntssendDT (국세청 전송일시) : %s" % (cashbillInfo.ntssendDT))
        print ("ntsresultDT (국세청 처리결과 수신일시) : %s" % (cashbillInfo.ntsresultDT))
        print ("ntsresultCode (국세청 처리결과 상태코드) : %s" % (cashbillInfo.ntsresultCode))
        print ("customerName (고객명) : %s" % (cashbillInfo.customerName))
        print ("orgConfirmNum (원본 현금영수증 국세청 승인번호) : %s" % (cashbillInfo.orgConfirmNum))
        print ("orgTradeDate (원본 현금영수증 거래일자) : %s" % (cashbillInfo.orgTradeDate))

        print ("printYN (인쇄여부) : %s\n" % (cashbillInfo.printYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
