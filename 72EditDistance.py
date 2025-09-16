class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        hashMap = {}
        def edit(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if (i,j) in hashMap:
                return hashMap[(i,j)]
            if word1[i-1] == word2[j-1]:
                return edit(i-1, j-1)
            hashMap[(i,j)] = 1 + min(
                edit(i-1, j),
                edit(i, j-1),
                edit(i-1, j-1)
            )
            return hashMap[(i,j)]

        m, n = len(word1), len(word2)
        return edit(m, n)
        
