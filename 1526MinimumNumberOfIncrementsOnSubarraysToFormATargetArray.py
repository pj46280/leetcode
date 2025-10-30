class Solution:
    def minNumberOperations(self, target) -> int:
    # find the minimum, start with that many operations
    # keep incrementing operations count with numbers 
    # until it start to decrease to minimum, then if it increase 
    # for every increase add 1

        operations = target[0]
        for i in range(1, len(target)):
            if target[i-1] < target[i]:
                oprtations += target[i] - target[i-1]

        return operations


# 1 2 3 2 1 1 2 3 1 2
target = [3, 2, 1]
# 1 1 2 2 3

#target = [1,2,3,2,1]
# target = [3, 1, 1, 2]
s = Solution()
print(s.minNumberOperations(target))

