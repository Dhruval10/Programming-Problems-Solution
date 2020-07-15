# Create Dictionary to count the number of occurrence of every digit in given number and also print which digit is not present in the number


#number = input('Number: ')

number = str(input('Enter Number: '))

# dict = {1:'',2:'',3:''}

dict = {}
count = 0

# count repetition of each key and if not present in the dict then add ket
for i in range(len(number)):
    if number[i] in dict:
        dict[number[i]] +=1
    else:
        dict[number[i]] = 1
print(dict)

# Check which number is not present in the dictionary
for i in range(0,10):
    if str(i) not in dict.keys():
        print("Not present in dictionary :",i)
    else:
        pass
