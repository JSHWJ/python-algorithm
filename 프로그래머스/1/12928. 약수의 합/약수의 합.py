import math

def solution(n):
    answer = 0
    array = []
    temp = 0
    # 아이디어 : 1부터 제곱근 n까지 나눈다.
    # 아이디어 : 정수 n가 제곱근이면 해당 수를 하나 빼야함 
    
    for i in range(int(math.sqrt(n))):
        if n % (i+1) == 0:
            answer += i+1
            answer += n // (i+1)
            array.append(i+1)
            array.append(n // (i+1))
            
    if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
        answer -= int(math.sqrt(n))
        
    print(array)

    return answer


print(solution(101))
