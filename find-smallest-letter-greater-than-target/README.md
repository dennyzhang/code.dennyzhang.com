# Leetcode: Find Smallest Letter Greater Than Target     :BLOG:Basic:


---

Find Smallest Letter Greater Than Target  

---

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.  

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.  

Examples:  

    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"

    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"

Note:  

1.  letters has a length in range [2, 10000].
2.  letters consists of lowercase letters, and contains at least 2 unique letters.
3.  target is a lowercase letter.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-smallest-letter-greater-than-target)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/find-smallest-letter-greater-than-target
    ## Basic Ideas: Binary search
    ##  Assumption: duplicate characters
    ##              ["a", "a", "b"], "c"
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution(object):
        def nextGreatestLetter(self, letters, target):
            """
            :type letters: List[str]
            :type target: str
            :rtype: str
            """
            length = len(letters)
            left, right = 0, length - 1
            while left <= right:
                mid = left + (right-left)/2
                if letters[mid] == target:
                    break
                elif letters[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
    
            if left <= right:
                # It has target inside, now find the last element equals the target
                left, right = 0, length - 1
                while left < right:
                    mid = left + (right-left)/2
                    if letters[mid] > target:
                        right = mid - 1
                    else:
                        left = mid
                    if right - left == 1:
                        if letters[right] == target:
                            left = right
                            break
                        else:
                            break
                index = (left + 1) % length
                return letters[index]
            else:
                # It doesn't have the target
                # ['a', 'a', 'a', 'a', 'c', 'c'], 'b'
                index = (right + 1) % length
                return letters[index]
    
    s = Solution()
    print s.nextGreatestLetter(["c","f","j"], "j")