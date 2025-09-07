class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        for i in range(2, n+1):
            next_string = ""
            index = 0
            while index < len(current):
                count = 1
                while (index+1) < len(current) and current[index] == current[index+1]:
                    count += 1
                    index += 1
                next_string += str(count) + current[index]
                index += 1

            current = next_string

        return current


s = Solution()
print(s.countAndSay(n=5))
