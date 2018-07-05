# Leetcode: Split Array into Fibonacci Sequence     :BLOG:Medium:


---

Split Array into Fibonacci Sequence  

---

Similar Problems:  
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#string](https://code.dennyzhang.com/tag/string)

---

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].  

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:  

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);  
F.length >= 3;  
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.  
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.  

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.  

Example 1:  

    Input: "123456579"
    Output: [123,456,579]

Example 2:  

    Input: "11235813"
    Output: [1,1,2,3,5,8,13]

Example 3:  

    Input: "112358130"
    Output: []
    Explanation: The task is impossible.

Example 4:  

    Input: "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:  

    Input: "1101111"
    Output: [110, 1, 111]
    Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:  

1.  1 <= S.length <= 200
2.  S contains only digits.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/split-array-into-fibonacci-sequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: Brute Force

**General Thinkings:**  

    The first two elements of the array uniquely determine the rest of the sequence.

    // Blog link: https://code.dennyzhang.com/split-array-into-fibonacci-sequence
    // Basic Ideas: Brute Force
    // num1: S[0:i], num2: S[i:j]
    // Complexity: Time ?, Space O(n)
    import "strconv"
    func splitString(S string, num1 int, num2 int) []int {
        if num1>(1<<31 - 1) || num2>(1<<31 - 1) { return []int{} }
        res := []int{num1, num2}
        for len(S) != 0 {
            num3 := num1+num2
            if num3>(1<<31 - 1) { return []int{} }
            str := strconv.Itoa(num3)
            if strings.Index(S, str) != 0 { return []int{} }
            S = S[len(str):]
            num1, num2 = num2, num3
            res = append(res, num3)
        }
        return res
    }
    
    func splitIntoFibonacci(S string) []int {
        // num1: S[0:i], num2: S[i:j]
        for i:=1; i<len(S)-2; i++ {
            for j:=i+1; j<len(S)-1; j++ {
                if S[0] == '0' && S[0:i] != "0" { continue }
                if S[i] == '0' && S[i:j] != "0" { continue }
                num1, _ := strconv.Atoi(S[0:i])
                num2, _ := strconv.Atoi(S[i:j])
                l := splitString(S[j:], num1, num2)
                if len(l) >=3 { return l }
            }
        }
        return []int{}
    }