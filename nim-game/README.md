# Puzzle: Nim Game     :BLOG:Game:


---

Do you want to play first or after, if you are determined to win.  

---

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.  

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.  

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.  

Credits To: [Leetcode.com](https://leetcode.com/problems/nim-game/description/)  

    class Solution(object):
        def canWinNim(self, n):
            """
            :type n: int
            :rtype: bool
            """
            ## Idea: recursive
            ## Complexity:
            ##  1,2,3 -> true
            ##  4 -> false
            ##  5 -> true
            ##  6 -> true
            ##  7 -> true
            ##  8 -> false
            ##  9 -> true
            ##  10 -> true
            ##  11 -> true
            ##  12 -> false
            return n%4 != 0

Leave me comments, if you know how to solve.  

More Reading:  
-   [Kids Puzzles](http://brain.dennyzhang.com/tag/kids/)