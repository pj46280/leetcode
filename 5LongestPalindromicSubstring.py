class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            palindrome1 = self.scan(s, i, i)
            palindrome2 = self.scan(s, i, i+1)
            palindrome = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
            # print("p1, p2, palindrome: ", (palindrome1, palindrome2, palindrome))
            if len(palindrome) > len(longest):
                longest = palindrome

        return longest

    def scan(self, s, start, end):
        palindrome = ""
        while start >= 0 and end < len(s) and s[start] == s[end]:
            current = s[start:end+1]
            start -= 1
            end += 1
            if len(current) > len(palindrome):
                palindrome = current

        return palindrome

string = input()
s = Solution()
print(s.longestPalindrome(string))
