# Leetcode: Reverse Words in a String II     :BLOG:Medium:


---

Reverse Words in a String II  

---

Similar Problems:  
-   Tag: [Rotate Array](https://code.dennyzhang.com/rotate-array)

---

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.  

The input string does not contain leading or trailing spaces and the words are always separated by a single space.  

For example,  

    Given s = "the sky is blue",
    return "blue is sky the".

Could you do it in-place without allocating extra space?  

Update (2017-10-16):  
We have updated the function signature to accept a character array, so please reset to the default code definition by clicking on the reload button above the code editor. Also, Run Code is now available!  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-words-in-a-string-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-words-in-a-string-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/reverse-words-in-a-string-ii
    ## Basic Ideas: Reverse string. Then find the groups, and reverse them.
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def reverseWords(self, str):
            """
            :type str: List[str]
            :rtype: void Do not return anything, modify str in-place instead.
            """
            length = len(str)
            self.myReverseString(str, 0, length-1)
    
            # find the groups seperated by whitespace
            left = 0
            for i in range(0, length):
                if i == length-1:
                    # no tailing whitespace
                    self.myReverseString(str, left, i)
                else:
                    if str[i] == ' ':
                        self.myReverseString(str, left, i-1)
                        left = i + 1
    
        def myReverseString(self, str, left, right):
            while left<right:
                str[left], str[right] = str[right], str[left]
                left, right = left+1, right-1