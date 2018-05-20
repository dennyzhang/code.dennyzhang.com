# Leetcode: Push Dominoes     :BLOG:Medium:


---

Push Dominoes  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs)

---

There are N dominoes in a line, and we place each domino vertically upright.  

![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/domino.png)  

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.  

After each second, each domino that is falling to the left pushes the adjacent domino on the left.  

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.  

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.  

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.  

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.  

Return a string representing the final state.  

Example 1:  

    Input: ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."

Example 2:  

    Input: "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.

Note:  

-   0 <= N <= 10^5
-   String dominoes contains only 'L', 'R' and '.'

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/push-dominoes)  

Credits To: [leetcode.com](https://leetcode.com/problems/push-dominoes/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/push-dominoes
    // Basic Ideas: BFS
    // Complexity: Time O(n), Space O(n)
    func pushDominoes(dominoes string) string {
        n := len(dominoes)
        res := make([]string, n)
        queue := []int{}
        for i, ch := range dominoes {
            if ch == 'L' || ch == 'R' {
                queue = append(queue, i)
                res[i] = string(ch)
            } else {
                res[i] = "."
            }
        }
        for len(queue)!=0 {
            m := make(map[int]int)
            for _, index := range queue {
                ch := res[index]
                if ch == "L" {
                    if index-1>=0 && res[index-1]=="." {
                        m[index-1] -= 1
                    }
                }
                if ch == "R" {
                    if index+1<n && res[index+1]=="." {
                        m[index+1] += 1
                    }
                }
            }
            queue = []int{}
            for index, value := range m {
                if value != 0 {
                    queue = append(queue, index)
                    if value < 0 {
                        res[index] = "L"
                    } else {
                        res[index] = "R"
                    }
                }
            }
        }
        return strings.Join(res, "")
    }