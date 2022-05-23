class Node:
    
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    
    def __init__(self) -> None:
        self.root = self.get_node()
    
    def get_node(self) -> Node:
        return Node()
        
    @classmethod
    def char_to_index(cls, ch):
        return ord(ch) - ord('a')
    
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = self.get_node()
            current = current.children[letter]
        current.is_end = True
    
    def search(self, word):
        current = self.root
        for letter in word:
            # index = Trie.char_to_index(key[level])
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_end
 

# driver function
def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    words = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for word in words:
        t.insert(word)
 
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()
