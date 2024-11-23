class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        dict = {"#":1, ".":0}
        gravity_box = []
        n = len(box)
        for j in range(n-1, -1, -1):
            row = box[j]
            n = len(row)
            new_row = ['.'] * n 
            obstacle_idx = n
            for i in range(n-1, -1, -1):
                if row[i]=="*":
                    new_row[i] = "*"
                    obstacle_idx = i
                elif row[i]=="#":
                    new_row[obstacle_idx-1]="#"
                    obstacle_idx-=1
            
            gravity_box.append(new_row)


        #shift
        res_box = []
        row = len(gravity_box)
        col = len(gravity_box[0])
        for j in range(col):
            new_r = []
            for i in range(0, row):
                new_r.append(gravity_box[i][j])
            res_box.append(new_r)

        return res_box


            

                    
