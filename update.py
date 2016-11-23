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
1건의 현금영수증을 수정합니다.
- [임시저장] 상태의 현금영수증만 수정할 수 있습니다.
- 국세청에 신고된 현금영수증은 수정할 수 없으며, 취소 현금영수증을 발행하여 취소처리 할 수 있습니다.
- 취소현금영수증 작성방법 안내 - http://blog.linkhub.co.kr/702
'''

try:
    print("=" * 15 + " 현금영수증 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 수정하고자하는 현금영수증 문서관리번호
    MgtKey = '20161123-03'

    # 현금영수증 정보
    cashbill = Cashbill (

        # 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
        mgtKey = "20161123-01",

        # 현금영수증 형태, '승인거래'/'취소거래'
        tradeType = "승인거래",

        # 과세형태, '과세'/'비과세'
        taxationType = "과세",

        # 거래유형, '소득공제용'/'지출증빙용'
        tradeUsage = "지출증빙용",

        # 거래처 식별번호
        # 거래유형이 '지출증빙용' - [휴대폰/카드/주민등록/사업자] 번호 입력
        # 거래유형이 '소득공제용' - [휴대폰/카드/주민등록] 번호 입력
        # 자진발급 "010-000-1234" 의 경우 "소득공제용"으로만 발급 가능
        identityNum = "6798700433",

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
        franchiseCorpName = "발행자 상호_수정",

        # 발행자 대표자성명
        franchiseCEOName = "발행 대표자 성명_수정",

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
        hp = "010111222",

        # 발행안내문자 전송여부
        smssendYN = False
    )

    result = cashbillService.update(CorpNum, MgtKey, cashbill)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
