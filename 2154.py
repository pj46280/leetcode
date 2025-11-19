class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hashMap = {}

        for n in nums:
            if n in hashMap: hashMap[n] += 1
            else: hashMap[n] = 1

        while True:
            if original not in hashMap.keys() or hashMap[original] == 0: return original
            # `` 
            original *= 2

        return original
            
