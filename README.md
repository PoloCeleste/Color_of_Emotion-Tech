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

11/18
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
- AI에게 상당히 의존하고 있다.
- 감정분석 알고리즘에 대한 신뢰도를 더욱 높여야 한다고 느꼈다.

- 공급자에 대한 정보를 상세히 얻고 싶었는데 실제로는 그렇지 못했다.
- TMDB API에서 인자로 주는 것이 정확히 어떤 인자인지 알 수 없어서 하나하나 확인해보는 과정이 힘들었다. (video : true <-이게뭐임?)

**유지웅**
- 오늘 할 일
    - 카메라 연동
    - 모달창 띄우기
    - 모달창 크기 조절
    - 색-감정-매칭 알고리즘

**김주찬**
- 오늘 할 일
    - 코드 다듬어서 api에서 가져오는 항목 긁어오기
    - 크롤링
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