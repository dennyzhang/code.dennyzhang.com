# LintCode: Input Stream     :BLOG:Basic:


---

Input Stream  

---

Similar Problems:  
-   Tag: [#stack](https://code.dennyzhang.com/tag/stack)

---

Give two input stream inputA and inputB, which have Backspace. If the final result of the two input streams is equal, output YES, otherwise output NO.  

Notice  
-   Input characters include only lowercase letters and '<'
-   The length of input stream does not exceed 10000.

Example  

    Given inputA = “abcde<<”, inputB = “abcd<e<”, return "YES".
    
    Explanation:
    The final result of inputA and inputB is abc, so return "YES".

    Given inputA = “a<<bc”, inputB = “abc<”, return "NO"
    
    Explanation:
    The final result of inputA is "bc", and the final result of inputB is "ab", so return "NO".

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/input-stream)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/input-stream/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/input-stream
    #!/usr/bin/env python
    class Solution:
        """
        @param inputA: Input stream A
        @param inputB: Input stream B
        @return: The answer
        """
        def inputStream(self, inputA, inputB):
           # Basic Ideas: stack
            stack1, stack2 = [], []
            for ch in inputA:
                if ch == '<':
                    if len(stack1) != 0: stack1.pop(-1)
                else:
                    stack1.append(ch)
            for ch in inputB:
                if ch == '<':
                   if len(stack2) != 0:
                       stack2.pop(-1)
                else:
                    stack2.append(ch)
            return 'YES' if stack1 == stack2 else 'NO'