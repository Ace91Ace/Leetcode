class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        new_tp = []
        for ele in timePoints:
            h = int(ele[:2])
            m = int(ele[-2:])
            ele = h*60+m
            new_tp.append(ele)
            #new_tp.append(1440-ele)

        new_tp.sort()
        diff = []    
        for i in range(len(new_tp)-1):
            d = abs(new_tp[i]-new_tp[i+1])
            '''if d<720:
                diff.append(d)
            else:
                diff.append(1440-d)'''
            diff.append(d)
        last_first_diff = new_tp[-1]-new_tp[0]
        diff.append(1440-last_first_diff)
        
        return min(diff)

        