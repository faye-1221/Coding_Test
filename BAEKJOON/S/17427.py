import sys
input = sys.stdin.readline

n = int(input())

sum = 0
for i in range(1, n+1):
    # i의 배수의 개수 = i를 약수로 갖는 수
    sum += (n//i)*i

print(sum)

# https://enhjh.tistory.com/37
# N의 배수는 N을 항상 약수로 갖는다.
# N 이하의 자연수 중에서 i를 약수로 갖는 개수는 N/i이다.

# g(N) = 1*N/1+2 * N/2 + ... + N*N/N