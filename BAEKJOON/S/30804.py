# 시간 초과: 문제 잘못 이해하고 다르게 풀다가 바꿔서 복잡해졌다..
# 처음부터 가락 잡았어도 시간초과 났을 것 같긴함.
# from collections import deque, Counter
# N = int(input())
# S = deque(map(int, input().split()))

# # 두 종류 이하의 탕후루인지 확인하는 method
# # 앞과 뒤의 과일을 빼는 method
# # 먼저 두 종류인지 확인 -> 앞 or 뒤를 빼고 -> 두 종류인지 확인

# # 두 종류면 많은 과일 개수 출력

# def check_two(S):
#     count = Counter(S)
#     # 두 종류 이하의 탕후루면
#     if len(count.values()) <= 2:
#         print(len(S))
#         return True
#     return False

# def popleftpop(S):
#     count = Counter(S)    
#     n = S.pop()
#     m = S.popleft()

#     # 둘 중에서 count가 큰 값
#     if count.get(n) < count.get(m):
#         S.appendleft(m)
#     else:
#         S.append(n)
    
#     if check_two(S):
#         return
#     else:
#         popleftpop(S)

# if not check_two(S):
#     popleftpop(S)

# 투포인터 풀이
# 리스트의 각 요소는 right 포인터가 한 번, left 포인터가 한 번씩 방문: 시간 복잡도는 O(n)
import sys

from collections import Counter

input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))

def max_tanghulu_length(S):
    left = 0  # 왼쪽 포인터
    right = 0  # 오른쪽 포인터
    max_len = 0  # 가장 긴 구간의 길이
    count = Counter()  # 각 문자의 빈도를 저장하는 Counter

    while right < len(S):
        count[S[right]] += 1  # 오른쪽 포인터가 가리키는 문자의 빈도 증가
        right += 1  # 오른쪽 포인터 확장

        # 두 종류 이상의 문자가 있을 경우
        while len(count) > 2:
            count[S[left]] -= 1  # 왼쪽 포인터가 가리키는 문자의 빈도 감소
            if count[S[left]] == 0:
                del count[S[left]]  # 빈도가 0인 문자는 삭제
            left += 1  # 왼쪽 포인터 축소

        # 현재 구간의 길이를 계산하고 최대 길이 갱신
        max_len = max(max_len, right - left)

    return max_len
print(max_tanghulu_length(S))