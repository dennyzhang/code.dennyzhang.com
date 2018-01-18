# Leetcode: Judge Route Circle     :BLOG:Basic:


---

Judge Route Circle  

---

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.  

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.  

    Example 1:
    Input: "UD"
    Output: true

    Example 2:
    Input: "LL"
    Output: false

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/judge-route-circle)  

Credits To: [Leetcode.com](https://leetcode.com/problems/judge-route-circle/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def judgeCircle(self, moves):
            """
            :type moves: str
            :rtype: bool
            """
            x = 0
            y = 0
            for move in moves:
                if move not in 'UDLR':
                    raise Exception("Wrong move: %s" % (move))
    
                if move == 'U':
                    y += 1
                if move == 'D':
                    y -= 1
                if move == 'L':
                    x -= 1
                if move == 'R':
                    x += 1
            return (x == 0) and (y==0)
    
    if __name__ == '__main__':
        s = Solution()
        print s.judgeCircle("UD")
        print s.judgeCircle("LL")