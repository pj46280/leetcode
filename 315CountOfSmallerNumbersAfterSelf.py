class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        def merge_special(left, right):
            i, j = 0, 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    counts[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                counts[left[i][1]] += j
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged


        def merge_sort(arr):
            # index of staring and last 
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge_special(left, right)

        arr = [(val, index) for index, val in enumerate(nums)]

        merge_sort(arr)
        return counts


