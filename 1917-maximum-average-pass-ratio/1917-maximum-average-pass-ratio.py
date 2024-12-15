class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []

        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heappush(pq, (-gain, p, t))

        for _ in range(extraStudents):
            p, t = pq[0][1] + 1, pq[0][2] + 1

            gain = (p + 1) / (t + 1) - p / t
            heapreplace(pq, (-gain, p, t))

        return sum(x[1] / x[2] for x in pq) / len(classes)