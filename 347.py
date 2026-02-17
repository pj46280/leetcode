class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for n in nums:
            if n in hashMap: hashMap[n] += 1
            else: hashMap[n] = 1

        bucket = [[] for i in range(len(nums)+1)]
        for key, value in hashMap.items():
            bucket[value].append(key)

        res = []

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k: return res
