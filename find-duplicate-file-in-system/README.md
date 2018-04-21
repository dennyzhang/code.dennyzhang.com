# Leetcode: Find Duplicate File in System     :BLOG:Basic:


---

Find Duplicate File in System  

---

Similar Problems:  
-   [Group Anagrams](https://code.dennyzhang.com/group-anagrams)
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.  

A group of duplicate files consists of at least two files that have exactly the same content.  

A single directory info string in the input list has the following format:  

"root/d1/d2/&#x2026;/dm f1.txt(f1\_content) f2.txt(f2\_content) &#x2026; fn.txt(fn\_content)"  

It means there are n files (f1.txt, f2.txt &#x2026; fn.txt with content f1\_content, f2\_content &#x2026; fn\_content, respectively) in directory root/d1/d2/&#x2026;/dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.  

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:  

"directory\_path/file\_name.txt"  

Example 1:  

    Input:
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    Output:  
    [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Note:  
1.  No order is required for the final output.
2.  You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
3.  The number of files given is in the range of [1,20000].
4.  You may assume no files or directories share the same name in the same directory.
5.  You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.

Follow-up beyond contest:  
1.  Imagine you are given a real file system, how will you search files? DFS or BFS?
2.  If the file content is very large (GB level), how will you modify your solution?
3.  If you can only read the file by 1kb each time, how will you modify your solution?
4.  What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
5.  How to make sure the duplicated files you find are not false positive?

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-duplicate-file-in-system)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-duplicate-file-in-system/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/find-duplicate-file-in-system
    // Basic Ideas: hashmap
    // Complexity:
    import (
            "strings"
    )
    
    func findDuplicate(paths []string) [][]string {
        m := make(map[string][]string)
        res := [][]string{}
        for _, path := range paths {
            l := strings.Split(path, " ")
            dir_name := l[0]
            for _, f := range l[1:] {
                i := strings.Index(f, "(")
                fname := f[0:i]
                content := f[i+1:len(f)-1]                    
                m[content] = append(m[content], strings.Join([]string{dir_name, fname}, "/"))
            }
        }
    
        for key := range m {
            if len(m[key]) != 1 {
                res = append(res, m[key])
            }
        }
        return res
    }