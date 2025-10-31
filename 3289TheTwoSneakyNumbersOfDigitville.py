class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = 0

        for n in nums:
            x = x ^ n
        for i in range(len(nums)-2):
            x = x ^ i

        db = x & -x
        xor1, xor2 = 0, 0

        for n in nums:
            if n & db:
                xor1 = xor1 ^ n
            else:
                xor2 = xor2 ^ n
        for i in range(len(nums)-2):
            if i & db:
                xor1 = xor1 ^ i
            else:
                xor2 = xor2 ^ i

        return [xor1, xor2]


        
