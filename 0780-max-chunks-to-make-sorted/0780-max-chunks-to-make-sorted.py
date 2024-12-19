class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        c = diff = 0

        for i in range(len(arr)):
            x = arr[i]
            diff += x-i
            c += (diff == 0)
        return c