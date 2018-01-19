# Leetcode: Student Attendance Record I     :BLOG:Basic:


---

Check string pattern  

---

You are given a string representing an attendance record for a student. The record only contains the following three characters:  
1.  'A' : Absent.
2.  'L' : Late.
3.  'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).  

You need to return whether the student could be rewarded according to his attendance record.  

    Example 1:
    Input: "PPALLP"
    Output: True

    Example 2:
    Input: "PPALLL"
    Output: False

Blog link: <http://brain.dennyzhang.com/student-attendance-record-i>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Useful link: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: One pass
    ##              absent: counter of absent records
    ##              max_continuous_late: counter of continous late
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def checkRecord(self, s):
            """
            :type s: str
            :rtype: bool
            """
            a, l = 0, 0
            for ch in s:
                if ch == 'A':
                    a += 1
                if ch == 'L':
                    l += 1
                else:
                    l = 0
                if a >= 2 or l >= 3:
                    return False
            return True
    
        def checkRecord_v2(self, s):
            return s.count('A') <= 1 and s.count('LLL') == 0
    
        def checkRecord_v1(self, s):
            """
            :type s: str
            :rtype: bool
            """
            absent = 0
            max_continuous_late, current_continuous_late = 0, 0
            previous_late = False
            for ch in s:
                if ch == 'L':
                    if previous_late:
                        current_continuous_late += 1
                    else:
                        previous_late = True
                        current_continuous_late = 1                    
                else:
                    previous_late = False
                    if current_continuous_late > max_continuous_late:
                        max_continuous_late = current_continuous_late
                    current_continuous_late = 0
                # tail of L
                max_continuous_late = max(max_continuous_late, current_continuous_late)
                if ch == 'A':
                    absent += 1
            return absent <= 1 and max_continuous_late <= 2
    
    s = Solution()
    print s.checkRecord('PPALLP')
    print s.checkRecord('PPALLL')
    print s.checkRecord('PPALLP')

More Reading:  
-   [[<http://brain.dennyzhang.com/student-attendance-record-i>