s1 = "3people unFollowed me"
s2 = "for the last week"

# 공백 2개면 안됨ㅠ
# def solution(s):
#     l = list(map(str, s.split(' ')))
#     l3 = []
#     for i in range(len(l)):
#         l2 = list(l[i])
#         if (l2[0].isdigit() == False):
#             l2[0] = l2[0].upper()
#         for j in range(1, len(l2)):
#             l2[j] = l2[j].lower()
#         l3.append(''.join(l2))
#     s = ' '.join(l3)
#     return s


def solution(s):
    l = list(map(str, s.split(' ')))
    for i in range(len(l)):
        l[i] = l[i].capitalize()
    return ' '.join(l)


print(solution(s1))
