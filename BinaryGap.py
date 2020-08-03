def toBinary(n):
    return bin(n).replace("0b","")
  
def solution(N):
    # write your code in Python 3.6
    min_count = 0
    max_count = 0
    number = toBinary(N)
    
    for i in range(0,len(number)):
      if(number[i] == '0'):
          min_count += 1
      elif(number[i] != '0'):
        if(min_count > max_count):
            max_count = min_count
            min_count = 0
    print(max_count)
    return max_count

def main():
  n = 74901729
  solution(n)

if __name__ == '__main__':
  main()
