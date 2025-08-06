class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    # def merge(self, nums1, nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        while n>0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

        return nums1

# nums1 = [1, 1, 3, 3, 4, 0]
# nums2 = [2]
# nums1 = [1, 2, 3, 4, 0, 0]
# nums2 = [2, 5]
# nums1 = [1]
# nums2 = []

## Failing
nums1, m = [1,2,3,0,0,0], 3
nums2, n = [2,5,6], 3

s = Solution()
print(s.merge(nums1, m, nums2, n))


# nums1 = [1, 2, 3, 4, 0, 0] ; nums2 = [2, 5]
# nums1 = [1, 1, 3, 3, 4, 0] ; nums2 = [2]
