# Leetcode: Distribute Candies     :BLOG:Basic:


---

Distribute Candies  

---

Similar Problems:  
-   [Review: Game Problems](https://code.dennyzhang.com/review-game), [Tag: #game](https://code.dennyzhang.com/tag/game)

---

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.  

    Example 1:
    Input: candies = [1,1,2,2,3,3]
    Output: 3
    Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies.

    Example 2:
    Input: candies = [1,1,2,3]
    Output: 2
    Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
    The sister has two different kinds of candies, the brother has only one kind of candies.

Note:  

1.  The length of the given array is in range [2, 10,000], and will be even.
2.  The number in given array is in range [-100,000, 100,000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/distribute-candies)  

Credits To: [leetcode.com](https://leetcode.com/problems/distribute-candies/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/distribute-candies
    ## Basic Ideas: Count how many different type of candies
    ##              If it has more then n/2 types, return n/2.
    ##              Otherwise return the count of candies' types
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def distributeCandies(self, candies):
            """
            :type candies: List[int]
            :rtype: int
            """
            return min(len(candies)/2, len(set(candies)))