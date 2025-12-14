class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def count(index, seats):
            if index == len(corridor):
                return 1 if seats == 2 else 0

            if cache[index][seats] != -1:
                return cache[index][seats]

            if seats == 2:
                if corridor[index] == 'S':  # start new section as 2 seats included
                    res = count(index+1, 1)
                else:
                    # if current index is plant we can create new section or extended the current section
                    res = (count(index+1, 0) + count(index+1, 2)) % MOD
            else:
                # if number of seats so far is not 2 
                if corridor[index] == 'S':  # if current index is seat add it to seats
                    res = count(index+1, seats+1)
                else:
                    res = count(index+1, seats)
            
            cache[index][seats] = res

            return res

        return count(0, 0)

