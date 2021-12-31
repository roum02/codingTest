def solution(schedule):

  mon = []

  for i in range(len(schedule)): 
    for j in range(len(schedule[i])) :
      if len(schedule[i][j])>8:
        #print(schedule[i][j])
        pass
      else:
        if schedule[i][j][:2] == "MO":
          time = int(schedule[i][j][4:])
          mon.append(time)
          print(mon)

    print()

    #answer = -1
    #return answer

print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], 
["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], 
["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], 
["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], 
["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))