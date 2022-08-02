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
1건의 취소현금영수증을 즉시발행합니다.
- 현금영수증 국세청 전송 정책 : https://docs.popbill.com/cashbill/ntsSendPolicy?lang=python
- https://docs.popbill.com/cashbill/python/api#RevokeRegistIssue
'''

try:
    print("=" * 15 + " 취소현금영수증 1건 즉시발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    mgtKey = "20220803-003"

    # 원본현금영수증 국세청승인번호, 문서정보확인(GetInfo API)로 확인가능
    orgConfirmNum = "TB0000253"

    # 원본현금영수증 거래일자, 문서정보확인(GetInfo API)로 확인가능
    orgTradeDate = "20220801"

    # 발행안내문자 전송여부
    smssendYN = False

    # 즉시발행 메모
    memo = "현금영수증 즉시발행 메모"

    result = cashbillService.revokeRegistIssue(CorpNum, mgtKey, orgConfirmNum, orgTradeDate, smssendYN, memo)

    print("처리결과 : [%d] %s" % (result.code, result.message))
    print("국세청 승인번호 : %s" % (result.confirmNum))
    print("거래일자 : %s" % (result.tradeDate))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
