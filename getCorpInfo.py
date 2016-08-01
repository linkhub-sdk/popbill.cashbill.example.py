# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService,PopbillException

cashbillService =  CashbillService(testValue.LinkID,testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 회사정보 확인 " + "=" * 15)

    ''' CorpInfo 구성
                ceoname     (대표자 성명)
                corpName    (상호)
                addr        (주소)
                bizType     (업태)
                bizClass    (종목)
    '''

    response = cashbillService.getCorpInfo(testValue.testCorpNum, testValue.testUserID)

    tmp = "ceonaem : " + response.ceoname + "\n"
    tmp += "corpName : " + response.corpName + "\n"
    tmp += "addr : " + response.addr + "\n"
    tmp += "bizType : " + response.bizType + "\n"
    tmp += "bizClass : " + response.bizClass + "\n"
    print(tmp);

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
