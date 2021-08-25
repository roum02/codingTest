# week 2

def solution(scores):
    answer = ''
    
    # score 조건

    unique = 0

    for i in range(0, len(scores)):
      for j in range(0, len(scores)):
        if (i == j) and ((scores[i][j] == max(scores[i])) or (scores[i][j] == min(scores[i]))) and ((scores[i].count(max(scores[i])) == 1) or (scores[i].count(min(scores[i])) == 1)):
          avg = (sum(scores[i]) - scores[i][j])/(len(scores[i])-1)
          print(avg)
        else:
          avg = sum(scores[i])/len(scores[i])
          print(avg)
    
    #return unique


solution([[70,90,90],[68,50,38],[73,31,100]])