class Solution:
    def fullJustify(self, words: list[str], maxWidth: int):
        widthCounter = 0
        lineCounter = 1
        output = [""]

        for word in words:
            l = len(word)
            #print(word, l, maxWidth-widthCounter)
            if (maxWidth - widthCounter) > l:
                widthCounter += l+1
                output[lineCounter-1] += word + " "
            elif (maxWidth - widthCounter) == l:
                widthCounter += l
                output[lineCounter-1] += word
            else:
                widthCounter = 0
                lineCounter += 1
                output.append("")
                if (maxWidth - widthCounter) > l:
                    widthCounter += l+1
                    output[lineCounter-1] += word + " "
                elif (maxWidth - widthCounter) == l:
                    widthCounter += l
                    output[lineCounter-1] += word


        return output

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, length = [], 0
        i = 0
        res = []

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                spaces_left = maxWidth - length
                # number of spaces that would go between len(line) words
                spaces = spaces_left // max(1, len(line) - 1) 
                # extra spaces
                remainder = spaces_left % max(1, len(line)-1)
                for j in range(max(1, len(line)-1)):
                    # for each word append spaces
                    line[j] += " "*spaces
                    if remainder:       # if spaces remain append them from left side
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                length, line = 0, []

            line.append(words[i])
            length += len(words[i])
            i += 1

        last_line = " ".join(line)
        spaces = maxWidth - len(last_line)
        res.append("".join(last_line+" "*spaces))

        return res

# [
#    "This1234is1234an",
#    "example12of1text",
#    "justification.12"
# ]
['This is an ', 'example of text ', 'justification. ']

# for each word increament the count + 1 for space
# if count > maxWidth: new line


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# words = ["Here","is","an","example","of","text","justification."]
# maxWidth = 14

s = Solution()
print(s.fullJustify(words, maxWidth))

