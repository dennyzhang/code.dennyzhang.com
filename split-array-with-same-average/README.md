
# Leetcode: Split Array With Same Average     :BLOG:Hard:

---

Split Array With Same Average  

---

Similar Problems:  

-   [Matchsticks to Square](https://code.dennyzhang.com/matchsticks-to-square)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#math](https://code.dennyzhang.com/tag/math), [#classic](https://code.dennyzhang.com/tag/classic)

---

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)  

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.  

    Example :
    Input: 
    [1,2,3,4,5,6,7,8]
    Output: true
    Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.

Note:  

-   The length of A will be in the range [1, 30].
-   A[i] will be in the range of [0, 10000].Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/split-array-with-same-average)  

Credits To: [leetcode.com](https://leetcode.com/problems/split-array-with-same-average/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/split-array-with-same-average
    // Basic Ideas: BFS pruning
    // Observation:
    //  avg(A) == avg(B) == avg(C)
    //  We only need to check combination which has no more than len(A)/2 items.
    //          Apparently max(len(B), len(C)) <= len(A)/2 
    //  Avoid duplicated caculation by using a hashmap
    //  If we sort A, once avg(B) >= avg(A), we can't add any more item which is bigger than avg(A)
    //  
    // Complexity:
    import "sort"
    type Entity struct {
      count, sum int
    }
    
    func splitArraySameAverage(A []int) bool {
        if len(A)<=1 { return false }
    
        sum_a := 0
        for _, v:= range A { sum_a+=v }
        visited := map[Entity]bool{}
    
        sort.Ints(A[:])
        // count, sum
        queue := [][]int{}
        for _, v:= range A {
    	// add current item to queue
    	if v*len(A) == sum_a { return true }
    	entity := Entity{1, v}
    	if visited[entity] == false {
    	    queue = append(queue, []int{1, v})
    	    visited[entity] = true
    	}
    	// whether add current item to existings items in the queue
    	list := [][]int{}
    	for _, item:= range queue {
    	    // whether to explore
    	    if item[0]*2<len(A) {
    		v1, v2:= (item[1]+v)*len(A), (item[0]+1)*sum_a
    		if v1==v2{
    		    return true
    		} else {
    		    if v1<v2 {
    			entity = Entity{item[0]+1, item[1]+v}
    			if visited[entity] == false {
    			    list = append(list, []int{item[0]+1, item[1]+v})
    			    visited[entity] = true
    			}
    		    }
    		}
    	    }
    	}
    	// update queue
    	for _, v:= range list { queue = append(queue, v) }
        }
        return false
    }

