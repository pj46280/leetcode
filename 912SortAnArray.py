class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        def merge(l, mid, r, arr):
            left = arr[l:mid+1]
            right = arr[mid+1:r+1]
            i, j, k = 0, 0, l

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            return arr

        def merge_sort(l, r, arr):
            if l < r:
                mid = (l + r) // 2
                merge_sort(l, mid, arr)
                merge_sort(mid+1, r, arr)
                return merge(l, mid, r, arr)

        return merge_sort(0, len(nums)-1, nums)

