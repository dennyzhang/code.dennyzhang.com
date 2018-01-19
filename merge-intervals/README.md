# Leetcode: Merge Intervals     :BLOG:Basic:


---

Merge Intervals  

---

Given a collection of intervals, merge all overlapping intervals.  

    For example,
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].

Blog link: <http://brain.dennyzhang.com/merge-intervals>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def merge(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """
            ret = []
            for entry in sorted(intervals, key=lambda entry: entry.start):
                if ret and entry.start <= ret[-1].end:
                    ret[-1].end = max(ret[-1].end, entry.end)
                else:
                    ret.append(entry)
            return ret