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

from popbill import CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
현금영수증을 팩스전송합니다.
- 팩스 전송 요청시 포인트가 차감됩니다. (전송실패시 환불처리)
- 전송내역 확인은 [팝빌 로그인] > [문자 팩스] > [팩스] > [전송내역] 메뉴에서 전송결과를 확인할 수 있습니다.
- https://docs.popbill.com/cashbill/python/api#SendFAX
'''

try:
    print("=" * 15 + " 현금영수증 팩스 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20190117-001"

    # 발신번호
    Sender = "07043042991"

    # 수신팩스번호
    Receiver = "070111222"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = cashbillService.sendFAX(CorpNum, MgtKey, Sender, Receiver, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
