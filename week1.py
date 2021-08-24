def solution(price, money, count):

    answer = -1
    price = int(price)
    money = int(money)
    count = int(count)
    
    if (price >= 1 and price <= 2500) and (money >= 1 and money <= 1000000000) and (count >= 1 and count <= 2500):
    
        result = []
        n = 1
        while n < (count+1):
            result.append(price * n)
            n = n + 1

            answer = money - sum(result)
            if answer > 0:
                answer = 0
            elif answer < 0:
                answer = abs(money - sum(result))
            
    return answer

solution(3,20,4)

