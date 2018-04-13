# Leetcode: Employee Importance     :BLOG:Basic:


---

Employee Importance  

---

Similar Problems:  
-   Tag: [graph](https://code.dennyzhang.com/tag/graph)

---

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.  

    For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
    They have importance value 15, 10 and 5, respectively. 
    Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. 
    
    Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.  

    Example 1:
    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11
    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:  
1.  One employee has at most one direct leader and may have several subordinates.
2.  The maximum number of employees won't exceed 2000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/employee-importance)  

Credits To: [leetcode.com](https://leetcode.com/problems/employee-importance/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/employee-importance
    ## Basic Ideas: BFS + hasmap
    ##         hasmap: find subordinate by id
    ##         visited_set: visited nodes
    ## Complexity: Time O(n), Space O(n)
    """
    # Employee info
    class Employee(object):
        def __init__(self, id, importance, subordinates):
            # It's the unique id of each node.
            # unique id of this employee
            self.id = id
            # the importance value of this employee
            self.importance = importance
            # the id of direct subordinates
            self.subordinates = subordinates
    """
    class Solution(object):
        def getImportance(self, employees, id):
            """
            :type employees: Employee
            :type id: int
            :rtype: int
            """
            m, visited_set, queue = {}, set([]), []
            for employee in employees: m[employee.id] = employee
    
            res = m[id].importance
            queue.append(id)
            visited_set.add(id)
            while len(queue) != 0:
                for i in xrange(len(queue)):
                    employee_id = queue[0]
                    del queue[0]
                    for subordinate_id in m[employee_id].subordinates:
                        if subordinate_id not in visited_set:
                            res += m[subordinate_id].importance
                            queue.append(subordinate_id)
                            visited_set.add(subordinate_id)
            return res