class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 1

        while res < n:
            res = (res << 1) | 1

        return res

        
        # we take then 1, shift it left, or it to 1
        '''
        def find_x(res):
            if res >= n:
                return res
            res <<= 1
            res = res | 1

            return find_x(res)

        return find_x(1) 
        '''
