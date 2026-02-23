class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers) - 1

        while ptr1 < ptr2:
            a, b = numbers[ptr1], numbers[ptr2]
            if a + b == target: 
                return [ptr1+1, ptr2+1]
            elif a + b < target:
                ptr1 += 1
            elif a + b > target:
                ptr2 -= 1

