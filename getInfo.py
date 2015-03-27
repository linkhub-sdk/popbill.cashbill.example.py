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
    print("현금영수증 상태/요약 정보 확인")
    
    MgtKey = "20150326-01" # 현금영수증 문서관리번호
 
    cashbillInfo = cashbillService.getInfo(testValue.testCorpNum,MgtKey)

    print ("itemKey : %s" % (cashbillInfo.itemKey))
    print ("mgtKey : %s" % (cashbillInfo.mgtKey))
    print ("tradeDate : %s" % (cashbillInfo.tradeDate))
    print ("issueDT : %s" % (cashbillInfo.issueDT))
    print ("regDT : %s" % (cashbillInfo.regDT))
    print ("taxationType : %s" % (cashbillInfo.taxationType))
    print ("totalAmount : %s" % (cashbillInfo.totalAmount))
    print ("tradeUsage : %s" % (cashbillInfo.tradeUsage))
    print ("tradeType : %s" % (cashbillInfo.tradeType))
    print ("identityNum : %s" % (cashbillInfo.identityNum))
    print ("itemName : %s" % (cashbillInfo.itemName))
    print ("customerName : %s" % (cashbillInfo.customerName))
    print ("stateCode : %s" % (cashbillInfo.stateCode))
    print ("stateDT : %s" % (cashbillInfo.stateDT))
    print ("printYN : %s" % (cashbillInfo.printYN))

    ''' CashbillInfo 구성 : 항목별 자세한 내용은 "현금영수증 API 연동매뉴얼 > [4.2 현금영수증 상태정보 구성]" 참조.'''
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))