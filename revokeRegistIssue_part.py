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
1건의 (부분) 취소현금영수증을 즉시발행합니다.
- 발행일 기준 오후 5시 이전에 발행된 현금영수증은 다음날 오후 2시에 국세청 전송결과를 확인할 수 있습니다.
- https://docs.popbill.com/cashbill/python/api#RevokeRegistIssue
'''

try:
    print("=" * 15 + " 취소현금영수증 1건 즉시발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    mgtKey = "20190117-002"

    # 원본현금영수증 국세청승인번호, 문서정보확인(GetInfo API)로 확인가능
    orgConfirmNum = "538588735"

    # 원본현금영수증 거래일자, 문서정보확인(GetInfo API)로 확인가능
    orgTradeDate = "20190116"

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

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
