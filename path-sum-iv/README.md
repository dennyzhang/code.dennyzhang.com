# Leetcode: Path Sum IV     :BLOG:Medium:


---

Path Sum IV  

---

Similar Problems:  

-   [Path Sum III](https://code.dennyzhang.com/path-sum-iii)
-   Tag: [#recursive](https://code.dennyzhang.com/tag/recursive), [#pathsum](https://code.dennyzhang.com/tag/pathsum), [#binarytree](https://code.dennyzhang.com/tag/binarytree)

---

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.  

For each integer in this list:  

1.  The hundreds digit represents the depth D of this node, 1 <= D <= 4.
2.  The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
3.  The units digit represents the value V of this node, 0 <= V <= 9.

Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.  

Example 1:  

    Input: [113, 215, 221]
    Output: 12
    Explanation: 
    The tree that the list represents is:
        3
       / \
      5   1
    
    The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:  

    Input: [113, 221]
    Output: 4
    Explanation: 
    The tree that the list represents is: 
        3
         \
          1
    
    The path sum is (3 + 1) = 4.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/path-sum-iv)  

Credits To: [leetcode.com](https://leetcode.com/problems/path-sum-iv/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: bfs

    // Blog link: https://code.dennyzhang.com/path-sum-iv
    // Baisc Ideas: BFS
    //
    // map: index -> value
    // From level i+1 to level i, it's simply (index+1)/2
    //
    // Interesting question: when we do bfs, how we know whether one node is a leaf?
    //
    // Complexity: Time O(n), Space O(n)
    func pathSum(nums int) int {
        if len(nums) == 0 { return 0 }
    
        res := 0
        m := map[int]int{1:nums[0]%10}
        i, level := 1, 1
        index, node := 0, 0
        for len(m) != 0{
            level++
            m2 := map[int]int{}
            for i<len(nums) && nums[i]<(level+1)*100 {
                index = (nums[i]%100)/10
                node = m[(index+1)/2]
                m2[index] = node+nums[i]%10
                i++
            }
            for key := range m {
                _, status1 := m2[key*2-1]
                _, status2 := m2[key*2]
                // collect leaf nodes at the current layer
                if status1 == false && status2 == false {
                    res += m[key]
                }
            }
            m = m2
        }
        return res
    }