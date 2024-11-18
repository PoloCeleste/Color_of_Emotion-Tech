'''
### Python 3.9 에서 작성.
### selenium, webdriver-manager, requests 모듈 설치 필요.

Gitlab Manage Ver 1.0
(Gitlab Create Ver 1.0, Gitlab Auto Clone Ver 2.0)

한 파일에서 두개의 기능 실행 가능
실습실 생성 또는 클론 둘 중 하나 실행하면 바로 종료
종료하려면 0 입력 필요



Gitlab Manage Ver 1.1
(Gitlab Create Ver 1.1, Gitlab Auto Clone Ver 2.1)

실습실 생성 후 바로 클론 가능
클론 시 절대경로 사용 수정
실습실 생성 시 드라이버 완전종료하도록 수정



Gitlab Manage Ver 1.2
(Gitlab Create Ver 1.2, Gitlab Auto Clone Ver 2.1)

파일/폴더명 원래대로 변경(실행시 오류 발생확률 줄이기 위함)
실습실 생성시 발생하는 문제 임시 수정

    Gitlab Manage Ver 1.2.1
    (Gitlab Create Ver 1.2.2, Gitlab Auto Clone Ver 2.1)

    핫픽스 - Create ; ARM기반 OS(Aarch64 아키텍쳐 CPU) 고려하도록 추가, 실습생성 과목 입력시 범위가 상수였던 것을 수정
    실습실 생성 시 차수 범위 표시



Gitlab Manage Ver 1.3
(Gitlab Create Ver 1.3, Gitlab Auto Clone Ver 2.2)

저장 폴더 규칙 변경
차수 다중입력 추가
ex> 2-4 : 2부터 4까지
Clone 종료 후 원한다면 Clone 관리에 머무를 수 있도록 변경



Gitlab Manage Ver 2.0
(Gitlab Create Ver 2.0, Gitlab Auto Clone Ver 2.2)

실습 제출 기능 추가. 특정 과제 제출은 불가.
실습실 생성 메뉴에서 실습 관리 메뉴로 이름 변경.



Gitlab Manage Ver 2.1
(Gitlab Create Ver 2.1, Gitlab Auto Clone Ver 2.2)

24.10.14 SSAFY GIT UI 업데이트로 인해 실습실 접속 방법 수정
실습 관리 메뉴 동작 방식을 동적 대기로 변경

    Gitlab Manage Ver 2.1.1
    (Gitlab Create Ver 2.1.1, Gitlab Auto Clone Ver 2.2)

    실습 관리 메뉴 안정성 위해 정적 대기 시간 추가 및 증가
    실습 관리 재접속 시 로그인 정보 유지(프로그램 종료시 초기화)
    
    
    Gitlab Manage Ver 2.1.2
    (Gitlab Create Ver 2.1.2, Gitlab Auto Clone Ver 2.2)

    핫픽스 ; 실습 관리 로그인 실패 시 무한 루프 돌면서 계속 로그인 실패 발생 
    -> 정상 동작하도록 수정
    
    
    Gitlab Manage Ver 2.1.3
    (Gitlab Create Ver 2.1.3, Gitlab Auto Clone Ver 2.2)

    핫픽스 ; 과목이 6개가 되면서 로그인 이후 실습실 과목 찾는 과정에서 오류 발생
    -> 정상 동작하도록 수정
    
    
    Gitlab Manage Ver 2.1.4
    (Gitlab Create Ver 2.1.3, Gitlab Auto Clone Ver 2.2.1)

    vue 과목 실습 클론 대응 추가
'''

import clone, create
Id, password = '',''
if __name__=='__main__':
    while 1:
        try: c=int(input("\n1. 실습 관리  2. clone 관리 (종료:0) : "))
        except: print("정수만 입력해주세요.")
        else:
            if c==0: break
            elif c==1: Id,password=create.main(Id,password)
            elif c==2: clone.main()
            else:
                print("1, 2 중 하나만 입력해 주세요.")
                continue