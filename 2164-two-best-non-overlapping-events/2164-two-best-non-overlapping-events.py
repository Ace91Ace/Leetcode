class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        mx = 0
        res = 0

        for s,e,v in events:
            while pq and pq[0][0] < s:
                mx = max(mx,heappop(pq)[1])
            res = max(res,mx + v)
            heappush(pq,(e,v))
        return res