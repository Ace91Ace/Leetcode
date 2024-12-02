class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i,word in enumerate(sentence) :
            print(word[0:len(searchWord)])
            if word[0:len(searchWord)] == searchWord:
                return i + 1
        return -1