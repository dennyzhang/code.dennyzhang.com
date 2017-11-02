People will ask silly algorithm questions.

So let's get it down.

One useful test website: https://leetcode.com

More website:
- https://en.wikipedia.org/wiki/Online_judge
- https://www.interviewbit.com
- http://www.geeksforgeeks.org
- https://careercup.com

# Blog Sites:
- http://bangbingsyb.blogspot.com

# Summary

## Tree
- **6 Traverse of Binary Tree**: first, middle, right; non-recursive first, middle, right
- DFS, BFS
- Sum of left leaves: https://leetcode.com/problems/sum-of-left-leaves/description/
- Get min and max depth of binary tree

## Why people would want to use your GitHub repo?
- TODO: think about it!

## Search & Sort

## Bit operation
- Number Complement: https://leetcode.com/problems/number-complement/description/
- X xor X = 0, X xor 0 = X
- Whether power of 2
- Number of 1 Bits( Hamming weight): https://leetcode.com/problems/number-of-1-bits/description/
- n % 2: (n & 1 == 1)
- How to check integer overflow?
- Mask bits: https://leetcode.com/problems/power-of-four/description/
- Binary Number with Alternating Bits: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
- Run demical sum by digits: https://leetcode.com/problems/add-strings/description/

## String
- Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/description/

## Good for DevOps in leetcode.com
- TODO: Important things

## Leetcode learns learned sharing from blogs
- http://blog.csdn.net/linhuanmars
- https://siddontang.gitbooks.io/leetcode-solution/content/

## Array
- sliding window solution: int index: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
- rotate array: https://leetcode.com/problems/rotate-array/description/
- Move zeros: https://leetcode.com/problems/move-zeroes/description/
- link in-place change: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

## Linked List
**How many pointers you use? For what purpose?**
- Remove Duplicates from Sorted List: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
- Remove Remove Duplicates from Sorted List II: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
- Reverse elements from i to j: https://leetcode.com/problems/reverse-linked-list-ii/description/

## Integer
- swap two values
- 2sum, 3sum, 4sum, ksum
- power of 3: https://leetcode.com/problems/power-of-three/description/

## Greedy
- TODO

## DP
- Climbing Stairs: https://leetcode.com/problems/climbing-stairs/description/

## Basic Elements:
- Description
- Basic Idea
- Complexity
- Tags: #amusing, #redo

## Procedure
1. Read and explain the question to the interviewr: Show you understand the questions
2. Interviewer may ask: tell me what you are thinking
3. Show your programming skills: how fluent you are with the language and lib
4. Watch out Complexity trade-off, and you may need to explain them
5. You can run unit test

## Command
- Find amusing tickets
find . -name *.py | xargs grep -C 3 amusing | grep -v Author | grep -v Description | grep -v "\-\-" | grep -v "File:" | grep -v "^$" | grep https

## Lesson learned from Cracking leetcode.com
- Learn to write bug-free code. Test-driven may lead you to waste time? If you think clearly and pass with once
- Understand data structure and common library in your languages: Python TreeNode, Python Interval
- Write your idea, before you coding. Update time/space complexity in advance.
- Know how to use library. Thus we can think and design in a higher layer. But make sure you can evaluate the time and space performance
- Think in a natural way, instead of a complicated way
- Time complexity of n is similar to 2n, but it's 100% faster in our real production!
- Don't write in your IDE. emacs/vi
- **Choose the proper variable names: easy to understand**
- **Explain the usage of your key data structure**
- **Read other people's code, then learn something**
