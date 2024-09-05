class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            if s == goal:
                return True
            goal = goal[-1] + goal[:-1]
        return False