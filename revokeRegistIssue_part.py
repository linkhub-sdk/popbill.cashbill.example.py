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
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
작성된 (부분)취소 현금영수증 데이터를 팝빌에 저장과 동시에 발행하여 "발행완료" 상태로 처리합니다.
- 취소 현금영수증의 금액은 원본 금액을 넘을 수 없습니다.
- 현금영수증 국세청 전송 정책 [https://docs.popbill.com/cashbill/ntsSendPolicy?lang=python]
- "발행완료"된 취소 현금영수증은 국세청 전송 이전에 발행취소(cancelIssue API) 함수로 국세청 신고 대상에서 제외할 수 있습니다.
- 취소 현금영수증 발행 시 구매자 메일주소로 발행 안내 베일이 전송되니 유의하시기 바랍니다.
- https://docs.popbill.com/cashbill/python/api#RevokeRegistIssue
'''

try:
    print("=" * 15 + " 취소현금영수증 1건 즉시발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    mgtKey = "20220803-002"

    # 원본현금영수증 국세청승인번호, 문서정보확인(GetInfo API)로 확인가능
    orgConfirmNum = "TB0000253"

    # 원본현금영수증 거래일자, 문서정보확인(GetInfo API)로 확인가능
    orgTradeDate = "20220801"

    # 발행안내문자 전송여부
    smssendYN = False

    # 즉시발행 메모
    memo = "현금영수증 즉시발행 메모"

    # 부분취소여부, True-부분취소 / False-전체취소
    isPartCancel = True

    # 취소사유, 1-거래취소, 2-오류발급취소, 3-기타
    cancelType = 1

    # [취소] 공급가액
    supplyCost = "4000"

    # [취소] 세액
    tax = "400"

    # [취소] 봉사료
    serviceFee = "0"

    # [취소] 합계금액
    totalAmount = "4400"

    result = cashbillService.revokeRegistIssue(CorpNum, mgtKey, orgConfirmNum, orgTradeDate, smssendYN, memo, UserID,
                                               isPartCancel, cancelType, supplyCost, tax, serviceFee, totalAmount)

    print("처리결과 : [%d] %s" % (result.code, result.message))
    print("국세청 승인번호 : %s" % (result.confirmNum))
    print("거래일자 : %s" % (result.tradeDate))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
