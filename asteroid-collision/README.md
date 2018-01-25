# Leetcode: Asteroid Collision     :BLOG:Medium:


---

Asteroid Collision  

---

Similar Problems:  
-   Tag: [#basic](http://brain.dennyzhang.com/tag/basic)

---

We are given an array asteroids of integers representing asteroids in a row.  

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.  

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.  

Example 1:  

    Input: 
    asteroids = [5, 10, -5]
    Output: [5, 10]
    Explanation: 
    The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:  

    Input: 
    asteroids = [8, -8]
    Output: []
    Explanation: 
    The 8 and -8 collide exploding each other.

Example 3:  

    Input: 
    asteroids = [10, 2, -5]
    Output: [10]
    Explanation: 
    The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:  

    Input: 
    asteroids = [-2, -1, 1, 2]
    Output: [-2, -1, 1, 2]
    Explanation: 
    The -2 and -1 are moving left, while the 1 and 2 are moving right.
    Asteroids moving the same direction never meet, so no asteroids will meet each other.

Note:  

-   The length of asteroids will be at most 10000.
-   Each asteroid will be a non-zero integer in the range [-1000, 1000]..

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/asteroid-collision)  

Credits To: [leetcode.com](https://leetcode.com/problems/asteroid-collision/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/asteroid-collision
    ## Basic Ideas: stack
    ##       Scan from left to right. 
    ##       If the element is positive, push
    ##       If the element is negative, check with the stack top
    ##              If collision is detected, make the decision
    ##                 If top element is smaller size, keep the loop
    ##
    ##   Sample data: [-1, 1]. It won't collide
    ##                [1, -1]. Both will explode
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def asteroidCollision(self, asteroids):
            """
            :type asteroids: List[int]
            :rtype: List[int]
            """
            stack = []
            for num in asteroids:
                element = num
                if element > 0:
                    stack.append(element)
                else:
                    # left direction
                    while len(stack) != 0 and stack[-1] > 0:
                        top_element = stack[-1]
                        # eliminate current node
                        if top_element > -element:
                            element = None
                            break
                        elif top_element == -element:
                            # eliminiate both
                            stack.pop()
                            element = None
                            break
                        else:
                            # eliminate stack top. Then recursive check
                            stack.pop()
                    if element:
                        stack.append(element)
            return stack
    
    s = Solution()
    print s.asteroidCollision([8, -8]) # []
    print s.asteroidCollision([-2,-1,1,2]) # [-2,-1,1,2]