# week 2

def solution(scores):
    answer = ''
    unique = 0
    result = ""
    result_list = []
    
    # score 조건
    n = 0
    c = 0

    for k in range(0, len(scores[c])):
        if max(scores[c]) <= 100 and min(scores[c]) >= 0:
          if len(scores[k]) != len(scores):
            n += 1
        c += 1

    if (n == 0) and (len(scores) >= 2 and len(scores) <= 10):  

        for i in range(0, len(scores)):
            if ((scores[i][i] == max(scores[i])) or (scores[i][i] == min(scores[i]))) and ((scores[i].count(max(scores[i])) == 1) or (scores[i].count(min(scores[i])) == 1)):
              avg = (sum(scores[i]) - scores[i][i])/(len(scores[i])-1)
            else:
              avg = sum(scores[i])/len(scores[i])
                      
            if avg >= 90:
                result = "A"
            elif avg >= 80:
                result = "B"
            elif avg >= 70:
                result = "C"
            elif avg >= 50:
                result = "D"
            else:
                result = "F" 
            result_list.append(result)

    answer = ",".join(result_list)
      
    return answer

solution(	[[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]])