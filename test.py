class Solution:
    def mergeTwoLists(self, list1, list2):
        res = []
        j = 0
        for i in range(len(list1)):
            while j < len(list2):
                if list2[j] < list1[i]:
                    res.append(list2[j])
                    j += 1
                else:
                    break


l1 = [1, 2, 4]
l2 = [1, 3, 4]

s = Solution()
print(s.mergeTwoLists(l1, l2))

