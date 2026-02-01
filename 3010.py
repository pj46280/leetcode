class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if nums[1] < nums[2]:
            first, second = 1, 2
        else:
            first, second = 2, 1
    
        for i in range(3, len(nums)):
            if nums[i] < nums[first]:
                second = first
                first = i
            elif nums[i] < nums[second]:
                second = i
    
        return nums[0] + nums[first] + nums[second]
