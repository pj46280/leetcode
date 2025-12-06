class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        # [9,4,1,3,7]
        dp = [0] * (n+1)
        prefix = [0] * (n+1)
        window = SortedList()
        dp[0] = 1
        prefix[0] = 1
        j = 0
        for i in range(n):
            window.add(nums[i])
            while j <= i and window[-1] - window[0] > k:
                window.remove(nums[j])
                j += 1
                
            dp[i+1] = (prefix[i] - (prefix[j-1] if j > 0 else 0)) % MOD
            prefix[i+1] = (prefix[i] + dp[i+1]) % MOD

        return dp[n]

