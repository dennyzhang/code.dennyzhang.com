# Leetcode: Meeting Rooms     :BLOG:Medium:


---

Meeting Rooms  

---

Similar Problems:  
-   [Meeting Rooms II](https://brain.dennyzhang.com/meeting-rooms-ii)
-   [Review: Interval Problems](https://brain.dennyzhang.com/review-interval)

---

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],&#x2026;] (si < ei), determine if a person could attend all meetings.  

For example,  
Given [[0, 30],[5, 10],[15, 20]],  
return false.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/meeting-rooms)  

Credits To: [leetcode.com](https://leetcode.com/problems/meeting-rooms/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/meeting-rooms
    ## Basic Ideas:
    ##
    ## Complexity: Time O(n*log(n)), Space O(1)
    ##
    # Definition for an interval.
    # class Interval:
    #     def __init__(self, s=0, e=0):
    #         self.start = s
    #         self.end = e
    
    class Solution:
        def canAttendMeetings(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: bool
            """
            length = len(intervals)
            if length <= 1: return True
            intervals.sort(key=lambda x: x.start)
            for i in range(1, length):
                if intervals[i].start < intervals[i-1].end:
                    return False
            return True