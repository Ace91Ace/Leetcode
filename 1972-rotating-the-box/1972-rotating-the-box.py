class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in box:
            start = 0
            for j in range(len(i)):
                if i[j] == '*':
                    i[start:j] = sorted(i[start:j] , reverse = True)
                    start = j + 1
            i[start:] = sorted(i[start:], reverse = True)

        def rotate(box):
            tran = [list(row) for row in zip(*box)]
            rot = [row[::-1] for row in tran]
            return rot
        
        return rotate(box)
        
        
