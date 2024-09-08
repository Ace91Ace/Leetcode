class Solution:  
    def myAtoi(self, s: str) -> int:  
        num, sign, index = [], 1, 0  
        
        s = s.strip()
        if index < len(s) and s[index] in ['-', '+']:  
            sign = -1 if s[index] == '-' else 1  
            index += 1  
        while index < len(s) and s[index].isdigit():  
            num.append(int(s[index]))  
            index += 1  
            
        if not num:  
            return 0  
        
        result = sign * reduce(lambda x, y: 10 * x + y, num)  
        return max(min(result, 2**31 - 1), -2**31) 