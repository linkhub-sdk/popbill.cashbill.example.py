# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Cashbill, CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

'''
1건의 현금영수증을 임시저장 합니다.
- [임시저장] 상태의 현금영수증은 발행(Issue API)을 호출해야만 국세청에 전송됩니다.
- 발행일 기준 오후 5시 이전에 발행된 현금영수증은 다음날 오후 2시에 국세청 전송결과를 확인할 수 있습니다.
- 현금영수증 국세청 전송 정책에 대한 정보는 "[현금영수증 API 연동매뉴얼] > 1.4. 국세청 전송정책"을
  참조하시기 바랍니다.
- 취소현금영수증 작성방법 안내 - http://blog.linkhub.co.kr/702
'''

try:
    print("=" * 15 + " 현금영수증 임시저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 정보
    cashbill = Cashbill (

        # 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
        mgtKey = "20161123-03",

        # 현금영수증 형태, '승인거래'/'취소거래'
        tradeType = "승인거래",

        # [취소거래시 필수] 원본 현금영수증 국세청승인번호
        orgConfirmNum = "",

        # [취소거래시 필수] 원본 현금영수증 거래일자
        orgTradeDate = "",

        # 과세형태, '과세'/'비과세'
        taxationType = "과세",

        # 거래유형, '소득공제용'/'지출증빙용'
        tradeUsage = "소득공제용",

        # 거래처 식별번호
        # 거래유형이 '지출증빙용' - [휴대폰/카드/주민등록/사업자] 번호 입력
        # 거래유형이 '소득공제용' - [휴대폰/카드/주민등록] 번호 입력
        # 자진발급 "010-000-1234" 의 경우 "소득공제용"으로만 발급 가능
        identityNum = "0100001234",

        # 공급가액
        supplyCost = "15000",

        # 세액
        tax = "5000",
        # 봉사료
        serviceFee = "0",

        # 거래금액, 공급가액+세액+봉사료
        totalAmount = "20000",


        # 발행자 사업자번호
        franchiseCorpNum = "1234567890",

        # 발행자 상호
        franchiseCorpName = "발행자 상호",

        # 발행자 대표자성명
        franchiseCEOName = "발행 대표자 성명",

        # 발행자 주소
        franchiseAddr = "발행자 주소",

        # 발행자 연락처
        franchiseTEL = "07043042991",


        # 고객명
        customerName = "고객명",

        # 상품명
        itemName = "상품명",

        # 주문번호
        orderNumber = "주문번호",

        # 고객 메일주소
        email = "test@test.com",

        # 고객 휴대폰번호
        hp = "01043255117",

        # 발행안내문자 전송여부
        smssendYN = False
    )

    result = cashbillService.register(CorpNum, cashbill)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
