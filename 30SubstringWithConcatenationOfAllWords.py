from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        k = len(words[0])
        m = len(words)
        total_len = m*k
        n = len(s)
        need = Counter(words)
        res = []

        for offset in range(k):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, n-k+1, k):
                word = s[right:right+k]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        left_word = s[left:left+k]
                        seen[left_word] -= 1
                        count -= 1
                        left += k

                    if count == m:
                        res.append(left)
                        left_word = s[left:left+k]
                        seen[left_word] -= 1
                        left += k
                        count -= 1

                else:
                    seen.clear()
                    count = 0
                    left = right+k

        return res




# string = "barfoothefoobarman"
# words = ["foo","bar"]

# string = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

string = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]


s = Solution()
print(s.findSubstring(string, words))

'''
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        k = len(words[0])
        total_len = k * len(words)
        res = []
        
        for i in range(0, len(s) - total_len + 1):
            window = s[i:i+total_len]
            j = 0
            counter = 0

            while j < total_len:
                word = window[j:j+k]
                if word in words:
                    counter += 1
                    j += k
                else:
                    break
            
            if counter == len(words):
                res.append(i)

        return res
'''
