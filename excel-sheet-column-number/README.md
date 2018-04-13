# Leetcode: Excel Sheet Column Number     :BLOG:Basic:


---

Excel Sheet Column Number  

---

    Given a column title as appear in an Excel sheet, return its corresponding column number.
    
    For example:
    
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/excel-sheet-column-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/excel-sheet-column-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/excel-sheet-column-number
    ## Basic Ideas: Convert 26 bits
    ## Complexity: Time O(n), Space, O(1)
    class Solution(object):
        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            letter_dict = {}
            i = 1
            for ch in map(chr, range(ord('A'), ord('Z')+1)):
                letter_dict[ch] = i
                i = i + 1
    
            value = 0
            # print letter_dict
            for i in range(0, len(s)):
                ch = s[i]
                value = value * 26 + letter_dict[ch]
            return value
    
    if __name__ == '__main__':
        s = Solution()
        print s.titleToNumber("AA")
        print s.titleToNumber("AB")
        print s.titleToNumber("B")