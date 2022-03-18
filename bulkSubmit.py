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

from popbill import CashbillService, PopbillException, Cashbill

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
최대 100건의 현금영수증 발행을 한번의 요청으로 접수합니다.
- https://docs.popbill.com/cashbill/python/api#BulkSubmit
"""

try:
    print("=" * 15 + " 현금영수증 초대량 발행 접수 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    #제출아이디
    #최대 36자리 영문, 숫자, '-' 조합으로 구성
    submitID = 'PYTHONSHELL001'

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 현금영수증 객체정보 리스트
    cashbillList = []
    for i in range(1, 101):
        cashbillList.append(
            Cashbill(
                # [필수] 문서번호, 1~24자리, (영문,숫자,'-','_') 조합으로 사업자별 고유번호 생성
                mgtKey=submitID + '-' + str(i),

                # [필수] 문서형태, [승인거래 / 취소거래]
                tradeType="승인거래",

                # [취소거래시 필수] 원본 현금영수증 국세청승인번호
                orgConfirmNum="",

                # [취소거래시 필수] 원본 현금영수증 거래일자
                orgTradeDate="",

                # [필수] 과세형태, [과세 / 비과세]
                taxationType="과세",

                # [필수] 거래유형, [일반 / 도서공연 / 대중교통]
                tradeOpt="일반",

                # [필수] 거래구분, [소득공제용 /지출증빙용]
                tradeUsage="소득공제용",

                # [필수] 거래처 식별번호
                # 거래유형이 '지출증빙용' - [휴대폰/카드/주민등록/사업자] 번호 입력
                # 거래유형이 '소득공제용' - [휴대폰/카드/주민등록] 번호 입력
                # 자진발급 "010-000-1234" 의 경우 "소득공제용"으로만 발급 가능
                identityNum="010-000-1234",

                # [필수] 공급가액
                supplyCost="10000",

                # [필수] 세액
                tax="1000",

                # 봉사료
                serviceFee="0",

                # [필수] 거래금액, 공급가액+세액+봉사료
                totalAmount="11000",

                # 가맹점 사업자번호
                franchiseCorpNum=CorpNum,

                # 가맹점 종사업장 식별번호
                franchiseTaxRegID="",

                # 가맹점 상호
                franchiseCorpName="가맹점 상호",

                # 가맹점 대표자성명
                franchiseCEOName="발행 대표자 성명",

                # 가맹점 주소
                franchiseAddr="가맹점 주소",

                # 가맹점 연락처
                franchiseTEL="07012345678",

                # 주문자명
                customerName="주문자명",

                # 주문상품명
                itemName="주문상품명",

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
        )

    bulkResponse = cashbillService.bulkSubmit(CorpNum, submitID, cashbillList, UserID)

    print("처리결과 : [%d] %s" % (bulkResponse.code, bulkResponse.message))
    print("접수번호 : %s" % (bulkResponse.receiptID))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
