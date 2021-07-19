class Solution:
  def __init__(self):
    self.head = {}
  
  def add_word(self,word):
    addWord = self.head
    for ch in word:
      if ch not in addWord:
        addWord[ch] = {}
      addWord = addWord[ch]
    addWord['*'] = True
  
  def search_word(self,word):
    search_word = self.head
    for ch in word:
      if ch not in search_word:
        return False
      search_word = search_word[ch]
    if search_word['*'] == True:
      return True
    else:
      return False
  
  def print(self):
    print(self.head)
    
obj1 = Solution()
obj1.add_word("banana")
obj1.add_word("ball")
obj1.add_word("all")
obj1.add_word("act")
obj1.add_word("active")
obj1.add_word("activa")
print(obj1.search_word("activa"))
obj1.print()
