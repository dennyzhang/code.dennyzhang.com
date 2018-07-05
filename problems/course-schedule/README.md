
# Leetcode: Course Schedule     :BLOG:Medium:

---

Course Schedule  

---

There are a total of n courses you have to take, labeled from 0 to n - 1.  

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]  

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?  

For example:  

    2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.  

    2, [[1,0],[0,1]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.  

Note:  

1.  The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2.  You may assume that there are no duplicate edges in the input prerequisites.

Hints:  

1.  This problem is equivalent to finding if a cycle exists in a directed graph.
2.  Topological Sort via DFS
3.  Topological sort could also be done via BFS.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/course-schedule)  

Credits To: [leetcode.com](https://leetcode.com/problems/course-schedule/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/course-schedule
    class Solution(object):
        def canFinish(self, numCourses, prerequisites):
    	"""
    	:type numCourses: int
    	:type prerequisites: List[List[int]]
    	:rtype: bool
    	"""

