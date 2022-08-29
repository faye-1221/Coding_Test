# 예시가 245의 분하햅은 245+2+4+5 = 256의 생성자는 245이다
# 예제 입력 1인 216의 생성자를 구한다.
N = int(input())

for i in range(1, N+1):  # 1부터 217까지 돈다
    A = list(map(int, str(i)))  # A에 i를 각각 나눠서 list로 가진다
    result = i+sum(A)  # result에 i와 각각 나눈 A를 합친다
    if result == N:  # result와 N이 같으면 i를 출력한다.
        print(i)
        break

    if i == N:  # i와 N이 같으면 0을 출력한다.
        print(0)
