class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        x = sentence.split()
        y = []
        for i in x:
            y.append(i[0])
            y.append(i[-1])
        m = y.pop(0)
        y.append(m)
        for i in range(0,len(y),2):
            if y[i] != y[i+1]:
                return False
        print(y)
        print(x)
        return True