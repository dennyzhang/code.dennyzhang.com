# Leetcode: Solve the Equation     :BLOG:Medium:


---

Solve the Equation  

---

Similar Problems:  
-   [Expressive Words](https://brain.dennyzhang.com/expressive-words)
-   [Review: Math Problems](https://brain.dennyzhang.com/review-math)
-   [Review: Problems With Many Details](https://brain.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://brain.dennyzhang.com/tag/manydetails), [#math](https://brain.dennyzhang.com/tag/math)

---

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.  

If there is no solution for the equation, return "No solution".  

If there are infinite solutions for the equation, return "Infinite solutions".  

If there is exactly one solution for the equation, we ensure that the value of x is an integer.  

Example 1:  

    Input: "x+5-3+x=6+x-2"
    Output: "x=2"

Example 2:  

    Input: "x=x"
    Output: "Infinite solutions"

Example 3:  

    Input: "2x=x"
    Output: "x=0"

Example 4:  

    Input: "2x+3x-6x=x+2"
    Output: "x=-1"

Example 5:  

    Input: "x=x+2"
    Output: "No solution"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/solve-the-equation)  

Credits To: [leetcode.com](https://leetcode.com/problems/solve-the-equation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/solve-the-equation
    ## Basic Ideas:
    ##
    ##  2x+3x-6x=x+2
    ##  ["2x", "+3x", "-6x", "-x", "-2"]
    ##
    ## Assumptions: equation has valid format
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def solveEquation(self, equation):
            """
            :type equation: str
            :rtype: str
            """
            queue = 
            reverse = False
            myStr, sign = '', ''
            for ch in equation:
                if ch == '=': 
                    # add previous item
                    queue.append("%s%s" % ('-' if sign == '-' else '', myStr))
                    myStr, sign = '', ''
    
                    reverse = True
                    continue
    
                if ch in '+-':
                    if myStr == '':
                        if (ch == '-' and reverse is False) or \
                            (ch == '+' and reverse is True):
                            sign = '-'
                        else:
                            sign = '+'
                        continue
                    # add previous item
                    if sign == '' and reverse is True: sign = '-'
                    queue.append("%s%s" % ('-' if sign == '-' else '', myStr))
    
                    # get new item
                    myStr, sign = '', ''
                    if (ch == '-' and reverse is False) or \
                        (ch == '+' and reverse is True):
                        sign = '-'
                    else:
                        sign = '+'
                    continue
                myStr += ch
    
            if myStr != '': 
                if sign == '' and reverse is True: sign = '-'
                queue.append("%s%s" % ('-' if sign == '-' else '', myStr))
    
            # print(queue)
            x, v = 0, 0
            for item in queue:
                if item[-1] == 'x':
                    if item == '-x':
                        x -= 1
                    elif item == 'x':
                        x += 1
                    else:
                        x += int(item[0:-1])
                else:
                    v += int(item)
            v = -v
            if x == 0:
                if v != 0: return "No solution"
                else: return "Infinite solutions"
            else:
                return "x=%d" % (int(v/x))
    
    # s = Solution()
    # print(s.solveEquation("-x=-1")) # x=1
    # print(s.solveEquation("2x+3x-6x=x+2")) # x=-1
    # print(s.solveEquation("x=x+2")) # "No solution"
    # print(s.solveEquation("x=x")) # "Infinite solutions"