class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        closest_sum = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s-target)
                if diff < distance:
                    distance = diff
                    closest_sum = s
                # distance = min(diff, distance)
                if s < target:
                    l += 1
                else:
                    r -= 1

        return closest_sum
