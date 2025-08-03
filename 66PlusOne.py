class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        p = len(digits) - 1
        digits[p], carry = (digits[p] + 1)%10, (digits[p] + 1)//10
        while carry > 0 and p > 0:
            p -= 1
            digits[p] = digits[p] + carry
            carry = digits[p]//10
            digits[p] = digits[p]%10

        return [carry] + digits if carry else digits

# 2 1 9
# p=9,c=0 -> n=0,c=1
# p=1,c=1 -> n=2,c=0
# p=2,c=0 -> n=2,c=0

lst = input().split(',')
lst = [int(i) for i in lst]
s = Solution()
print(s.plusOne(lst))
