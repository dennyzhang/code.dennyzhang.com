# Leetcode: Valid Number     :BLOG:Medium:


---

Validate if a given string is numeric.  

---

Validate if a given string is numeric.  

Some examples:  
-   "0" => true
-   " 0.1 " => true
-   "abc" => false
-   "1 a" => false
-   "2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-number/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas
    ##      Data clean first
    ##      Make sure it only has valid character
    ##      integer, float, scientific notation
    ## Complexity
    ## Assumptions:
    ##      00: True
    ##      -2: True
    ##      +2: True
    ##  ' -+ ': False
    ##  12341467980: False too long
    ##   '12.': True
    ##   '.12': True
    ##   '.': False
    ##   'e': False 
    ##   '21e': False
    ##   'e12': False
    ##   '46.e3': True
    ##   '.e1': False
    ##  '46.e3': True
    ##  '.2e81': True
    ##  '6e6.5': False
    ##  ' 005047e+6': True
    ##  'e+8': False
    class Solution(object):
        def isNumber(self, s):
            """
            :type s: str
            :rtype: bool
            """
            s = s.strip()
            if s == "":
                return False
            valid_list = "0123456789.e-+"
            dot_count, e_count = 0, 0
            n_count, p_count = 0, 0
            d_count = 0
            for ch in s:
                if ch not in valid_list:
                    return False
                if ch == '.':
                    dot_count += 1
                if ch == 'e':
                    e_count += 1
                if ch == '-':
                    n_count += 1
                if ch == '+':
                    p_count += 1
                if ch in '0123456789':
                    d_count += 1
    
                # fast fail
                if dot_count > 1 or e_count > 1 \
                    or n_count > 1 or p_count > 1:
                        return False
    
            if d_count == 0:
                return False
            if n_count == 1 and p_count == 1:
                return False
            # negative
            if n_count != 0:
                if s[0] != '-':
                    return False
                s = s[1:]
    
            # positive
            if p_count != 0:
                if e_count == 0:
                    if s[0] != '+':
                        return False
                if s.find('e+') != -1:
                    return False
                s = s[1:]
    
            max_int_digit = 28
            # too long
            if len(s) > max_int_digit:
                return False
    
            if dot_count == 0:
                # all number
                if e_count == 0:
                    if len(s) > max_int_digit:
                        return False
                else:
                    # scientific notation
                    if s[-1] == 'e' or s[0] == 'e' or s == 'e':
                        return False
            else:
                # dot_count must be 1
                if e_count != 0:
                    # scientific float
                    if s.find('.e') == 0:
                        return False
                    if s[-1] == 'e' or s[0] == 'e' or s == 'e':
                        return False
                    if s.find('.') > s.find('e'):
                        return False
                if s == '.':
                    return False
    
            return True
    
    s = Solution()  
    print s.isNumber('0') # true
    print s.isNumber(' 0.1 ') # true
    print s.isNumber('abc') # false
    print s.isNumber('1 a') # false
    print s.isNumber('2e10') # true
    print s.isNumber(' 001 ') # true
    print s.isNumber(' -1. ') # true
    print s.isNumber('  005047e+6') # true
    print s.isNumber('  e+ ') # false
    print s.isNumber('  e+8') # false
    print s.isNumber('  e2+') # true