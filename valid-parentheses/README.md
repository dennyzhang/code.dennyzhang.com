# Leetcode: Valid Parentheses     :BLOG:Basic:


---

Valid Parentheses  

---

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-parentheses)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-parentheses/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/valid-parentheses
    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            matched_dict = {
                '(': ')',
                ')': '(',
                '[': ']',
                ']': '[',
                '{': '}',
                '}': '{'
            }
    
            string_stack = []
    
            for ch in s:
                if ch not in '()[]{}':
                    raise Exception("Unexpected string: %s, character: %s" % (s, ch))
                if len(string_stack) == 0:
                    string_stack.append(ch)
                else:
                    if string_stack[-1] == matched_dict[ch]:
                        # pop the last item
                        string_stack.pop()
                    else:
                        string_stack.append(ch)
            return len(string_stack) == 0
    
    if __name__ == '__main__':
        s = Solution()
        print s.isValid("([])")
        print s.isValid("()[]{}")
        print s.isValid("()")
        print s.isValid("(]")
        print s.isValid("([)]")