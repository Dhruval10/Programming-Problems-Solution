def goodTuples(a):
  count = 0
  for i in range(1,len(a)-1):
    if a[i-1] == a[i] and a[i] == a[i+1]:
      continue
    elif a[i-1] == a[i] or a[i] == a[i+1] or a[i-1] == a[i+1]:
      count += 1
  print(count)
  return count

goodTuples([4,6,4,1,3,4]) # Output: 1
goodTuples([4,4,6,1,2,2,2,3]) # Output: 3
