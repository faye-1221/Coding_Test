# 2^N-1 × 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문
# r행 c열을 몇 번째로 방문했는지 출력

def z_search(n, r, c):
    if n == 0:
        return 0

    # 반으로 쪼갠다
    half = 2 ** (n - 1)

    # 왼쪽 위 사분면
    if r < half and c < half:
        return z_search(n - 1, r, c)
    # 오른쪽 위 사분면
    elif r < half and c >= half:
        return half * half + z_search(n - 1, r, c - half)
    # 왼쪽 아래 사분면
    elif r >= half and c < half:
        return 2 * half * half + z_search(n - 1, r - half, c)
    # 오른쪽 아래 사분면
    else:
        return 3 * half * half + z_search(n - 1, r - half, c - half)


n, r, c = map(int, input().split())

print(z_search(n, r, c))