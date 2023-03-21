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
from popbill import Cashbill, CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
작성된 현금영수증 데이터를 팝빌에 저장과 동시에 발행하여 "발행완료" 상태로 처리합니다.
- 현금영수증 국세청 전송 정책 : https://developers.popbill.com/guide/cashbill/python/introduction/policy-of-send-to-nts
- https://developers.popbill.com/reference/cashbill/python/api/issue#RegistIssue
"""

try:
    print("=" * 15 + " 현금영수증 1건 즉시발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 정보
    cashbill = Cashbill(
        # 문서번호, 1~24자리, (영문,숫자,'-','_') 조합으로 사업자별 고유번호 생성
        mgtKey="20220803-001",

        # 문서형태, 승인거래 기재
        tradeType="승인거래",

        # 과세형태 (과세, 비과세) 중 기재
        taxationType="과세",

        # 거래유형 (일반, 도서공연, 대중교통) 중 기재
        # - 미입력시 기본값 "일반" 처리
        tradeOpt="일반",

        # 거래구분 (소득공제용, 지출증빙용) 중 기재
        tradeUsage="소득공제용",

        # 식별번호, 거래구분에 따라 작성
        # └ 소득공제용 - 주민등록/휴대폰/카드번호(현금영수증 카드)/자진발급용 번호(010-000-1234) 기재가능
        # └ 지출증빙용 - 사업자번호/주민등록/휴대폰/카드번호(현금영수증 카드) 기재가능
        # └ 주민등록번호 13자리, 휴대폰번호 10~11자리, 카드번호 13~19자리, 사업자번호 10자리 입력 가능
        identityNum="010-000-1234",

        # 공급가액
        supplyCost="10000",

        # 부가세
        tax="1000",

        # 봉사료
        serviceFee="0",

        # 거래금액, 공급가액+세액+봉사료
        totalAmount="11000",

        # 가맹점 사업자번호
        franchiseCorpNum=CorpNum,
        # 가맹점 종사업장 식별번호
        franchiseTaxRegID="",

        # 가맹점 상호
        franchiseCorpName="가맹점 상호",

        # 가맹점 대표자성명
        franchiseCEOName="가맹점 대표자 성명",

        # 가맹점 주소
        franchiseAddr="가맹점 주소",

        # 가맹점 연락처
        franchiseTEL="",

        # 주문자명
        customerName="고객명",

        # 주문상품명
        itemName="상품명",

        # 주문번호
        orderNumber="주문번호",

        # 이메일
        # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
        # 실제 거래처의 메일주소가 기재되지 않도록 주의
        email="",

        # 휴대폰
        hp="",

        # 발행안내문자 전송여부
        smssendYN=False,
        # 거래일시, 날짜(yyyyMMddHHmmss)
        # 당일, 전일만 가능, 미입력시 기본값 발행일시 처리
        tradeDT="20221108000000",
    )

    # 즉시발행 메모
    Memo = "현금영수증 즉시발행 메모"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 안내메일 제목, 공백처리시 기본양식으로 전송
    EmailSubject = ""

    result = cashbillService.registIssue(CorpNum, cashbill, Memo, UserID, EmailSubject)

    print("처리결과 : [%d] %s" % (result.code, result.message))
    print("국세청 승인번호 : %s" % (result.confirmNum))
    print("거래일자 : %s" % (result.tradeDate))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
