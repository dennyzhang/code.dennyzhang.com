# Leetcode: Flip Game     :BLOG:Basic:


---

Flip Game  

---

Similar Problems:  
-   [Flip Game II](https://brain.dennyzhang.com/flip-game-ii)
-   [Tag: #string](https://brain.dennyzhang.com/tag/string)
-   [Tag: #game](https://brain.dennyzhang.com/tag/game)

---

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "&#x2013;". The game ends when a person can no longer make a move and therefore the other person will be the winner.  

Write a function to compute all possible states of the string after one valid move.  

For example, given s = "<del>++</del>", after one move, it may become one of the following states:  

    [
      "--++",
      "+--+",
      "++--"
    ]

If there is no valid move, return an empty list [].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/flip-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/flip-game/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/flip-game
    ## Basic Ideas: One pass
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def generatePossibleNextMoves(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            res = []
            for i in range(1, len(s)):
                if s[i-1:i+1] == '++':
                    res.append(s[:i-1] + '--' + s[i+1:])
            return res