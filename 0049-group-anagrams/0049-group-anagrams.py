class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}

        for i in strs:
            x = "".join(sorted(i))
            
            if x in dicti:
                dicti[x].append(i)
            else:
                dicti[x] = [i]
        
        return list(dicti.values())