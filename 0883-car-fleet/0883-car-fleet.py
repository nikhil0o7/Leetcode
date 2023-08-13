class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = [[position[i],speed[i]] for i in range(len(position))]
        merged.sort(key= lambda x: -x[0])
        slst = (target - merged[0][0])/merged[0][1]
        reslt = 1
        for i in range(1 , len(position)):
            time = (target - merged[i][0])/merged[i][1]
            if time > slst:
                slst = time
                reslt+=1
        return reslt

