
# Leetcode: Car Fleet     :BLOG:Medium:

---

Car Fleet  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

N cars are going to the same destination along a one lane road.  The destination is target miles away.  

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.  

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.  

The distance between these two cars is ignored - they are assumed to have the same position.  

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.  

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.  

How many car fleets will arrive at the destination?  

Example 1:  

    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3
    Explanation:
    The cars starting at 10 and 8 become a fleet, meeting each other at 12.
    The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
    The cars starting at 5 and 3 become a fleet, meeting each other at 6.
    Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:  

1.  0 <= N <= 10 ^ 4
2.  0 < target <= 10 ^ 6
3.  0 < speed[i] <= 10 ^ 6
4.  0 <= position[i] < target
5.  All initial positions are different.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/car-fleet)  

Credits To: [leetcode.com](https://leetcode.com/problems/car-fleet/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: array

    // Blog link: https://code.dennyzhang.com/car-fleet
    // Basic Ideas:
    //
    // Complexity Time O(n*log(n)), Space O(n)
    import "sort"
    func carFleet(target int, position []int, speed []int) int {
        if len(position) == 0 { return 0 }
        m := map[int]float32{}
        for i, p := range position {
    	m[p] = float32(target-p)/float32(speed[i])
        }
        sort.Ints(position)
        time := make([]float32, len(position))
        for i, p := range position {
    	time[len(position)-1-i] = m[p]
        }
        res := 1
        max := time[0]
        for i:=1; i<len(time); i++ {
    	if time[i]>max {
    	    res ++
    	    max = time[i]
    	}
        }
        return res
    }

