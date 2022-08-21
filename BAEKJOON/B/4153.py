# a,b,c인 삼각형에서 a^2 + b^2 = c^2(가장긴변) 이면 직각 삼각형! => 피타고라스의 정리

from statistics import median
while (True):
    l = list()
    l = list(map(int, (input().split(' '))))

    if sum(l) == 0:
        break
    elif (max(l) ** 2) == ((min(l) ** 2) + (median(l) ** 2)):
        print("right")
    else:
        print("wrong")
