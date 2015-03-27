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
    print("현금영수증 상세정보 확인")
    
    MgtKey = "20150326-01" #현금영수증 문서관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
 
    #현금영수증 임시저장시 구성한 정보를 반환한다.
    cashbill = cashbillService.getDetailInfo(testValue.testCorpNum,MgtKey)

    print ("mgtKey : %s" % (cashbill.mgtKey))
    print ("orgConfirmNum : %s" % (cashbill.orgConfirmNum))
    print ("tradeDate : %s" % (cashbill.tradeDate))
    print ("tradeUsage : %s" % (cashbill.tradeUsage))
    print ("tradeType : %s" % (cashbill.tradeType))
    print ("taxationType : %s" % (cashbill.taxationType))
    print ("supplyCost : %s" % (cashbill.supplyCost))
    print ("tax : %s" % (cashbill.tax))
    print ("serviceFee : %s" % (cashbill.serviceFee))
    print ("totalAmount : %s" % (cashbill.totalAmount))
    
    print ("franchiseCorpNum : %s" % (cashbill.franchiseCorpNum))
    print ("franchiseCorpName : %s" % (cashbill.franchiseCorpName))
    print ("franchiseCEOName : %s" % (cashbill.franchiseCEOName))
    print ("franchiseAddr : %s" % (cashbill.franchiseAddr))
    print ("franchiseTEL : %s" % (cashbill.franchiseTEL))

    print ("identityNum : %s" % (cashbill.identityNum))
    print ("customerName : %s" % (cashbill.customerName))
    print ("itemName : %s" % (cashbill.itemName))
    print ("orderNumber : %s" % (cashbill.orderNumber))
    print ("email : %s" % (cashbill.email))
    print ("hp : %s" % (cashbill.hp))
    print ("fax : %s" % (cashbill.fax))

    print ("smssendYN : %s" % (cashbill.smssendYN))
    print ("faxsendYN : %s" % (cashbill.faxsendYN))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))