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
검색조건을 사용하여 현금영수증 목록을 조회합니다. (조회기간 단위 : 최대 6개월)
- https://docs.popbill.com/cashbill/python/api#Search
'''

try:
    print("=" * 15 + " 현금영수증 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 조회 일자유형, R-등록일자, T-거래일자, I-발행일자
    DType = "R"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20211201"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20211230"

    # 상태코드 배열, 2,3번째 자리에 와일드카드(*) 사용 가능
    State = ["3**", "4**"]

    # 문서형태, N-일반 현금영수증, C-취소 현금영수증
    TradeType = ["N", "C"]

    # 거래구분 배열, P-소득공제용, C-지출증빙용
    TradeUsage = ["P", "C"]

    # 과세형태 배열, T-과세, N-비과세
    TaxationType = ["T", "N"]

    # 페이지번호, 기본값 ‘1’
    Page = 1

    # 페이지당 검색개수, 기본값 500, 최대 1000
    PerPage = 10

    # 정렬방향, D-내림차순, A-오름차순
    Order = "D"

    # 현금영수증 식별번호, 미기재시 전체조회
    QString = ""

    # 거래유형 배열, N-일반, B-도서공연, T-대중교통
    TradeOpt = ["N", "B", "T"]

    # 가맹점 종사업장 번호
    # └ 다수건 검색시 콤마(",")로 구분. 예) 1234,1000
    FranchiseTaxRegID = ""

    response = cashbillService.search(CorpNum, DType, SDate, EDate, State, TradeType,
                                      TradeUsage, TaxationType, Page, PerPage, Order, UserID, QString, TradeOpt, FranchiseTaxRegID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for cashbillInfo in response.list:
        print("\n==========현금영수증 정보==========>")
        print("itemKey (팝빌번호) : %s" % cashbillInfo.itemKey)
        print("mgtKey (문서번호) : %s" % cashbillInfo.mgtKey)
        print("tradeDate (거래일자) : %s" % cashbillInfo.tradeDate)
        print("tradeType (문서형태) : %s" % cashbillInfo.tradeType)
        print("tradeUsage (거래구분) : %s" % cashbillInfo.tradeUsage)
        print("tradeOpt (거래유형) : %s" % cashbillInfo.tradeOpt)
        print("taxationType (과세형태) : %s" % cashbillInfo.taxationType)
        print("totalAmount (거래금액) : %s" % cashbillInfo.totalAmount)
        print("issueDT (발행일시) : %s" % cashbillInfo.issueDT)
        print("regDT (등록일시) : %s" % cashbillInfo.regDT)
        print("stateMemo (상태메모) : %s" % cashbillInfo.stateMemo)
        print("stateCode (상태코드) : %s" % cashbillInfo.stateCode)
        print("stateDT (상태변경일시) : %s" % cashbillInfo.stateDT)

        print("\n거래처 정보>")
        print("identityNum (거래처 식별번호) : %s" % cashbillInfo.identityNum)
        print("itemName (주문상품명) : %s" % cashbillInfo.itemName)
        print("customerName (주문자명) : %s" % cashbillInfo.customerName)

        print("\n국세청 정보>")
        print("confirmNum (국세청 승인번호) : %s" % cashbillInfo.confirmNum)
        print("ntssendDT (국세청 전송일시) : %s" % cashbillInfo.ntssendDT)
        print("ntsresultDT (국세청 처리결과 수신일시) : %s" % cashbillInfo.ntsresultDT)
        print("ntsresultCode (국세청 처리결과 상태코드) : %s" % cashbillInfo.ntsresultCode)
        print("customerName (고객명) : %s" % cashbillInfo.customerName)
        print("orgConfirmNum (원본 현금영수증 국세청 승인번호) : %s" % cashbillInfo.orgConfirmNum)
        print("orgTradeDate (원본 현금영수증 거래일자) : %s" % cashbillInfo.orgTradeDate)

        print("\n부가 정보>")
        print("printYN (인쇄여부) : %s\n" % cashbillInfo.printYN)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
