최종 관통 프론젝트

12기 1학기 최종 관통 프로젝트

주제

- 딥러닝 기반 안면인식 데이터를 활용한 감정, 색 추출 및 데이터, 감정, 색 기반 영화 추천 서비스

- `배포 할 거면 링크 넣기`
- 카메라를 이용한 감정 분석

  - 웹소켓을 활용, 백엔드로 사용자 표정사진 전달.
  - 자체 제작한 딥러닝 모델을 사용. 사용자 감정 추출.
  - 감정값을 전 / 후로 나누어 통계적으로 분석. 변화값으로 현재 감정을 추론.

- 감정기반 색상 추출

  - 색채심리학 기반 감정별 색상 매칭
  - 현재 감정 ( 주감정, 부감정 \* 2) 기준으로 사용자에게 어울리는 색상 추출

- 감정, 색 기반 영화 추천
  - 현재 감정 기반 장르 매칭
  - 매칭된 장르 내에서 추출한 색상과 가장 어울리는 포스터를 가진 영화를 선별.

개요

- 수상 내역

  - 시발.

- 프로젝트 진행 기간

  - 사전준비 기간은 뺄까? ( 빼는 게 좋긴 함 )
  - 24.11.18(월) - 24.11.26(화) / 9일간 진행.

  - 배포 할거면 하는 기간 추가

- 프로젝트 팀

  - 유지웅 : 프론트(정), 백엔드(부), 알고리즘
  - 김주찬 : 백엔드(정), 프론트(부), 알고리즘

- 기술 스택

  - DB

    - SQLite

  - BACK

    - Django
    - Channel
    - Web socket
    - Daphne

  - FRONT

    - Vue 3
    - Channel
    - axios
    - Web socket
    - pinia
    - router

  - API

    - 자체제작 API ( TMDB + 왓챠피디아 크롤링 )

  - Data

    - 감정사진 30만장
    - 색채심리학 자료

  - Version Control

    - gitlab
    - github

  - CoOperation Tool

    - Discord
    - MatterMost

  - 배포 ( 한다면 )

- ERD

  ![alt text](movie_erd_crow.png)

기술

- 데이터 수집
  - 셀레니움( 김주찬씨가 작성하십시오. )
- 감정분석 ( 딥러닝 + 알고리즘 )

  - AI 허브에서 가져온 사전 학습된 모델을 이용.
  - 선정 이유 : 모델을 학습시키기 위한 시간과 데이터 수집 시간의 부족.

  - 프론트와 백 사이에 web socket을 열어서 실시간으로 사용자 사진을 백으로 보냄.
  - 백에서는 현재 사용자 상태 / 감정 유도 이후 상태 로 데이터를 나누어 감정데이터의 값을 `알고리즘`을 통해 처리함
  - 알고리즘 : 감정데이터를 딕셔너리 형태로 모으고, 로버스트 통계를 활용하여 정규화, 표준편차를 통해 감정 변화값을 추출
  - 로버스트 통계를 사용한 이유 : 사용자의 감정이 정규분포를 이루지 않을 가능성이 높고, 측정한 감정값 중에서 이상값들을 배제하기 위해서 사용.
  - 정규화 한 이유 : 모든 값의 합이 100이어서 절대적 변화량을 측정하기 힘듦으로 전체 크기를 1로 통일
  - 표준편차 : 중간값에서 가장 크게 요동친 값을 주된 감정으로 분석. 이를 위해서 이상치 탐지가 가능한 IQR 표준편차를 이용.
  - t-test 사용 : 1번째 측정한 집단과 2번째 측정한 집단의 분산이 동질한지 검정하기 위해 사용.<br>t-value와 p-value로 유의성을 판단하며, p-value가 .05보다 클 경우 두 집단의 분산이 동질하다고 판단. -> 의미있는 감정 변화라고 판단<br>이를 바탕으로 감정 점수와 유의성이 높은 순으로 주감정과 부감정을 분류

- 색채심리학 ( 관련 논문 )

  - 현재 심리에 따라서 색상값을 연결하기 위해 학술자료를 활용.
  - [색채 심리학](https://www.thedigitalmkt.com/color-psychology/)
  - ![alt text](image-4.png)
  - 학술 자료에서 감정에 대한 기준을 다양하게 나누어 우리가 사전에 지정하였던 7개의 감정으로 정확히 매치하기 힘듦.
  - 유사한 감정과 연계하여 감정-색상 데이터 연결

- 색상파레트 추출 ( 라이브러리 )

  - 관련 라이브러리 사용
  - [Pylette](https://github.com/qTipTip/Pylette)
  - 포스터에서 주로 사용된 색상, 색상별 지배도 추출

- 색상유사도 ( 알고리즘 )
  - CIE(국제조명위원회)에서 개발한 색상 차이를 측정하는 표준 방법을 활용함.
  - ![alt text](image-3.png)
  - CIELAB 기준 유사도를 판별
  - [CIELAB 설명](https://ko.wikipedia.org/wiki/CIELAB_%EC%83%89_%EA%B3%B5%EA%B0%84#:~:text=Lab%20%EC%83%89%20%EA%B3%B5%EA%B0%84%EC%9D%80%20%EC%9D%B8%EA%B0%84,%ED%95%98%EB%8A%94%20%EC%98%81%EC%97%AD%EB%A7%8C%EC%9D%84%20%EB%B3%B4%EC%97%AC%EC%A3%BC%EB%8A%94%20%EA%B7%B8%EB%A6%BC)
  - CIE76으로 사용( 유클리드 거리를 기준으로 유사도 판별 )
  - 이후 정확도를 높이기 위해 CIE94( 가중치 )에서 CIE dE2000으로 변경

  - ![alt text](image-2.png)
  - [Color Space](https://en.wikipedia.org/wiki/Color_space)
  - [CIE dE 2000](https://techkonusa.com/demystifying-the-cie-%CE%B4e-2000-formula/)
  - 색상의 유사도를 파악하기 위해 비선형적으로 공간을 휘어 실제로 보았을 때 더욱 유사한 색감을 뽑아낼 수 있도록 함.

- 영화추천 ( 알고리즘 )
  - 감정 기준으로 장르 선별, 포스터 색상 기준 색상으로 유사도, 지배도를 고려하여 색감이 유사한 영화를 선별.

- 적용
색상 처리 방식
RGB에서 LAB 색공간으로 변환
```py
def rgb_to_lab(rgb):
    rgb_normalized = np.array(rgb) / 255.0
    rgb_normalized = rgb_normalized.reshape(1, 1, 3)
    lab = skcolor.rgb2lab(rgb_normalized)
    return lab[0, 0]
```

RGB 값을 0-1 사이로 정규화
LAB 색공간으로 변환하여 인간의 시각적 인식과 유사한 방식으로 색상 표현

CIEDE2000 알고리즘 사용
```py
def delta_e_2000(lab1, lab2, kL=1, kC=1, kH=1):
    # L: 명도(Lightness)
    # a: 빨강-초록 축
    # b: 노랑-파랑 축
```
두 색상 간의 차이를 계산하는 가장 정확한 방식 중 하나
명도, 채도, 색상의 차이를 각각 고려하여 종합적인 색상 차이 계산

영화 추천 프로세스
감정 색상 세트 찾기
```py
color_set = EmotionColor.objects.filter(
    emotion_id__in=current_emotions
).first()
```
입력된 감정 ID들에 맞는 색상 세트 검색
가장 많은 감정을 포함하는 세트부터 검색

장르 기반 필터링
```py
matching_movies = Movie.objects.filter(
    genre_ids__name__in=[genre.name for genre in color_set.genres_id.all()]
).distinct()
```
색상 세트와 연관된 장르의 영화들만 선택

색상 유사도 계산
```py
similarities = []
for emotion_color in color_set.emotions_color:
    for poster_color in movie.poster_palette:
        similarity = calculate_color_similarity(emotion_color, poster_color[:3])
        similarities.append((similarity, poster_color[3]))
```
감정 색상과 영화 포스터의 색상 팔레트를 비교
각 색상의 지배도(dominance)를 가중치로 사용

최종 점수 계산
```py
avg_similarity = np.mean([s[0] for s in similarities])
weighted_dominance = np.average(
    [s[1] for s in similarities],
    weights=[1/s[0] if s[0] != 0 else 1 for s in similarities]
)
```
색상 유사도의 평균과 지배도를 결합하여 최종 점수 계산
유사도가 높을수록 가중치가 높아지는 방식 사용

영화 정렬 및 선택
```py
sorted_movies = [movie for movie, _ in sorted(movie_scores, key=lambda x: x[1])][:51]
sorted_movies.reverse()
```
계산된 점수를 기준으로 영화 정렬
상위 51개 영화 선택 후 역순 정렬

기타 / 배운 점 / 깨달은 점 등 모든 기록

- 느낀 점

- 아쉬웠던 점

- 깃허브 협업 세팅

```

```
