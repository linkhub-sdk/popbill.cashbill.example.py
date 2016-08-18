# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService,PopbillException

cashbillService =  CashbillService(testValue.LinkID,testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 목록 조회 " + "=" * 15)

    # 조회 일자유형, R-등록일자, T-거래일자, I-발행일자
    DType = "R"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20160701"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20160831"

    #상태코드 배열, 2,3번째 자리에 와일드카드(*) 사용 가능
    State = ["3**", "4**"]

    # 현금영수증 형태, N-일반 현금영수증, C-취소 현금영수증
    TradeType = ["N", "C"]

    # 거래용도 배열, P-소득공제용, C-지출증빙용
    TradeUsage = ["P", "C"]

    # 과세형태 배열, T-과세, N-비과세
    TaxationType = ["T", "N"]

    # 페이지 번호
    Page = 1

    # 페이지당 목록개수
    PerPage = 10

    # 정렬방향, D-내림차순, A-오름차순
    Order = "D"

    # 현금영수증 식별번호, 미기재시 전체조회
    QString = ""

    response = cashbillService.search(testValue.testCorpNum, DType, SDate, EDate, State, TradeType, TradeUsage, TaxationType, Page, PerPage, Order, testValue.testUserID, QString)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list :
        print("====== 현금영수증 정보 [%d] ======"% i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print()

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
