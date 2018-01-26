# Leetcode: Basic Calculator III     :BLOG:Hard:


---

Basic Calculator III  

---

Similar Problems:  
-   Tag: [#stack](http://brain.dennyzhang.com/tag/stack)

---

Implement a basic calculator to evaluate a simple expression string.  

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .  

The expression string contains only non-negative integers, +, -, \*, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.  

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].  

    Some examples:
    
    "1 + 1" = 2
    " 6-4 / 2 " = 4
    "2*(5+5*2)/3+(6/2+8)" = 21
    "(2+6* 3+5- (3*14/7+2)*5)+3"=-12

Note: Do not use the eval built-in library function.  
Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/basic-calculator-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/basic-calculator-iii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/basic-calculator-iii
    ## Basic Ideas: +- yield to */
    ##
    ##           When we found one operator as +/, look for the next operator
    ##           When we found one operator as */, we solve it immediately
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def calculate(self, s):
            """
            :type s: str
            :rtype: int
            """
            stack = 
            s = s.replace(' ', '')
            i, length = 0, len(s)
            while i<length:
                # print stack
                ch = s[i]
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    str_temp = stack.pop()
                    stack.pop() # (
                    str_temp = str(self.calculate_no_parenthese(str_temp))
                    if len(stack) != 0 and (stack[-1] != '('):
                        stack[-1] = "%s%s" % (stack[-1], str_temp)
                    else:
                        stack.append(str_temp)
                else:
                    str_temp = ''
                    while i<length and s[i] not in '()':
                        str_temp = '%s%s' % (str_temp, s[i])
                        i += 1
                    if len(stack) != 0 and (stack[-1] != '('):
                        stack[-1] = "%s%s" % (stack[-1], str_temp)
                    else:
                        stack.append(str_temp)
                    continue
                i += 1
            return self.calculate_no_parenthese(stack[0])
    
        def calculate_no_parenthese(self, s):
            """
            :type s: str
            :rtype: int
            """
            """
            :type s: str
            :rtype: int
            """
            s = s.replace(' ', '')
            s = s.replace('--', '+')
            i = 0
            length = len(s)
            # solve */
            stack = 
            while i<length:
                if s[i].isdigit():
                    # get the num
                    num_str = ''
                    while i<length and s[i].isdigit():
                        num_str = "%s%s" % (num_str, s[i])
                        i += 1
                    stack.append(num_str)
                elif s[i] in '*/':
                    num1 = int(stack.pop())
                    num_str = ''
                    op = s[i]
                    # find the next number
                    i += 1
                    while i<length and s[i].isdigit():
                        num_str = "%s%s" % (num_str, s[i])
                        i += 1
                    num2 = int(num_str)
                    if op == '*':
                        num1 = num1*num2
                    else:
                        num1 = num1/num2
                    stack.append(str(num1))
                else:
                    # +-
                    stack.append(s[i])
                    i += 1
    
            # solve +-
            res, i = 0, 0
            while i<len(stack):
                element = stack[i]
                if element in '+-':
                    num2 = stack[i+1]
                    i = i+2
                    if element == '+':
                        res += int(num2)
                    else:
                        res -= int(num2)
                else:
                    res += int(element)
                    i += 1
            return res
    
    s = Solution()
    print s.calculate(" 2-(5-6) ") # 3
    print s.calculate("2*(5+5*2)/3+(6/2+8)") # 21
    print s.calculate(" 3+5 / 2 ") # 5
    print s.calculate("1 + 1") # 2
    print s.calculate(" 6-4 / 2 ") # 4
    print s.calculate("(2+6* 3+5- (3*14/7+2)*5)+3") # -12
    print s.calculate("1-(2+3-(4+(5-(1-(2+4-(5+6))))))") # -1