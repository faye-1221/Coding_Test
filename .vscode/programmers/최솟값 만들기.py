from itertools import product

A = [1, 4, 2]
B = [5, 4, 4]


def solution(A, B):
    com = list(product(A, B))
    print(com)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer


print(solution(A, B))
