def solution(nums):
    set_num = len(set(nums)) # 중복 제거한 폰켓몬 종류의 수
    
    catch_num = len(nums) // 2 # 고를 수 있는 폰켓몬 수
    
    # 폰켓몬 종류의 수와 고를 수 있는 수 중에 교집합 하는 수가 정답이므로 둘 중 작은 게 답
    result = min(set_num, catch_num)
    
    return result