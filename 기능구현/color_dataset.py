import json
import numpy as np

def file_out(dataname, data):
    with open(f'{dataname}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent="\t", cls=NpEncoder)
    print(len(data))

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):		# np.integer를 python의 int로 변환
            return int(obj)
        if isinstance(obj, np.floating):	# np.floating을 python의 float로 변환
            return float(obj)
        if isinstance(obj, np.ndarray):		# np.ndarray를 python의 list로 변환
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

emotion_color_dict = {
    'Joy': [
        (255, 255, 0),  # 밝은 노란색
        (255, 215, 0)   # 금색 [1]
    ],
    'Sadness': [
        (0, 0, 139),    # 어두운 파란색
        (70, 130, 180)  # 강철 파란색 [3]
    ],
    'Anger': [
        (255, 0, 0),    # 빨간색
        (178, 34, 34)   # 짙은 빨간색 [3]
    ],
    'Embarrassment': [
        (255, 192, 203),  # 연한 분홍색
        (255, 182, 193)   # 연한 분홍색 (Light Pink) [2]
    ],
    'Anxiety': [
        (128, 128, 128),  # 회색
        (169, 169, 169)   # 어두운 회색 [4]
    ],
    'Pain': [
        (128, 0, 0),    # 어두운 빨간색
        (139, 0, 0)     # 짙은 빨간색 [3]
    ],
    'Neutral': [
        (255, 255, 255),  # 흰색
        (245, 245, 245)   # 흰 연기색 [5]
    ],

    'Joy, Sadness': [
        (152, 251, 152),  # 연한 녹색
        (0, 255, 255),    # 청록색
        (176, 224, 230)   # 파우더 블루 [4]
    ],
    'Joy, Anger': [
        (255, 165, 0),    # 주황색
        (255, 140, 0)     # 짙은 주황색 [2]
    ],
    'Joy, Embarrassment': [
        (255, 182, 193),  # 연한 분홍색
        (255, 218, 185)   # 복숭아색 [2]
    ],
    'Joy, Anxiety': [
        (255, 255, 224),  # 연한 노란색
        (240, 230, 140)   # 카키색 [2]
    ],
    'Joy, Pain': [
        (255, 127, 80),   # 산호색
        (255, 160, 122)   # 연한 산호색 [2]
    ],
    'Joy, Neutral': [
        (255, 255, 128),  # 매우 연한 노란색
        (255, 250, 205)   # 레몬 쉬폰 [4]
    ],

    'Sadness, Anger': [
        (128, 0, 128),    # 보라색
        (75, 0, 130)      # 짙은 보라색 [4]
    ],
    'Sadness, Embarrassment': [
        (147, 112, 219),  # 연한 보라색
        (230, 230, 250)   # 라벤더색 [4]
    ],
    'Sadness, Anxiety': [
        (70, 130, 180),   # 강철 파란색
        (112, 128, 144)   # 슬레이트 그레이 [4]
    ],
    'Sadness, Pain': [
        (75, 0, 130),     # 짙은 보라색
        (72, 61, 139)     # 짙은 슬레이트 블루 [4]
    ],
    'Sadness, Neutral': [
        (176, 224, 230),  # 파우더 블루
        (176, 196, 222)   # 연한 강철 블루 [4]
    ],

    'Anger, Embarrassment': [
        (255, 69, 0),     # 빨간 주황색
        (205, 92, 92)     # 인디언 레드 [4]
    ],
    'Anger, Anxiety': [
        (178, 34, 34),    # 짙은 빨간색
        (139, 0, 0)       # 매우 짙은 빨간색 [3]
    ],
    'Anger, Pain': [
        (139, 0, 0),      # 어두운 빨간색
        (128, 0, 0)       # 마룬색 [4]
    ],
    'Anger, Neutral': [
        (255, 99, 71),    # 토마토색
        (233, 150, 122)   # 연한 산호색 [4]
    ],

    'Embarrassment, Anxiety': [
        (216, 191, 216),  # 연한 보라색
        (221, 160, 221)   # 자두색 [4]
    ],
    'Embarrassment, Pain': [
        (255, 160, 122),  # 연한 산호색
        (219, 112, 147)   # 팔레 바이올렛 레드 [4]
    ],
    'Embarrassment, Neutral': [
        (255, 228, 225),  # 미색
        (255, 245, 238)   # 조개껍질색 [4]
    ],

    'Anxiety, Pain': [
        (169, 169, 169),  # 어두운 회색
        (128, 128, 128)   # 회색 [5]
    ],
    'Anxiety, Neutral': [
        (211, 211, 211),  # 연한 회색
        (220, 220, 220)   # 게인스보로 [5]
    ],

    'Pain, Neutral': [
        (245, 245, 245),  # 흰 연기색
        (192, 192, 192)   # 은색 [4]
    ],

    'Joy, Sadness, Anger': [
        (218, 112, 214),  # 난초색
        (128, 128, 0),    # 올리브색
        (153, 50, 204)    # 짙은 난초색 [4]
    ],
    'Joy, Sadness, Embarrassment': [
        (175, 238, 238),  # 연한 청록색
        (230, 230, 250)   # 라벤더색 [4]
    ],
    'Joy, Sadness, Anxiety': [
        (176, 224, 230),  # 파우더 블루
        (112, 128, 144)   # 슬레이트 그레이 [4]
    ],
    'Joy, Sadness, Pain': [
        (221, 160, 221),  # 자두색
        (216, 191, 216)   # 엷은 자주색 [4]
    ],
    'Joy, Sadness, Neutral': [
        (240, 248, 255),  # 앨리스 블루
        (230, 230, 250)   # 라벤더색 [4]
    ],

    'Joy, Anger, Embarrassment': [
        (255, 99, 71),    # 토마토색
        (255, 127, 80)    # 산호색 [2]
    ],
    'Joy, Anger, Anxiety': [
        (255, 140, 0),    # 짙은 주황색
        (255, 69, 0)      # 빨간 주황색 [2]
    ],
    'Joy, Anger, Pain': [
        (255, 69, 0),     # 빨간 주황색
        (178, 34, 34)     # 짙은 빨간색 [3]
    ],
    'Joy, Anger, Neutral': [
        (255, 160, 122),  # 연한 산호색
        (255, 218, 185)   # 복숭아색 [2]
    ],

    'Joy, Embarrassment, Anxiety': [
        (255, 228, 196),  # 비스크색
        (255, 250, 205)   # 레몬 쉬폰 [4]
    ],
    'Joy, Embarrassment, Pain': [
        (255, 218, 185),  # 복숭아색
        (255, 192, 203)   # 연한 분홍색 [2]
    ],
    'Joy, Embarrassment, Neutral': [
        (255, 245, 238),  # 조개껍질색
        (255, 228, 225)   # 미색 [4]
    ],

    'Joy, Anxiety, Pain': [
        (240, 230, 140),  # 카키색
        (255, 255, 224)   # 연한 노란색 [2]
    ],
    'Joy, Anxiety, Neutral': [
        (255, 250, 205),  # 레몬 쉬폰
        (255, 255, 224)   # 연한 노란색 [2]
    ],

    'Joy, Pain, Neutral': [
        (255, 228, 225),  # 미색
        (255, 218, 185)   # 복숭아색 [2]
    ],

    'Sadness, Anger, Embarrassment': [
        (153, 50, 204),   # 짙은 난초색
        (139, 0, 139)     # 진한 자주색 [4]
    ],
    'Sadness, Anger, Anxiety': [
        (72, 61, 139),    # 짙은 슬레이트 블루
        (75, 0, 130)      # 짙은 보라색 [4]
    ],
    'Sadness, Anger, Pain': [
        (85, 26, 139),    # 짙은 보라색
        (128, 0, 128)     # 보라색 [4]
    ],
    'Sadness, Anger, Neutral': [
        (123, 104, 238),  # 중간 슬레이트 블루
        (106, 90, 205)    # 슬레이트 블루 [4]
    ],

    'Sadness, Embarrassment, Anxiety': [
        (230, 230, 250),  # 라벤더색
        (216, 191, 216)   # 엷은 자주색 [4]
    ],
    'Sadness, Embarrassment, Pain': [
        (219, 112, 147),  # 팔레 바이올렛 레드
        (199, 21, 133)    # 중간 자주색 [4]
    ],
    'Sadness, Embarrassment, Neutral': [
        (230, 230, 250),  # 라벤더색
        (240, 248, 255)   # 앨리스 블루 [4]
    ],

    'Sadness, Anxiety, Pain': [
        (112, 128, 144),  # 슬레이트 그레이
        (119, 136, 153)   # 연한 슬레이트 그레이 [4]
    ],
    'Sadness, Anxiety, Neutral': [
        (176, 196, 222),  # 연한 강철 블루
        (173, 216, 230)   # 연한 하늘색 [4]
    ],

    'Sadness, Pain, Neutral': [
        (192, 192, 192),  # 은색
        (211, 211, 211)   # 연한 회색 [4]
    ],

    'Anger, Embarrassment, Anxiety': [
        (205, 92, 92),    # 인디언 레드
        (178, 34, 34)     # 짙은 빨간색 [3]
    ],
    'Anger, Embarrassment, Pain': [
        (178, 34, 34),    # 짙은 빨간색
        (165, 42, 42)     # 갈색 [4]
    ],
    'Anger, Embarrassment, Neutral': [
        (233, 150, 122),  # 연한 산호색
        (250, 128, 114)   # 연어색 [2]
    ],

    'Anger, Anxiety, Pain': [
        (139, 0, 0),      # 짙은 빨간색
        (128, 0, 0)       # 마룬색 [4]
    ],
    'Anger, Anxiety, Neutral': [
        (205, 92, 92),    # 인디언 레드
        (188, 143, 143)   # 로지 브라운 [4]
    ],

    'Anger, Pain, Neutral': [
        (205, 92, 92),    # 인디언 레드
        (165, 42, 42)     # 갈색 [4]
    ],

    'Embarrassment, Anxiety, Pain': [
        (188, 143, 143),  # 로지 브라운
        (199, 21, 133)    # 중간 자주색 [4]
    ],
    'Embarrassment, Anxiety, Neutral': [
        (216, 191, 216),  # 엷은 자주색
        (230, 230, 250)   # 라벤더색 [4]
    ],

    'Embarrassment, Pain, Neutral': [
        (245, 222, 179),  # 밀색
        (255, 228, 196)   # 비스크색 [4]
    ],

    'Anxiety, Pain, Neutral': [
        (211, 211, 211),  # 연한 회색
        (192, 192, 192)   # 은색 [4]
    ]
}

emotion_color_dict.update({
    'Neutral': [
        (255, 255, 255),  # 흰색 (기존)
        (245, 245, 245),  # 흰 연기색 (기존)
        (144, 238, 144)   # 연한 녹색 (Light Green) [1][2]
    ],
    'Joy, Neutral': [
        (255, 255, 128),  # 매우 연한 노란색 (기존)
        (255, 250, 205),  # 레몬 쉬폰 (기존)
        (152, 251, 152)   # 연한 민트색 (Mint Green) [1][2]
    ],
    'Sadness, Neutral': [
        (176, 224, 230),  # 파우더 블루 (기존)
        (176, 196, 222),  # 연한 강철 블루 (기존)
        (143, 188, 143)   # 다크 시 그린 (Dark Sea Green) [1][4]
    ],
    'Anger, Neutral': [
        (255, 99, 71),    # 토마토색 (기존)
        (233, 150, 122),  # 연한 산호색 (기존)
        (128, 128, 0)     # 올리브 그린 [1][5]
    ],
    'Embarrassment, Neutral': [
        (255, 228, 225),  # 미색 (기존)
        (255, 245, 238),  # 조개껍질색 (기존)
        (144, 238, 144)   # 연한 녹색 (Light Green) [2][4]
    ],
    'Anxiety, Neutral': [
        (211, 211, 211),  # 연한 회색 (기존)
        (220, 220, 220),  # 게인스보로 (기존)
        (173, 255, 47)    # 그린 옐로우 (Green Yellow) [1][4]
    ],
    'Pain, Neutral': [
        (245, 245, 245),  # 흰 연기색 (기존)
        (192, 192, 192),  # 은색 (기존)
        (0, 128, 128)     # 틸 그린 (Teal Green) [1][5]
    ]
})

emotion_color_dict.update({
    # 빨간색/주황색 영역 (Energy, Courage, Strength)
    'Joy': [
        (255, 255, 0),    # 밝은 노란색 - Joy
        (255, 215, 0),    # 금색 - Glory
        (255, 223, 0),    # 황금빛 노란색 - Harvest
        (255, 236, 139),  # 연한 황금빛 - Victory
        (255, 140, 0),    # 진한 주황색 - Physical energy
        (255, 127, 80),   # 산호색 - Vitality
        (255, 99, 71),    # 토마토색 - Strength
        (255, 160, 122),  # 연한 산호색 - Beauty
        (255, 165, 0),    # 주황색 - Pleasure
        (255, 140, 0),    # 진한 주황색 - Friendship
        (255, 127, 36),   # 캐럿 오렌지 - Hospitality
        (255, 69, 0)      # 레드 오렌지 - Community
    ],

    'Anger': [
        (255, 0, 0),      # 순수 빨간색 - Courage
        (220, 20, 60),    # 진홍색 - Inner-Strength
        (178, 34, 34),    # 짙은 빨간색 - Protection
        (139, 0, 0),      # 진한 적갈색 - Tenacity
        (128, 0, 0),      # 마룬 - Will-power
        (205, 92, 92),    # 인디언 레드 - Dedication
        (240, 128, 128),  # 연한 산호색 - Vigilance
        (165, 42, 42),    # 갈색 - Loyalty
        (233, 150, 122),  # 다크 샐몬 - Drive
        (250, 128, 114),  # 샐몬 - Poetry
        (205, 92, 92),    # 인디언 레드 - Passion
        (178, 34, 34)     # 피어리 레드 - Energy
    ],

    # 보라색/자주색 영역 (Creativity, Intuition, Wisdom)
    'Anxiety': [
        (128, 0, 128),    # 보라색 - Intuition
        (147, 112, 219),  # 연한 보라색 - Dreams
        (138, 43, 226),   # 파란보라 - Imagination
        (75, 0, 130),     # 짙은 보라색 - Spiritual mastery
        (153, 50, 204),   # 다크 오키드 - Destiny
        (186, 85, 211),   # 중간 오키드 - Vision
        (221, 160, 221),  # 자두색 - Music
        (216, 191, 216),  # 엷은 자주색 - Creativity
        (238, 130, 238),  # 바이올렛 - Magic
        (148, 0, 211),    # 다크 바이올렛 - Maturity
        (139, 0, 139),    # 진한 자주색 - Judgement
        (153, 50, 204)    # 다크 오키드 - Long life
    ],

    'Embarrassment': [
        (255, 192, 203),  # 연한 분홍색 - Self-knowledge
        (255, 182, 193),  # 연한 분홍색 - Elegance
        (219, 112, 147),  # 팔레 바이올렛 레드 - Perception
        (255, 20, 147),   # 진한 분홍색 - Mature Love
        (199, 21, 133),   # 중간 자주색 - Originality
        (218, 112, 214),  # 난초색 - Discernment
        (238, 130, 238),  # 바이올렛 - Self-esteem
        (255, 0, 255),    # 마젠타 - Insight
        (218, 112, 214),  # 난초색 - Vision
        (199, 21, 133),   # 미디엄 바이올렛 레드 - Dreams
        (219, 112, 147),  # 팔레 바이올렛 레드 - Inspiration
        (255, 105, 180)   # 핫 핑크 - Luxury
    ],

    # 파란색 영역 (Trust, Wisdom, Discovery)
    'Sadness': [
        (0, 0, 139),      # 어두운 파란색 - Trust
        (25, 25, 112),    # 미드나잇 블루 - Wisdom
        (65, 105, 225),   # 로열 블루 - Dignity
        (30, 144, 255),   # 도지 블루 - Faith
        (70, 130, 180),   # 강철 파란색 - Respect
        (100, 149, 237),  # 콘플라워 블루 - Understanding
        (176, 224, 230),  # 파우더 블루 - Compassion
        (135, 206, 235),  # 하늘색 - Honor
        (0, 191, 255),    # 딥 스카이 블루 - Truth
        (173, 216, 230),  # 연한 파란색 - Grace
        (176, 196, 222),  # 연한 강철 블루 - Virtue
        (176, 224, 230)   # 파우더 블루 - Prophecy
    ],

    # 초록색 영역 (Growth, Balance, Renewal)
    'Neutral': [
        (144, 238, 144),  # 연한 녹색 - Growth
        (34, 139, 34),    # 숲 녹색 - Balance
        (0, 128, 0),      # 녹색 - Renewal
        (85, 107, 47),    # 다크 올리브 그린 - Safety
        (143, 188, 143),  # 다크 시 그린 - Learning
        (60, 179, 113),   # 중간 시 그린 - Prosperity
        (46, 139, 87),    # 시 그린 - Productivity
        (32, 178, 170),   # 라이트 시 그린 - Health
        (152, 251, 152),  # 연한 녹색 - Fertility
        (50, 205, 50),    # 라임 그린 - Exuberance
        (0, 255, 127),    # 스프링 그린 - Awakening
        (124, 252, 0),    # 로운 그린 - Independence
        (173, 255, 47),   # 그린 옐로우 - Spiritual development
        (154, 205, 50)    # 옐로우 그린 - Good fortune
    ],

    # 노란색 영역 (Joy, Enthusiasm, Enlightenment)
    'Joy, Neutral': [
        (255, 255, 224),  # 연한 노란색 - Enlightenment
        (255, 250, 205),  # 레몬 쉬폰 - Consciousness
        (250, 250, 210),  # 연한 골덴로드 - Authority
        (240, 230, 140),  # 카키 - Success
        (238, 232, 170),  # 페일 골덴로드 - Enthusiasm
        (189, 183, 107),  # 다크 카키 - Adventure
        (255, 255, 240),  # 아이보리 - Belonging
        (245, 245, 220),  # 베이지 - Home
        (255, 248, 220),  # 콘실크 - Family
        (250, 250, 210),  # 연한 골덴로드 - Influence
        (255, 255, 224),  # 라이트 옐로우 - Free expression
        (255, 250, 205)   # 레몬 쉬폰 - Decisiveness
    ],

    # 청록색 영역 (Discovery, Balance, Understanding)
    'Joy, Sadness': [
        (152, 251, 152),  # 연한 민트색 - Serenity
        (0, 255, 255),    # 청록색 - Discovery
        (72, 209, 204),   # 중간 청록색 - Balance
        (32, 178, 170),   # 연한 청록색 - Understanding
        (95, 158, 160),   # 카뎃 블루 - Empathy
        (127, 255, 212),  # 아쿠아마린 - Calmness
        (64, 224, 208),   # 청록색 - Openness
        (0, 206, 209),    # 다크 청록색 - Flexibility
        (72, 209, 204),   # 중간 청록색 - Recovery
        (0, 139, 139),    # 다크 청록색 - Practicality
        (32, 178, 170),   # 라이트 시 그린 - Idealism
        (95, 158, 160)    # 카뎃 블루 - Change
    ]
})

emotion_color = []
i=0
for key, value in emotion_color_dict.items():
    i+=1
    emotion_color.append({
        'color_id':i,
        'emotions_name':key,
        'emotions_color':value,
    })

file_out('emotion_color', emotion_color)
