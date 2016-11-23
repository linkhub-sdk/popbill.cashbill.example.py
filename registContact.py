# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import ContactInfo, CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

'''
연동회원의 담당자를 신규로 등록합니다.
'''

try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    newContact = ContactInfo (

        # 아이디
        id = "testkorea_1117",

        # 비밀번호
        pwd = "thisispassword",

        # 담당자명
        personName = "정대리",

        # 연락처
        tel = "010-4304-2991",

        # 휴대폰번호
        hp = "010-4304-2991",

        # 팩스번호
        fax = "070-4324-2991",

        # 메일주소
        email = "dev@linkhub.co.kr",

        # 회사조회 권한여부, True(회사조회) False(개인조회)
        searchAllAllowYN = True
    )

    result = cashbillService.registContact(CorpNum, newContact, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))