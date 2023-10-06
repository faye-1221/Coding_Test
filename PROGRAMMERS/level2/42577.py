# 효율성 테스트 실패
def solution(phone_book):
    phone_book.sort(key=lambda x : len(x))
    
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True

# 효율성 테스트 성공
def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True