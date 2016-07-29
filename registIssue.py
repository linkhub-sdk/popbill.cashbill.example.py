# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Cashbill,CashbillService,PopbillException

cashbillService =  CashbillService(testValue.LinkID,testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 현금영수증 1건 즉시발행 "+ "=" * 15)

    # 즉시발행 메모
    Memo = "현금영수증 즉시발행 메모 테스트"

    # 현금영수즈 정보
    cashbill = Cashbill(mgtKey = "20160729-07", # 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
                        tradeType = "승인거래", # 현금영수증 형태, '승인거래'/'취소거래'
                        tradeUsage = "소득공제용", # 거래유형, '소득공제용'/'지출증빙용'
                        taxationType = "과세", # 과세형태, '과세'/'비과세'

                        # 거래처 식별번호
                        # 거래유형이 '지출증빙용' - [휴대폰/카드/주민등록/사업자] 번호 입력
                        # 거래유형이 '소득공제용' - [휴대폰/카드/주민등록] 번호 입력
                        # 자진발급 "010-000-1234" 의 경우 "소득공제용"으로만 발급 가능
                        identityNum = "4108600477", # 거래처 식별번호

                        franchiseCorpNum = "1234567890", # 발행자 사업자번호
                        franchiseCorpName = "발행자 상호",
                        franchiseCEOName = "발행 대표자 성명",
                        franchiseAddr = "발행자 주소",
                        franchiseTEL = "07075103710",

                        smssendYN = False, # SMS 전송 여부
                        customerName = "고객명",
                        itemName = "상품명",
                        orderNumber = "주문번호",
                        email = "test@test.com",
                        hp = "01043255117",
                        fax = "07075103710",

                        supplyCost = "15000", # 공급가액
                        tax = "5000", # 세액
                        serviceFee = "0", # 봉사료
                        totalAmount = "20000" # 거래금액, 공급가액+세액+봉사료
                        )

    result = cashbillService.registIssue(testValue.testCorpNum, cashbill, Memo, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
