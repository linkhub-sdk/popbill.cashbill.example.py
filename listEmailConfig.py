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
현현금영수증 관련 메일 항목에 대한 발송설정을 확인합니다.
- https://docs.popbill.com/cashbill/python/api#ListEmailConfig
'''

try:
    print("=" * 15 + " 현금영수증 메일전송여부 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    EmailConfig = cashbillService.listEmailConfig(CorpNum)

    for info in EmailConfig:
        if info.emailType == "CSH_ISSUE":
            print("%s(고객에게 현금영수증이 발행 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "CSH_CANCEL":
            print("%s(고객에게 현금영수증이 발행취소 되었음을 알려주는 메일 전송 여부) : %s" % (info.emailType, info.sendYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
