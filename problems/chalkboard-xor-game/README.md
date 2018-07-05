
# Leetcode: Chalkboard XOR Game     :BLOG:Hard:

---

Chalkboard XOR Game  

---

Similar Problems:  

-   [Swap Adjacent in LR String](https://code.dennyzhang.com/swap-adjacent-in-lr-string)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [#bitmanipulation](https://code.dennyzhang.com/tag/bitmanipulation), [#game](https://code.dennyzhang.com/tag/game), [#math](https://code.dennyzhang.com/tag/math)

---

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)  

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.  

Return True if and only if Alice wins the game, assuming both players play optimally.  

Example:  

    Input: nums = [1, 1, 2]
    Output: false
    Explanation: 
    Alice has two choices: erase 1 or erase 2. 
    If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
    If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:  

-   1 <= N <= 1000.
-   0 <= nums[i] <= 2^16.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/chalkboard-xor-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/chalkboard-xor-game/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/chalkboard-xor-game
    ## Basic Ideas:
    ##
    ##  One Item:
    ##    [0] -> win
    ##    [x] -> lose
    ##
    ##  Two Items:
    ##    [x, x] -> win
    ##    [x, y] -> win
    ##
    ##  Three Items:
    ##    [x, y, z] -> if xor is 0, win
    ##      [1, 2, 3], [0, 0, 0]
    ##    Otherwise: lose
    ##
    ##  Four Items:
    ##    [x, y, z, m]
    ##       The only way to lose is xor of all remainings is 0
    ##       This indicates x==y==z==m. Then we will win immediately
    ##       [1, 2, 3, 4]
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def xorGame(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: bool
    	"""
    	xor = 0
    	for num in nums: xor ^= num
    	return xor == 0 or len(nums)%2 == 0

