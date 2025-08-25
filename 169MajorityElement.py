class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, counter = 0, 0
        for val in nums:
            if counter == 0:
                res = val
            if val == res:
                counter += 1
            else:
                counter -= 1

        return res
