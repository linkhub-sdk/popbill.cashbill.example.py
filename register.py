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

from popbill import Cashbill, CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
1건의 현금영수증을 임시저장 합니다.
- [임시저장] 상태의 현금영수증은 발행(Issue API)을 호출해야만 국세청에 전송됩니다.
- https://docs.popbill.com/cashbill/python/api#Register
'''

try:
    print("=" * 15 + " 현금영수증 임시저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 정보
    cashbill = Cashbill(

        # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
        mgtKey="20190116-001",

        # 문서형태, '승인거래'/'취소거래'
        tradeType="승인거래",

        # [취소거래시 필수] 원본 현금영수증 국세청승인번호
        orgConfirmNum="",

        # [취소거래시 필수] 원본 현금영수증 거래일자
        orgTradeDate="",

        # 과세형태, '과세'/'비과세'
        taxationType="과세",

        # 거래유형, '일반'/'도서공연'/'대중교통'
        tradeOpt="일반",

        # 거래구분, '소득공제용'/'지출증빙용'
        tradeUsage="소득공제용",

        # 거래처 식별번호
        # 거래유형이 '지출증빙용' - [휴대폰/카드/주민등록/사업자] 번호 입력
        # 거래유형이 '소득공제용' - [휴대폰/카드/주민등록] 번호 입력
        # 자진발급 "010-000-1234" 의 경우 "소득공제용"으로만 발급 가능
        identityNum="0100001234",

        # 공급가액
        supplyCost="15000",

        # 부가세
        tax="5000",

        # 봉사료
        serviceFee="0",

        # 거래금액, 공급가액+세액+봉사료
        totalAmount="20000",

        # 가맹점 사업자번호
        franchiseCorpNum=CorpNum,

        # 가맹점 상호
        franchiseCorpName="가맹점 상호",

        # 가맹점 대표자성명
        franchiseCEOName="가맹점 대표자 성명",

        # 가맹점 주소
        franchiseAddr="가맹점 주소",

        # 가맹점 연락처
        franchiseTEL="07043042991",

        # 주문자명
        customerName="고객명",

        # 주문상품명
        itemName="상품명",

        # 주문번호
        orderNumber="주문번호",

        # 이메일
        # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
        # 실제 거래처의 메일주소가 기재되지 않도록 주의
        email="test@test.com",

        # 휴대폰
        hp="010111222",

        # 발행안내문자 전송여부
        smssendYN=False
    )

    result = cashbillService.register(CorpNum, cashbill)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
