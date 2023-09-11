class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        target = 0
        jewels = sorted(jewels)
        for jewel in jewels:
            if jewel in stones:
                target += stones.count(jewel)
        return target
                
        