
# Leetcode: Queue Reconstruction by Height     :BLOG:Medium:

---

Queue Reconstruction by Height  

---

Similar Problems:  

-   Tag: [#greedy](https://code.dennyzhang.com/tag/greedy), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.  

Note: The number of people is less than 1,100.  

Example  

    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    
    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/queue-reconstruction-by-height)  

Credits To: [leetcode.com](https://leetcode.com/problems/queue-reconstruction-by-height/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/queue-reconstruction-by-height
    // Basic Ideas:
    //     Intuitive Idea: Find the mininum h, whose k is 0
    //        Once we have identified one, 
    //          we deduct k of other other items whose h is no smaller than current one
    //
    //     Better Idea: sort and insert
    //
    // [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    //
    // sorted:
    // [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
    //
    // switch:
    // [[7,0], [6,1], [7,1], [5,0], [5,2], [4,4]]
    // [[5,0], [7,0], [6,1], [7,1], [5,2], [4,4]]
    // [[5,0], [7,0], [5,2], [6,1], [7,1], [4,4]]
    // [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    //
    // TODO: need a simple way to switch items
    //
    // Complexity: Time O(n*n), Space O(n)
    
    func reconstructQueue(people [][]int) [][]int {
        res := people
        sort.Slice(people, func(i, j int) bool {
    	if people[i][0] > people[j][0] {return true}
    	if people[i][0] == people[j][0] && people[i][1] < people[j][1] {
    	    return true
    	}
    	return false
        })
    
        for i, p := range people {
    	j := p[1]
    	copy(res[j+1:i+1], res[j:i])
    	res[j] = p
        }
        return res
    }

