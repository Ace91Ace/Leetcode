class Trienode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word) :
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.is_word = True

    def searchReplacePrefix(self, word):
        cur = self.root
        prefix = ""
        for c in word:
            if c not in cur.children:
                return word
            cur = cur.children[c]
            prefix += c
            if cur.is_word:
                return prefix
        return word


    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
 
        for w in dictionary:
            self.insert(w)
        words = sentence.split(" ")
        for i in range(len(words)):
            words[i] = self.searchReplacePrefix(words[i])

        return " ".join(words)

        
        