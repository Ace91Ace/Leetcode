class Solution:  
    def maximumSwap(self, num: int) -> int:  
        num = list(str(num))  
        x = sorted(num)[::-1]  # sorted in descending order  

        for i in range(len(num)):  
            if num[i] != x[i]:  
                # Find the last occurrence of the character to swap  
                y = len(num) - 1 - num[::-1].index(x[i])  
                # Swap the characters  
                num[i], num[y] = num[y], num[i]  
                break  

        return int(''.join(num))   

