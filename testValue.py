# -*- coding: utf-8 -*-

"""
팝빌 현금영수증 API Python SDK Example

Python 연동 튜토리얼 안내 : https://developers.popbill.com/guide/cashbill/python/getting-started/tutorial
연동 기술지원 연락처 : 1600-9854
연동 기술지원 이메일 : code@linkhubcorp.com

<테스트 연동개발 준비사항>
1) API Key 변경 (연동신청 시 메일로 전달된 정보)
    - LinkID : 링크허브에서 발급한 링크아이디
    - SecretKey : 링크허브에서 발급한 비밀키
2) SDK 환경설정 옵션 설정
    - IsTest : 연동환경 설정, true-테스트, false-운영(Production), (기본값:true)
    - IPRestrictOnOff : 인증토큰 IP 검증 설정, true-사용, false-미사용, (기본값:true)
    - UseStaticIP : 통신 IP 고정, true-사용, false-미사용, (기본값:false)
    - UseLocalTimeYN : 로컬시스템 시간 사용여부, true-사용, false-미사용, (기본값:true).
"""

# 링크아이디
LinkID = "TESTER"

# 비밀키
SecretKey = "SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I="

# 연동환경 설정, true-테스트, false-운영(Production), (기본값:true)
IsTest = True

# 인증토큰 IP 검증 설정, true-사용, false-미사용, (기본값:true)
IPRestrictOnOff = True

# 통신 IP 고정, true-사용, false-미사용, (기본값:false)
UseStaticIP = False

# 로컬시스템 시간 사용여부, true-사용, false-미사용, (기본값:true)
UseLocalTimeYN = True

# 테스트 회원 사업자번호
testCorpNum = "1234567890"

# 테스트 회원 팝빌 아아디
testUserID = "testkorea"
