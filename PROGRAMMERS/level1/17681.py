def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1_bin = bin(arr1[i])[2:]
        arr2_bin = bin(arr2[i])[2:]
        
        # n의 갯수만큼 앞에 0 채우기
        arr1_fin = ""
        for j in range(n - len(arr1_bin)):
            arr1_fin += "0"
        arr1_fin += arr1_bin
        
        arr2_fin = ""
        for j in range(n - len(arr2_bin)):
            arr2_fin += "0"
        arr2_fin += arr2_bin
        
        # #으로 채울지 공백으로 채울지
        arr = ""
        for j in range(n):
            if (arr1_fin[j] == '1') or (arr2_fin[j] == '1'):
                arr += "#"
            else:
                arr += " "
        answer.append(arr)
    return answer


# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # i, j를 비트 or 연산한 뒤에 [2:]로 '0b'부분을 제거한다.
        a12=a12.rjust(n,'0') # n에 맞게 오른쪽으로 졍렬하고, 부족한 부분은 '0'으로 채운다.
        a12=a12.replace('1','#') # '1'을 '#'으로 대체하고,
        a12=a12.replace('0',' ') #'0'을 공백으로 대체한다.
        answer.append(a12) # 리스트에 추가한다.
    return answer