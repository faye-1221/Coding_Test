# 바깥으로 갈 수록 1, 6, 12, 18, 24개의 숫자가 둘러싼다. (6의 배수)
# 62부터 70까지는 6번 나아간다
# 이외는 6의 배수에 해당하는 값만큼...

n = int(input())
cnt = 1
room = 1
while (n > room):
    room += (6*cnt)
    cnt += 1

print(cnt)
