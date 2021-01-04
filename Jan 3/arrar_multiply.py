# Write a program that takes two arrays representing integers, and retums an integer representing their product. 
# For example, since 193707721.x -761838257287 = -147573952589676412927, if the inputs are [1,9,3,7,0,7,7,2,1] and [-7,6,1,8,3,8,2,5,7,2,8,7], 
# your function should return [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]

arr1 = [1,9,3,7,0,7,7,2,1]
arr2 = [-7,6,1,8,3,8,2,5,7,2,8,7]

def multiply(arr1, arr2):
  num1 = 0

  for i in arr1:
    num1 = abs(num1 * 10) + i

  num2 = 0

  for i in arr2:
    num2 = abs(num2 * 10) + i

  # print()
  ans = num1 * num2
  ans_arr = []

  for i in str(ans):
      ans_arr.append(int(i))

  if arr1[0] < 0 or arr2[0] < 0:
    ans_arr[0] = ans_arr[0] * -1

  print(ans_arr)

multiply(arr1, arr2)
