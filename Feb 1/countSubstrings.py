def countSubstrings(S):
  N = len(S) 
  ans = set([]) # needed as we ned to remember old elements
  S = S +'#' # used to traverse last element
  for center in range(2*N - 1):
      left = center // 2
      right = left + center % 2
      while left >= 0 and right < N and S[left] == S[right]:
          ans.add(S[left:right+1])
          left -= 1
          right += 1
  print(len(ans))
  return len(ans)

countSubstrings('aabaa')