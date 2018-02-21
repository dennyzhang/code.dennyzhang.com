# Leetcode: Two Sum III - Data structure design     :BLOG:Medium:


---

Two Sum III - Data structure design  

---

Similar Problems:  
-   Tag: [#oodesign](https://brain.dennyzhang.com/tag/oodesign)

---

Design and implement a TwoSum class. It should support the following operations: add and find.  

add - Add the number to an internal data structure.  
find - Find if there exists any pair of numbers which sum is equal to the value.  

For example,  

    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/two-sum-iii-data-structure-design)  

Credits To: [leetcode.com](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/two-sum-iii-data-structure-design
    ## Basic Ideas: hashmap
    ##
    ## Complexity: Time O(n), Space O(n)
    import collections
    class TwoSum:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.m = collections.defaultdict(lambda: 0)
    
        def add(self, number):
            """
            Add the number to an internal data structure..
            :type number: int
            :rtype: void
            """
            self.m[number] += 1
    
        def find(self, value):
            """
            Find if there exists any pair of numbers which sum is equal to the value.
            :type value: int
            :rtype: bool
            """
            for v in self.m:
                complement_v = value - v
                if v == complement_v:
                    if self.m[v] >= 2: return True
                else:
                    if complement_v in self.m: return True
            return False
    
    # Your TwoSum object will be instantiated and called as such:
    # obj = TwoSum()
    # obj.add(number)
    # param_2 = obj.find(value)