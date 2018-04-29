# Leetcode: Friends Of Appropriate Ages     :BLOG:Medium:


---

Friends Of Appropriate Ages  

---

Similar Problems:  
-   [LintCode: Friend Request](https://code.dennyzhang.com/friend-request)
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.  

Person A will NOT friend request person B (B != A) if any of the following conditions are true:  

-   age[B] <= 0.5 \* age[A] + 7
-   age[B] > age[A]
-   age[B] > 100 && age[A] < 100
-   Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.  

How many total friend requests are made?  

Example 1:  

    Input: [16,16]
    Output: 2
    Explanation: 2 people friend request each other.

Example 2:  

    Input: [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:  

    Input: [20,30,100,110,120]
    Output: 
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:  

-   1 <= ages.length <= 20000.
-   1 <= ages[i] <= 120.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/friends-of-appropriate-ages)  

Credits To: [leetcode.com](https://leetcode.com/problems/friends-of-appropriate-ages/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/friends-of-appropriate-ages
    // Basic Ideas: hashmap
    //    We can ignore Rule 3, since rule 2 will cover it.
    //
    // Complexity: Time O(n), Space O(1)
    func numFriendRequests(ages []int) int {
        m := make(map[int]int)
        for age:=1; age<=120; age++ { m[age] = 0 }
        for _, age := range ages { m[age] += 1 }
    
        res := 0
        for age:=1; age<=120; age++ {
            count, _ := m[age]
            if count == 0 { continue }
    
            // friends with the same age
            if float32(age)>0.5*float32(age)+7 { res += count*(count-1) }
    
            // friends with different ages
            for age2:=1; age2<age; age2++ {
                count2, _ := m[age2]
                if count2 == 0 { continue }
                if 0.5*float32(age)+7>= float32(age2) { continue }
                res += count*count2
            }
        }
        return res
    }