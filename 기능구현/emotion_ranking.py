import random

퍼센테이지 = [(random.random(), i) for i in range(1, 8)]

print(퍼센테이지)

퍼센테이지.sort(reverse=True)
기준값 = 퍼센테이지[0][0] * 0.7

상위퍼센테이지 = [퍼센테이지[0]]
for i in range(1, 3):
    if 퍼센테이지[i][0] >= 기준값:
        상위퍼센테이지.append(퍼센테이지[i])

상위감정 = [상위퍼센테이지[i][1] for i in range(len(상위퍼센테이지))]
print(상위퍼센테이지)
print(상위감정)