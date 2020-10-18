def Atm_queue(line1, persons):
    
    line1 = [int(number) for number in line1]
    persons = [int(number) for number in persons]
    
    return_ans = []
    
    for i in range(line1[0]):
        persons[i] = [persons[i], i+1]
    
    i = 0

    while(len(persons) > 0):

        if persons[i][0] <= line1[1]:
            return_ans.append(persons[i][1])
            persons.remove(persons[i])

        else:
            new_val = persons[i][0] - line1[1]
            persons.append([new_val,persons[i][1]])
            persons.remove(persons[i])

    return return_ans


class main():
  Num_input = int(input())

  for i in range(Num_input):
    line1 = input().split()
    persons = input().split()
    list1 = Atm_queue(line1, persons)
    print("Case #",i,':', list1)
