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
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
현금영수증과 관련된 안내 SMS(단문) 문자를 재전송하는 함수로, 팝빌 사이트 [문자·팩스] > [문자] > [전송내역] 메뉴에서 전송결과를 확인 할 수 있습니다.
- 메시지는 최대 90byte까지 입력 가능하고, 초과한 내용은 자동으로 삭제되어 전송합니다. (한글 최대 45자)
- 알림문자 전송시 포인트가 차감됩니다. (전송실패시 환불처리)
- https://developers.popbill.com/reference/cashbill/python/api/etc#SendSMS
'''

try:
    print("=" * 15 + " 현금영수증 알림문자 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서번호
    MgtKey = "20220803-001"

    # 발신번호
    Sender = ""

    # 수신번호
    Receiver = ""

    # 메시지내용, 메시지 길이가 90Byte 초과시 길이가 조정되어 전송됨
    Contents = "현금영수증 문자메시지 전송 테스트"

    result = cashbillService.sendSMS(CorpNum, MgtKey, Sender, Receiver, Contents)
    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
