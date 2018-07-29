
# LintCode: Function Runtime     :BLOG:Basic:

---

Function Runtime  

---

Similar Problems:  

-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Description  
Given a series of descriptions of when the function enters and exits, ask how long each function will run.  

The function string length does not exceed 1010, the description number does not exceed 1000010000, and the time does not exceed 1e91e9  
All descriptions are in chronological order and the input is guaranteed to be correct. Each function first enters and then exits  
Ascending output according to function name dictionary order  

Example  

    Give s=["F1 Enter 10","F2 Enter 18","F2 Exit 19","F1 Exit 20"],return["F1|10","F2|1"].
    
    Explanation:
    F1 enters from time 10, exits at time 20, and the running time is 10,
    F2 enters from time 18, exits at time 19, and the running time is 1.
    Give s=["F1 Enter 10","F1 Exit 18","F1 Enter 19","F1 Exit 20"],return["F1|9"].

    Explanation:
    F1 enters from time 10, exits at time 18 and enters from time 19, 
    exits at time 20, and the total running time is 9.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/function-runtime)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/function-runtime/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/function-runtime
    // Basic Ideas: two hashmap
    // Complexity: Time O(n*log(n)), Space O(n)
    /**
     * @param a: The Descriptions
     * @return: Every functions' runtime
     */
    import (
        "fmt"
        "strconv"
        "strings"
        "sort"
        )
    func getRuntime (a []string) []string {
        m1, m2 := map[string]int{}, map[string]int{}
        for _, s := range a {
    	l := strings.Split(s, " ")
    	f, e:= l[0], l[1]
    	v, _ := strconv.Atoi(l[2])
    	if e == "Enter" {
    	    m1[f] = v
    	} else {
    	    m2[f] += v - m1[f]
    	}
        }
    
        res, keys := []string{}, []string{}
        for f := range m2 { keys = append(keys, f) }
        sort.Strings(keys)
        for _, f := range keys {
    	res = append(res, fmt.Sprintf("%s|%d", f, m2[f]))
        }
        return res
    }

