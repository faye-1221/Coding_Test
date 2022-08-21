x, y, w, h = map(int, input().split(' '))
distance = list()

distance.append(x)  # 0과 x의 거리
distance.append(w-x)  # w와 x의 거리

distance.append(y)  # 0과 y의 거리
distance.append(h-y)  # h와 y의 거리

print(min(distance))

# 굳이 append까지는 안해도 됨..ㅎㅎ
#main(x, y, w-x, h-y)
