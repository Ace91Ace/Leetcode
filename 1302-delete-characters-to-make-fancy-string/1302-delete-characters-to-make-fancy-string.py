class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        c = s[0]
        x = [s[0]]
        flag = 0
        for i in range(1,len(s)):
            if s[i] == c and flag == 0:
                print(s[i])
                x.append(s[i])
                flag = 1
            elif s[i] != c:
                print(s[i])
                x.append(s[i])
                flag = 0
            c = x[-1]
        return ''.join(x)
            
