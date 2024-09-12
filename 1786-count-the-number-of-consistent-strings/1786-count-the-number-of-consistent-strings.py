class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words :
            if all(j in allowed for j in i ):
                count+=1
        return count