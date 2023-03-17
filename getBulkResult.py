# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import CashbillService, PopbillException

cashbillService = CashbillService(testValue.LinkID, testValue.SecretKey)
cashbillService.IsTest = testValue.IsTest
cashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
cashbillService.UseStaticIP = testValue.UseStaticIP
cashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
접수시 기재한 SubmitID를 사용하여 현금영수증 접수결과를 확인합니다.
- 개별 현금영수증 처리상태는 접수상태(txState)가 완료(2) 시 반환됩니다.
- https://developers.popbill.com/reference/cashbill/python/api/issue#GetBulkResult
"""

try:
    print("=" * 15 + " 현금영수증 초대량 접수결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 제출아이디
    # 최대 36자리 영문, 숫자, '-' 조합으로 구성
    submitID = "PYTHON-BULK"

    bulkCashbillResult = cashbillService.getBulkResult(CorpNum, submitID)

    print("code (요청에 대한 응답 상태코드) : %s " % bulkCashbillResult.code)
    print("message (요청에 대한 응답 메시지) : %s " % bulkCashbillResult.message)
    print("submitID (제출아이디) : %s " % bulkCashbillResult.submitID)
    print("submitCount (현금영수증 접수 건수) : %s " % bulkCashbillResult.submitCount)
    print("successCount (현금영수증 발행 성공 건수) : %s " % bulkCashbillResult.successCount)
    print("failCount (현금영수증 발행 실패 건수) : %s " % bulkCashbillResult.failCount)
    print("txState (접수상태코드) : %s " % bulkCashbillResult.txState)
    print("txResultCode (접수 결과코드) : %s " % bulkCashbillResult.txResultCode)
    print("txStartDT (발행처리 시작일시) : %s " % bulkCashbillResult.txStartDT)
    print("txEndDT (발행처리 완료일시) : %s " % bulkCashbillResult.txEndDT)
    print("receiptDT (접수일시) : %s " % bulkCashbillResult.receiptDT)
    print("receiptID (접수아이디) : %s " % bulkCashbillResult.receiptID)

    print("=" * 15 + " issueResult (발행결과) " + "=" * 15)
    for bulkCashbillIssueResult in bulkCashbillResult.issueResult:
        print("code (응답코드) : %s " % bulkCashbillIssueResult.code)
        print("message (응답메시지) : %s " % bulkCashbillIssueResult.message)
        print("mgtKey (문서번호) : %s " % bulkCashbillIssueResult.mgtKey)
        print("confirmNum (국세청승인번호) : %s " % bulkCashbillIssueResult.confirmNum)
        print("tradeDate (거래일자) : %s " % bulkCashbillIssueResult.tradeDate)
        print("issueDT (발행일시) : %s " % bulkCashbillIssueResult.issueDT)
        print("*" * 50)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
