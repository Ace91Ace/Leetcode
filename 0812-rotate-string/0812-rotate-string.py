class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if goal == s:
                return True
            goal = goal[1::] + goal[0]
        return False