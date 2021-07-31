class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_available = False
        
class Trie():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        add_node = self.root
        for ch in word:
            if ch not in add_node.children:
                add_node.children[ch] = TrieNode()
            add_node = add_node.children[ch]
        add_node.is_available = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        search_word = self.root
        for ch in word:
            # print(f"character {ch} in {word}")
            if ch not in search_word.children:
                return False
            search_word = search_word.children[ch]
        return search_word.is_available
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        check_word = self.root
        for ch in prefix:
            if ch not in check_word.children:
                return False
            check_word = check_word.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
