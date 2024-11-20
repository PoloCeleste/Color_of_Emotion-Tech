# drillllll
0. https://github.com/ParkSeYun98/SSACCER-BE?tab=readme-ov-file

위 사이트를 가이드라인으로 함
- 회의타임 (최소 5분에서 최대 15분)
    1. 09시 00분
        - 어제 하면서 썼던 것, 배운 것 공유
        - 오늘의 할 일
        - 오전 할 일

    2. 14시 00분
        - 오전의 진행상황
        - 오후 할 일

    3. 21시 00분 (최대 1시간까지 가능)
        - 지금까지의 진행상황
        - 오늘 남은 시간에 할 일
        - 내일 할 일
        
    +. 다하고 나서 끄기 전에 업데이트 한 번

1. 팀원 정보 및 업무 분담 내역
유지웅: 프론트, css, 알고리즘
김주찬: 백, css, 알고리즘

2. 목표 서비스 구현 및 실제 구현 정도
11/17
??????????

- 11/18
    **유지웅**
    : 화이트베이스, 와이어프레임 작성
    - (SSAFY) 뷰 프레임워크 + 퍼플렉시티로 VIEWS랑 COMPONENTS 작성
    - (21:00 ~) 프론트 VIEWS, COMPONENTS 다듬기, 약간의 ACTION(캐러셀) 추가, 감정분석 알고리즘 수정

    **김주찬**
    : ERD 작성
    - (SSAFY) API REQUEST(TMDB 기반) + 크롤링(왓챠피디아) -> 영화 데이터 수집 코드 작성
    - (21:00 ~) DB 수집코드 완성해보기

    **오늘의 이슈**
    - 와이어프레임 역량이 매우 열악했다.(그림을 못그린다.)
    - AI에게 상당히 의존하고 있다. 코드 완성 이후 코드 리뷰를 해야겠음.
    - 감정분석 알고리즘에 대한 신뢰도를 더욱 높여야 한다고 느꼈다.(but, 시간, 데이터가 없어서 확인이 불가능)

    - 공급자에 대한 정보를 상세히 얻고 싶었는데 실제로는 그렇지 못했다.
    - TMDB API에서 인자로 주는 것이 정확히 어떤 인자인지 알 수 없어서 하나하나 확인해보는 과정이 힘들었다. (video : true <-이게뭐임?)
    - TMDB API에서 watchprovider를 불러오지 못했다(한국의 프로바이더를 제공하지 않는다). **-> 왓챠피디아 기준으로 변경**

- 11/19
    **유지웅**
    - 오늘 할 일
        - (SSAFY) 모달창에 카메라 연결, 모달창 크기 조절
        - (SSAFY) 색-감정-매칭 알고리즘
        - (숙제) 멘트 전후 나누고, 측정 두 번 하게 만들기 (시간 좀 길게) (못함)

    **김주찬**
    - 오늘 할 일
        - (SSAFY) 영화 DB 출처 다시따기
        - (숙제) 영화 DB 출처 다시따기

    **오늘의 이슈**
    - (API 작업하면서 포스터 색상 집어넣을 때)파이썬에서 json을 저장할 일이 있었는데, 
    object of type int32 is not json serializable 오류가 발생했다. 이런 비슷한 오류가 
    자료형이 numpy의 int32, int64 이거나, datetime 일 경우에도 발생한다. -> 리스트로 묶어서 안에 넣어버림.
    - 사이트가 로딩이 되어야 이미지, 동영상에 접근 할 수 있다. 저기에 대한 url들은 스타일의 백그라운드 url으로 설정되어
    있어서, 스타일 속성값을 가져와서 전처리를 해야한다.

    - 색-감정 매칭하는 알고리즘 작성 중에 유클리드 거리로 유사도를 계산했더니 색상이 별로 비슷하다고 느끼지 못했다. 
    그래서 CIELAB 이라는 방법을 도입해서 유사도 계산식을 바꿨더니 유의미한 결과가 나왔다.
    - water 브랜치를 새로 파서 프론트를 정리하면서 다시 구현함. 코드 기능별로 주석 넣고, 추가되는 코드가 뭔지 표기하고
    이게 왜 그렇게 작동하는지 이유를 파악하려고 했다. 하지만 웹소켓을 적용하는 순간부터 모든 것이 무너졌다.
    계속 공부해야 답이 나올 것 같다.

11/20
**유지웅**
- 오늘 할 일
    - 카메라 전 후 나눈 데이터 처리하기ㅇ
    - 짜스만지기
    - DB 완성되면 그걸로 페이지 구성짜기
    - 멘트 두 분류로 나누기 -> (1. 측정 준비 2. 감정 유도 멘트 방식으로) 나누기 위한 프로세스 결정ㅇ
    - 코드 구현

**김주찬**
- 오늘 할 일
    - 크롤링 알고리즘 마무리
    - 짜스와서 도와주세요

**오늘의 이슈**


1. 데이터베이스 모델링 (ERD)


4. 영화 추천 알고리즘에 대한 기술적 설명


5. 핵심 기능에 대한 설명


6. 생성형 AI를 활용한 부분


7. 기타 (느낀점, 후기 등)


8. 배포 서버 URL (배포했을 경우)


9. 이 외의 내용은 자유롭게 작성 가능


최소한 5개 이상의 URL 및 페이지를 구성해야 함
• Django REST framework를 사용하는 경우 사용자 요청에 따라 적절한
HTTP response status code를 응답해야 함
• .gitignore 파일을 추가하여 불필요한 파일 및 폴더는 제출하지 않음
• 필수 요구사항 이 외의 추가 기능 및 반응형 디자인 등은 자유롭게 수행