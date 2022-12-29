#A: 낮에 올라갈 수 있는 높이
#B: 밤에 미끄러지는 높이
#V: 막대 높이
#정상에 가면 밤에 미끄러지지 않음
import math
a, b, v = map(int, input().split())

day = math.ceil((v-a)/(a-b)) + 1
print(day)