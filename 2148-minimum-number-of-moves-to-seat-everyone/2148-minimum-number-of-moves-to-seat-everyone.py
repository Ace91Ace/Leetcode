class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        diff = 0
        for i in range(len(seats)):
            diff += abs(seats[i]-students[i])
        return diff