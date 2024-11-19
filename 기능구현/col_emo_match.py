'''
제가 제시한 색상 팔레트의 타당성을 뒷받침할 수 있는 몇 가지 연구 결과를 소개해 드리겠습니다:
Kaya and Epps (2004)의 연구1:
기쁨(Joy)은 노란색과 가장 많이 연관되었습니다. 이는 우리 팔레트의 '기쁨' 색상과 일치합니다.
슬픔(Sadness)은 파란색, 회색, 보라색과 연관되었습니다. 우리 팔레트에서 '슬픔'을 
짙은 파란색으로 표현한 것과 일치합니다.
분노(Anger)는 빨간색과 가장 많이 연관되었습니다. 이 역시 우리 팔레트와 일치합니다.
Sutton and Altarriba (2016)의 연구4:
빨간색은 주로 부정적인 감정 단어와 연관되었습니다. 이는 우리 팔레트에서 '분노'를 빨간색으로 
표현한 것과 일치합니다.
노란색과 흰색은 긍정적인 감정 단어와 연관되었습니다. 이는 우리 팔레트에서 '기쁨'을 밝은 
노란색으로 표현한 것과 일치합니다.
Moller et al. (2009)의 연구3:
부정적인 단어를 빨간색으로, 긍정적인 단어를 초록색으로 제시했을 때 반응 시간이 감소했습니다. 
이는 색상과 감정 사이의 연관성을 지지합니다.
Kuhbandner and Pekrun (2013)의 연구3:
빨간색으로 제시된 부정적 단어와 초록색으로 제시된 긍정적 단어의 회상률이 더 높았습니다. 
이 역시 색상과 감정의 연관성을 뒷받침합니다.
이러한 연구 결과들은 우리가 제시한 색상 팔레트의 많은 부분을 지지합니다. 
그러나 일부 감정(예: 당황, 불안, 상처)에 대해서는 직접적인 연구 결과가 부족하며, 
이는 향후 추가 연구가 필요한 영역입니다. 또한, 색상과 감정의 연관성은 문화적 차이와 
개인적 경험에 따라 달라질 수 있음을 유의해야 합니다2.
'''
import matplotlib.pyplot as plt
import numpy as np

# RGB값 두 배열 사이의 유클리드 거리를 계산하는 함수
def calculate_distance(color1, color2):
    return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

# RGB 값을 HEX 코드로 변환하는 함수
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# 제공된 색상 팔레트와 해당 감정
color_palette = {
    'Joy': (255, 255, 0),
    'Sadness': (0, 0, 139),
    'Anger': (255, 0, 0),
    'Embarrassment': (255, 165, 0),
    'Anxiety': (128, 0, 128),
    'Pain': (165, 42, 42),
    'Joy + Sadness': (0, 255, 255),
    'Joy + Anger': (255, 165, 0),
    'Joy + Embarrassment': (255, 218, 185),
    'Joy + Anxiety': (144, 238, 144),
    'Joy + Pain': (255, 182, 193),
    'Sadness + Anger': (128, 0, 128),
    'Sadness + Embarrassment': (128, 128, 128),
    'Sadness + Anxiety': (0, 0, 128),
    'Sadness + Pain': (75, 0, 130),
    'Anger + Embarrassment': (255, 69, 0),
    'Anger + Anxiety': (139, 0, 0),
    'Anger + Pain': (165, 42, 42),
    'Embarrassment + Anxiety': (216, 191, 216),
    'Embarrassment + Pain': (210, 180, 140),
    'Anxiety + Pain': (139, 0, 139),
    'Joy + Sadness + Anger': (85, 107, 47),
    'Joy + Sadness + Embarrassment': (175, 238, 238),
    'Joy + Sadness + Anxiety': (112, 128, 144),
    'Joy + Sadness + Pain': (230, 230, 250),
    'Joy + Anger + Embarrassment': (255, 127, 80),
    'Joy + Anger + Anxiety': (255, 0, 255),
    'Joy + Anger + Pain': (250, 128, 114),
    'Joy + Embarrassment + Anxiety': (255, 255, 224),
    'Joy + Embarrassment + Pain': (255, 218, 185),
    'Joy + Anxiety + Pain': (154, 205, 50),
    'Sadness + Anger + Embarrassment': (139, 0, 139),
    'Sadness + Anger + Anxiety': (0, 0, 103),
    'Sadness + Anger + Pain': (128, 0, 32),
    'Sadness + Embarrassment + Anxiety': (112, 128, 144),
    'Sadness + Embarrassment + Pain': (105, 105, 105),
    'Sadness + Anxiety + Pain': (25, 25, 112),
    'Anger + Embarrassment + Anxiety': (255, 140, 0),
    'Anger + Embarrassment + Pain': (205, 92, 92),
    'Anger + Anxiety + Pain': (128, 0 ,0 ),
    'Embarrassment + Anxiety + Pain' : (101 ,0 ,11)
}

# 사용자로부터 RGB 값 입력 받기
try:
    r = int(input("R 값을 입력하세요(0-255): "))
    g = int(input("G 값을 입력하세요(0-255): "))
    b = int(input("B 값을 입력하세요(0-255): "))
except ValueError:
    print("올바른 숫자를 입력하세요.")
else:
    
    user_rgb = (r,g,b)

    # 모든 팔레트 색상에 대해 유사도 계산
    similarities = [(emotion ,calculate_distance(user_rgb ,color),color) for emotion ,color in color_palette.items()]

    #유사도 순으로 정렬 
    sorted_similarities = sorted(similarities ,key=lambda x:x[1])

    #모든 팔레트의 컬러 출력

    fig ,ax = plt.subplots(figsize=(10 ,6))
    for i,(emotion,color) in enumerate(color_palette.items()):
        rect = plt.Rectangle((0,i),1 ,1,color=[c/255. for c in color])
        ax.add_patch(rect)
        ax.text(1.1,i+ .5,f'{emotion}:{color}',va='center',fontsize=10)

    ax.set_xlim(0 ,2)
    ax.set_ylim(0,len(color_palette))
    ax.set_axis_off()
    plt.title('Color Palette with Emotions')
    plt.show()

    #가장 유사한 상위 다섯 감정 추출 및 시각화

    top_5_similar_colors = sorted_similarities[:5]

    fig ,axes = plt.subplots(1,len(top_5_similar_colors),figsize=(15 ,3))
    fig.subplots_adjust(wspace=.5)

    for i,(emotion,distance,color) in enumerate(top_5_similar_colors):
        color_image = np.zeros((100 ,100 ,3),dtype=np.uint8)
        color_image[:] = color

        axes[i].imshow(color_image)
        axes[i].set_title(f"{emotion}\nRGB:{color}\n유사도:{distance:.2f}",fontsize=10)
        axes[i].axis('off')

    plt.show()
    
    
    
# import matplotlib.pyplot as plt
# import numpy as np

# # RGB값 두 배열 사이의 유클리드 거리를 계산하는 함수
# def calculate_distance(color1, color2):
#     return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

# # RGB 값을 HEX 코드로 변환하는 함수
# def rgb_to_hex(rgb):
#     return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# # 제공된 색상 팔레트와 해당 감정
# color_palette = {
#     '기쁨': (255, 255, 0),
#     '슬픔': (0, 0, 139),
#     '분노': (255, 0, 0),
#     '당황': (255, 165, 0),
#     '불안': (128, 0, 128),
#     '상처': (165, 42, 42),
#     '기쁨 + 슬픔': (0, 255, 255),
#     '기쁨 + 분노': (255, 165, 0),
#     '기쁨 + 당황': (255, 218, 185),
#     '기쁨 + 불안': (144, 238, 144),
#     '기쁨 + 상처': (255, 182, 193),
#     '슬픔 + 분노': (128, 0, 128),
#     '슬픔 + 당황': (128, 128, 128),
#     '슬픔 + 불안': (0, 0, 128),
#     '슬픔 + 상처': (75, 0, 130),
#     '분노 + 당황': (255, 69, 0),
#     '분노 + 불안': (139, 0, 0),
#     '분노 + 상처': (165, 42, 42),
#     '당황 + 불안': (216, 191, 216),
#     '당황 + 상처': (210, 180, 140),
#     '불안 + 상처': (139, 0, 139),
#     '기쁨 + 슬픔 + 분노': (85, 107, 47),
#     '기쁨 + 슬픔 + 당황': (175, 238, 238),
#     '기쁨 + 슬픔 + 불안': (112, 128, 144),
#     '기쁨 + 슬픔 + 상처': (230, 230, 250),
#     '기쁨 + 분노 + 당황': (255, 127, 80),
#     '기쁨 + 분노 + 불안': (255, 0, 255),
#     '기쁨 + 분노 + 상처': (250, 128, 114),
#     '기쁨 + 당황 + 불안': (255, 255, 224),
#     '기쁨 + 당황 + 상처': (255, 218, 185),
#     '기쁨 + 불안 + 상처': (154, 205, 50),
#     '슬픔 + 분노 + 당황': (139, 0, 139),
#     '슬픔 + 분노 + 불안': (0, 0, 103),
#     '슬픔 + 분노 + 상처': (128, 0, 32),
#     '슬픔 + 당황 + 불안': (112, 128, 144),
#     '슬픔 + 당황 + 상처': (105, 105, 105),
#     '슬픔 + 불안 + 상처': (25, 25, 112),
#     '분노 + 당황 + 불안': (255, 140, 0),
#     '분노 + 당황 + 상처': (205, 92, 92),
#     '분노 + 불안 + 상처': (128, 0, 0),
#     '당황 + 불안 + 상처': (101, 0, 11)
# }

# # 사용자로부터 RGB 값 입력 받기
# r = int(input("R 값을 입력하세요 (0-255): "))
# g = int(input("G 값을 입력하세요 (0-255): "))
# b = int(input("B 값을 입력하세요 (0-255): "))

# user_rgb = (r, g, b)

# # 모든 팔레트 색상에 대해 유사도 계산
# similarities = [(emotion, calculate_distance(user_rgb, color)) for emotion, color in color_palette.items()]
# # 유사도 순으로 정렬
# sorted_similarities = sorted(similarities, key=lambda x: x[1])

# # 가장 유사한 상위 다섯 감정 추출
# top_5_similar_colors = sorted_similarities[:5]

# # 시각적으로 색상을 보여주기 위한 플롯 생성
# fig, axes = plt.subplots(1, len(top_5_similar_colors), figsize=(15, 3))
# fig.subplots_adjust(wspace=0.5)

# for i, (emotion, distance, color) in enumerate(top_5_similar_colors):
#     # 빈 이미지에 해당 색상 채우기
#     color_image = np.zeros((100, 100, 3), dtype=np.uint8)
#     color_image[:] = color
    
#     # 해당 색상과 감정을 플롯에 표시
#     axes[i].imshow(color_image)
#     axes[i].set_title(f"{emotion}\nRGB: {color}\nHEX: {rgb_to_hex(color)}", fontsize=10)
#     axes[i].axis('off')  # 축 숨기기

# plt.show()

# # 가장 유사한 상위 다섯 감정 출력
# print(f"\n입력한 RGB 값 ({r}, {g}, {b})과 가장 유사한 다섯 가지 감정:")
# for i, (emotion, distance) in enumerate(sorted_similarities[:5], 1):
#     print(f"{i}. {emotion} (유사도 점수: {distance:.2f})")

# import matplotlib.pyplot as plt
# import numpy as np

# def calculate_distance(color1, color2):
#     return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

# def rgb_to_hex(rgb):
#     return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# color_palette = {
#     'Joy': (255, 255, 0),
#     'Sadness': (0, 0, 139),
#     'Anger': (255, 0, 0),
#     'Embarrassment': (255, 165, 0),
#     'Anxiety': (128, 0, 128),
#     'Pain': (165, 42, 42),
#     'Joy + Sadness': (0, 255, 255),
#     'Joy + Anger': (255, 165, 0),
#     'Joy + Embarrassment': (255, 218, 185),
#     'Joy + Anxiety': (144, 238, 144),
#     'Joy + Pain': (255, 182, 193),
#     'Sadness + Anger': (128, 0, 128),
#     'Sadness + Embarrassment': (128, 128, 128),
#     'Sadness + Anxiety': (0, 0, 128),
#     'Sadness + Pain': (75, 0, 130),
#     'Anger + Embarrassment': (255, 69, 0),
#     'Anger + Anxiety': (139, 0, 0),
#     'Anger + Pain': (165, 42, 42),
#     'Embarrassment + Anxiety': (216, 191, 216),
#     'Embarrassment + Pain': (210, 180, 140),
#     'Anxiety + Pain': (139, 0, 139),
#     'Joy + Sadness + Anger': (85, 107, 47),
#     'Joy + Sadness + Embarrassment': (175, 238, 238),
#     'Joy + Sadness + Anxiety': (112, 128, 144),
#     'Joy + Sadness + Pain': (230, 230, 250),
#     'Joy + Anger + Embarrassment': (255, 127, 80),
#     'Joy + Anger + Anxiety': (255, 0, 255),
#     'Joy + Anger + Pain': (250, 128, 114),
#     'Joy + Embarrassment + Anxiety': (255, 255, 224),
#     'Joy + Embarrassment + Pain': (255, 218, 185),
#     'Joy + Anxiety + Pain': (154, 205, 50),
#     'Sadness + Anger + Embarrassment': (139, 0, 139),
#     'Sadness + Anger + Anxiety': (0, 0, 103),
#     'Sadness + Anger + Pain': (128, 0, 32),
#     'Sadness + Embarrassment + Anxiety': (112, 128, 144),
#     'Sadness + Embarrassment + Pain': (105, 105, 105),
#     'Sadness + Anxiety + Pain': (25, 25, 112),
#     'Anger + Embarrassment + Anxiety': (255, 140, 0),
#     'Anger + Embarrassment + Pain': (205, 92, 92),
#     'Anger + Anxiety + Pain': (128, 0, 0),
#     'Embarrassment + Anxiety + Pain': (101, 0, 11)
# }

# # 사용자로부터 RGB 값 입력 받기
# try:
#     r = int(input("R 값을 입력하세요 (0-255): "))
#     g = int(input("G 값을 입력하세요 (0-255): "))
#     b = int(input("B 값을 입력하세요 (0-255): "))
#     user_rgb = (r, g, b)
# except ValueError:
#     print("올바른 숫자를 입력해주세요.")
#     exit()

# # 모든 팔레트 색상에 대해 유사도 계산
# similarities = [(emotion, calculate_distance(user_rgb, color), color) for emotion, color in color_palette.items()]
# # 유사도 순으로 정렬
# sorted_similarities = sorted(similarities, key=lambda x: x[1])

# # 가장 유사한 상위 다섯 감정 추출
# top_5_similar_colors = sorted_similarities[:5]

# # 시각적으로 색상을 보여주기 위한 플롯 생성
# fig, axes = plt.subplots(1, len(top_5_similar_colors), figsize=(15, 3))
# fig.subplots_adjust(wspace=0.5)

# for i, (emotion, distance, color) in enumerate(top_5_similar_colors):
#     # 빈 이미지에 해당 색상 채우기
#     color_image = np.zeros((100, 100, 3), dtype=np.uint8)
#     color_image[:] = color
    
#     # 해당 색상과 감정을 플롯에 표시
#     axes[i].imshow(color_image)
#     axes[i].set_title(f"{emotion}\nRGB: {color}\nHEX: {rgb_to_hex(color)}", fontsize=10)
#     axes[i].axis('off')  # 축 숨기기

# plt.show()


# import seaborn as sns

# # 컬러 팔레트 로드 (예: 'husl' 팔레트)
# palette = sns.color_palette("color_palatte", len(color_palette))

# # 팔레트의 색상 출력
# for color in palette:
#     print(color)

# # 팔레트를 시각적으로 출력
# sns.palplot(palette)
# plt.show()


