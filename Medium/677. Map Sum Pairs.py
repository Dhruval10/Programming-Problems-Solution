class TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0
        self.is_word = ''
        
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        add_word = self.root
        temp=val
        if key in self.map:
            val = val - self.map[key]
            
        self.map[key] = temp
        
        for ch in key:
            if ch not in add_word.children:
                add_word.children[ch] = TrieNode()
            add_word.total += val
            if add_word.is_word == key:
                add_word.total = val
            add_word = add_word.children[ch]

        add_word.total += val
        add_word.is_word = key

    def sum(self, prefix: str) -> int:
        search_word = self.root
        
        for ch in prefix:
            if ch not in search_word.children:
                return 0
            search_word = search_word.children[ch]
        return search_word.total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
