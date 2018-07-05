
# Leetcode: 24 Game     :BLOG:Hard:

---

24 Game  

---

Similar Problems:  

-   Tag: [#recursive](https://code.dennyzhang.com/tag/recursive), [#game](https://code.dennyzhang.com/tag/game)

---

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through \*, /, +, -, (, ) to get the value of 24.  

Example 1:  

    Input: [4, 1, 8, 7]
    Output: True
    Explanation: (8-4) * (7-1) = 24

Example 2:  

    Input: [1, 2, 1, 2]
    Output: False

Note:  

1.  The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
2.  Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
3.  You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/24-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/24-game/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

**General Thinkings:**  

    

**Key Observations:**  

    

**Walk Through Testdata**  

    

    // Blog link: https://code.dennyzhang.com/24-game
    // Basic Ideas:
    // From a list of numbers, choose any two.
    // [1,3,4,6]: 6/(1-3/4)
    // [3,3,8,8]: 8/(3-8/3)
    // Then get all the possiblities and put back the result to to the list.
    // Complexity:
    func caculateList(nums []float32) bool {
        //fmt.Println(nums)
        if len(nums) == 0 { return false }
        if len(nums) == 1 {
    	diff := nums[0] - 24
    	if diff<0 { diff = -diff }
    	if diff<0.0001 { return true }
    	return false
        }
        for i:= 0; i<len(nums); i++ {
    	for j:=0; j<len(nums); j++ {
    	    if j==i { continue }
    	    items := []float32{}
    	    for k:=0; k<len(nums); k++ {
    		if (k!=i && k!=j) {
    		    items = append(items, nums[k])
    		}
    	    }
    	    // fmt.Println(nums, items)
    	    if caculateList(append(items, nums[i]+nums[j])) {
    		return true
    	    }
    	    if caculateList(append(items, nums[i]-nums[j])) {
    		return true
    	    }
    	    if caculateList(append(items, nums[i]*nums[j])) {
    		return true
    	    }
    	    if nums[j] != 0 {
    		if caculateList(append(items, nums[i]/nums[j])) {
    		    return true
    		}
    	    }
    	    //fmt.Println(nums, items)
    	}
        }
        return false
    }
    
    func judgePoint24(nums []int) bool {
        l := []float32{}
        for _, num := range nums {
    	l = append(l, float32(num))
        }
        return caculateList(l)
    }

