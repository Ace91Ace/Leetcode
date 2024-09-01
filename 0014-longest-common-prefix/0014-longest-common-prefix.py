class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorts = sorted(strs, key=len)
        pre = ""

        for i in range(len(sorts[0])):
            for j in range(1,len(sorts)):
                if sorts[0][i] != sorts[j][i]:
                    return pre
            pre += sorts[0][i]
        return pre
            