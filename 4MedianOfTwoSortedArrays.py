class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A

        total = len(A) + len(B)
        start, end = 0, len(A) - 1
        while True:
            x = (start + end) // 2
            y = (total) // 2 - x - 2

            aLeftMax = A[x] if x >= 0 else float("-infinity")
            bLeftMax = B[y] if y >= 0 else float("-infinity")
            aRightMin = A[x + 1] if (x + 1) < len(A) else float("infinity")
            bRightMin = B[y + 1] if (y + 1) < len(B) else float("infinity")

            if aLeftMax <= bRightMin and bLeftMax <= aRightMin:
                if total % 2 == 0:
                    return (max(aLeftMax, bLeftMax) + min(aRightMin, bRightMin)) / 2
                else:
                    return min(aRightMin, bRightMin)

            elif aLeftMax > bRightMin:
                end = x - 1
            else:
                start = x + 1

nums1 = input().split()
nums1 = [int(i) for i in nums1]
nums2 = input().split()
nums2 = [int(i) for i in nums2]

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))

