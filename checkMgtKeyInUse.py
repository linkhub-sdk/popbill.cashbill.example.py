# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService =  CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

'''
현금영수증 관리번호 중복여부를 확인합니다.
- 관리번호는 1~24자리로 숫자, 영문 '-', '_' 조합으로 구성할 수 있습니다.
'''

try:
    print("=" * 15 + " 문서관리번호 사용여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 현금영수증 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
    MgtKey = "20161118-01"

    bIsInUse = cashbillService.checkMgtKeyInUse(CorpNum, MgtKey)

    print("사용여부 : %s" % "사용중" if bIsInUse else '미사용중')

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
