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
1건의 취소현금영수증을 임시저장 합니다.
- [임시저장] 상태의 현금영수증은 발행(Issue API)을 호출해야만 국세청에 전송됩니다.
- https://docs.popbill.com/cashbill/python/api#RevokeRegister
'''

try:
    print("=" * 15 + " 취소현금영수증 1건 임시저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    mgtKey = "20190117-001"

    # 원본현금영수증 국세청승인번호, 문서정보확인(GetInfo API)로 확인가능
    orgConfirmNum = "538588735"

    # 원본현금영수증 거래일자, 문서정보확인(GetInfo API)로 확인가능
    orgTradeDate = "20190116"

    # 발행안내문자 전송여부
    smssendYN = False

    result = cashbillService.revokeRegister(CorpNum, mgtKey, orgConfirmNum, orgTradeDate, smssendYN, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
