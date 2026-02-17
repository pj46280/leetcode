class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

        for char in t:
            if char not in hashMap: return False
            if hashMap[char] > 1:
                hashMap[char] -= 1
            else:
                del hashMap[char]

        s = sum(hashMap.values()) if len(hashMap.values()) >= 1 else 0

        return True if s == 0 else False
