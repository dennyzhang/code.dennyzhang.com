
# Leetcode: Elimination Game     :BLOG:Medium:

---

Elimination Game  

---

Similar Problems:  

-   Tag: [#inspiring](https://code.dennyzhang.com/category/inspiring), [#math](https://code.dennyzhang.com/category/math)

---

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.  

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.  

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.  

Find the last number that remains starting with a list of length n.  

Example:  

    Input:
    n = 9,
    1 2 3 4 5 6 7 8 9
    2 4 6 8
    2 6
    6
    
    Output:
    6

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/elimination-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/elimination-game/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/elimination-game
    // Basic Ideas:
    //  We get the result, when we have ony one left
    //  Each round we will elimate half of the items
    //  Distance between each item will double after each round
    //  Whether we delete or keep the first item, it depends on the remaining count
    // Complexity: Time O(log(n)), Space O(1)
    func lastRemaining(n int) int {
    	head, dist := 1, 1
    	forward := true
    	for n>1 {
    	if forward || n%2 == 1 {
    		head += dist
    	}
    	dist, n = 2*dist, n/2
    	forward = !forward
    	}
    	return head
    }

