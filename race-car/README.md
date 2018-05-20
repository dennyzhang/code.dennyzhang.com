# Leetcode: Race Car     :BLOG:Hard:


---

Race Car  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)  

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).  

When you get an instruction "A", your car does the following: position += speed, speed \*= 2.  

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)  

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.  

Now for some target position, say the length of the shortest sequence of instructions to get there.  

Example 1:  

    Input: 
    target = 3
    Output: 2
    Explanation: 
    The shortest instruction sequence is "AA".
    Your position goes from 0->1->3.

Example 2:  

    Input: 
    target = 6
    Output: 5
    Explanation: 
    The shortest instruction sequence is "AAARA".
    Your position goes from 0->1->3->7->7->6.

Note:  

-   1 <= target <= 10000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/race-car)  

Credits To: [leetcode.com](https://leetcode.com/problems/race-car/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/race-car
    // Basic Ideas: BFS + Memorized
    //   When speed is 1 or -1, put (location, speed) into visisted set
    //
    // Notice:
    //   When we have passed the target and the speed is positive, we turn back
    //   When we on the left side of target and speed is negative, we turn back
    //   Above 2 assumptions don't hold
    //
    // Complexity:
    type Node struct {
        loc, speed int
    }
    func racecar(target int) int {
        if target == 0 { return 0 }
        visisted := map[string]bool{}
        queue := []Node{}
        queue = append(queue, Node{0, 1})
        visisted[fmt.Sprintf("%d:%d", 0, 1)] = true
        level := 0
        for len(queue) != 0 {
            level++
            items := []Node{}
            for _, node := range queue {
                loc2 := node.loc+node.speed
                if loc2 == target { return level }
                // speed up
                speed2 := node.speed*2
                items = append(items, Node{loc2, speed2})
                // change direction
                if node.speed < 0 {
                    speed2 = 1
                } else {
                    speed2 = -1
                }
                if visisted[fmt.Sprintf("%d:%d", node.loc, speed2)] == false {
                    visisted[fmt.Sprintf("%d:%d", node.loc, speed2)] = true
                    items = append(items, Node{node.loc, speed2})
                }
            }
            // copy back
            queue = []Node{}
            for _, node := range items{
                queue = append(queue, node)
            }
        }
        return -1
    }