class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word
    
    def starts_with(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    

def main():
    words = ["Trie", "trie", "tree", "insert", "search"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    print(trie.search("tree"))  # True
    print(trie.search("word"))  # False
    print(trie.starts_with("tr"))   # True
    print(trie.starts_with("try"))  # False


if __name__ == '__main__':
    main()
