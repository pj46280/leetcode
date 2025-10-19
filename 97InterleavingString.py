class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        d = {}
        ptr1, ptr2 = (0, 0)

        def backtrack(ptr1, ptr2):
            if ptr1 == len(s1) and ptr2 == len(s2):
                return True

            if (ptr1, ptr2) in d:
                return d[ptr1, ptr2]

            if ptr1 < len(s1) and s1[ptr1] == s3[ptr1+ptr2] and backtrack(ptr1+1,ptr2):
                d[(ptr1, ptr2)] = True
                return True
            if ptr2 < len(s2) and s2[ptr2] == s3[ptr1+ptr2] and backtrack(ptr1,ptr2+1):
                d[(ptr1, ptr2)] = True
                return True

            d[(ptr1, ptr2)] = False
            return False
            
        return backtrack(ptr1, ptr2)

