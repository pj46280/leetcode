class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                spaces = i - last_one - 1
                if spaces < k and last_one >= 0:
                    return False
                last_one = i


        return True
                    
                
