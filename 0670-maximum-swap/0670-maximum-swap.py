class Solution:  
    def maximumSwap(self, num: int) -> int:  
        num = list(str(num))  
        x = sorted(num)[::-1]  

        for i in range(len(num)):  
            if num[i] != x[i]:  
                y = len(num) - 1 - num[::-1].index(x[i])
                num[i], num[y] = num[y], num[i]  
                break  

        return int(''.join(num))   

