# https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726-2xn-%ED%83%80%EC%9D%BC%EB%A7%81-%ED%95%B4%EC%84%A4-python
n = int(input())

cache = [0] * 1001

cache[1] = 1
cache[2] = 2

for i in range(3, 1001):
    cache[i] = (cache[i-1] + cache[i-2]) % 10007

print(cache[n])