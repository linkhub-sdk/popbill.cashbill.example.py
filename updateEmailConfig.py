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
현금영수증 관련 메일전송 항목에 대한 전송여부를 수정합니다.
- https://docs.popbill.com/cashbill/python/api#UpdateEmailConfig

메일전송유형
CSH_ISSUE : 고객에게 현금영수증이 발행 되었음을 알려주는 메일 입니다.
CSH_CANCEL : 고객에게 현금영수증이 발행취소 되었음을 알려주는 메일 입니다.
'''

try:
    print("=" * 15 + " 현금영수증 메일전송여부 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 메일 전송 유형
    EmailType = 'CSH_ISSUE'

    # 전송 여부 (True = 전송, False = 미전송)
    SendYN = True

    result = cashbillService.updateEmailConfig(CorpNum, EmailType, SendYN)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
