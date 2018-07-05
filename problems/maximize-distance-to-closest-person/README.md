# Leetcode: Maximize Distance to Closest Person     :BLOG:Basic:


---

Maximize Distance to Closest Person  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/arrary)

---

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.  

There is at least one empty seat, and at least one person sitting.  

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.  

Return that maximum distance to closest person.  

Example 1:  

    Input: [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
    If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

Example 2:  

    Input: [1,0,0,0]
    Output: 3
    Explanation: 
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

Note:  

1.  1 <= seats.length <= 20000
2.  seats contains only 0s or 1s, at least one 0, and at least one 1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximize-distance-to-closest-person)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximize-distance-to-closest-person/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/maximize-distance-to-closest-person
    // Basic Ideas: One pass
    // Find the longest group of consective 0s.
    // Note: for the leading consective 0s and tailing consective 0s, they are different
    // Complexity: Time O(n), Space O(1)
    func maxDistToClosest(seats []int) int {
        res := 0
        i, count, candidate := 0, 0, 0
        for i<len(seats) {
            if seats[i] == 1 {
                i++
                continue
            }
            count = 0
            for i<len(seats) && seats[i] == 0 {
                i, count = i+1, count+1
            }
            // first group or last group
            if i-count == 0 || i==len(seats) {
                candidate = count
            } else {
                candidate = (count+1)/2
            }
            if candidate>res { res = candidate }
        }
        return res
    }