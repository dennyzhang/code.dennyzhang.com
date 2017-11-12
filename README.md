Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Basic Intro](#basic-intro)
   * [About Code Interview](#about-code-interview)
      * [General Procedure](#general-procedure)
      * [Lessons learned](#lessons-learned)
   * [Basic](#basic)
      * [Array pointer](#array-pointer)
      * [Integer](#integer)
      * [String](#string)
      * [Array](#array)
      * [Linked List](#linked-list)
      * [Search &amp; Sort](#search--sort)
      * [Binary Search](#binary-search)
   * [Advanced](#advanced)
      * [Tree](#tree)
      * [Combination](#combination)
      * [Bit operation](#bit-operation)
      * [DP](#dp)
      * [Greedy](#greedy)
      * [Contiguous Subarray](#contiguous-subarray)
   * [About this Github Repo](#about-this-github-repo)
      * [Commands](#commands)
      * [Frequently Used Tags](#frequently-used-tags)
      * [Grow Influence](#grow-influence)
      * [Similar Websites](#similar-websites)
   * [License](#license)

# Basic Intro
<a href="https://github.com/DennyZhang?tab=followers"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/fork_github.png" /></a>

[![Build Status](https://travis-ci.org/DennyZhang/leetcode_python.svg?branch=master)](https://travis-ci.org/DennyZhang/leetcode_python) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![LinkedIn](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/linkedin.png)](https://www.linkedin.com/in/dennyzhang001) [![Slack](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/slack.png)](https://www.dennyzhang.com/slack) [![Github](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/github.png)](https://github.com/DennyZhang)

File me [tickets](https://github.com/DennyZhang/leetcode_python/issues) or star [the repo](https://github.com/DennyZhang/leetcode_python).

Solve all [leetcode.com](https://leetcode.com) problems in Python

http://brain.dennyzhang.com/contact

People will ask silly algorithm questions.

# About Code Interview
## General Procedure
1. Read and explain the question to the interviewr: Show you understand the questions
2. Interviewer may ask: tell me what you are thinking
3. Show your programming skills: how fluent you are with the language and lib
4. Watch out Complexity trade-off, and you may need to explain them
5. You can run unit test

## Lessons Learned
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

# Basic
## Array
- sliding window solution: int index: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
- rotate array: https://leetcode.com/problems/rotate-array/description/
- Move zeros: https://leetcode.com/problems/move-zeroes/description/
- link in-place change: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
- String Compression: https://leetcode.com/problems/string-compression/description/

## Integer
- swap two values
- 2sum, 3sum, 4sum, ksum
- power of 3: https://leetcode.com/problems/power-of-three/description/

## String
- Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/description/

## Linked List
**How many pointers you use? For what purpose?**
- Remove Duplicates from Sorted List:

```
I: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
II: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
```

- Reverse elements from i to j: https://leetcode.com/problems/reverse-linked-list-ii/description/

## Search & Sort

## Binary Search
- binary search: log(n)

# Advanced
## Tree

- **6 Traverse of Binary Tree**: first, middle, right; non-recursive first, middle, right

```
https://leetcode.com/problems/binary-tree-preorder-traversal/description/
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
```
- DFS, BFS
- **BFS: Generate Parentheses**: https://leetcode.com/problems/generate-parentheses/description/
- System Tree: https://leetcode.com/problems/symmetric-tree/description/
- Path Sum
```
II: https://leetcode.com/problems/path-sum-ii/description/
II: https://leetcode.com/problems/path-sum-ii/description/
III: https://leetcode.com/problems/path-sum-iii/description/
```

- Define how many layers
- what value to get and concat
- Sum of left leaves: https://leetcode.com/problems/sum-of-left-leaves/description/
- Get min and max depth of binary tree

## Combination
- Permutations:

```
I: https://leetcode.com/problems/permutations/description/
II: https://leetcode.com/problems/permutations-ii/description/
```

## Bit Operation
- Number Complement: https://leetcode.com/problems/number-complement/description/
- X xor X = 0, X xor 0 = X
- Whether power of 2
- Number of 1 Bits( Hamming weight): https://leetcode.com/problems/number-of-1-bits/description/
- n % 2: (n & 1 == 1)
- How to check integer overflow?
- Mask bits: https://leetcode.com/problems/power-of-four/description/
- Binary Number with Alternating Bits: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
- Run demical sum by digits: https://leetcode.com/problems/add-strings/description/

## DP
- Climbing Stairs: https://leetcode.com/problems/climbing-stairs/description/
- House Robber: https://leetcode.com/problems/house-robber/description/

## Greedy
- TODO

## Contiguous Subarray
- Maximum Product Subarray: https://leetcode.com/problems/maximum-product-subarray/description/

# About this Github Repo
## Commands
- Find amusing tickets

```
find . -name *.py | xargs grep -C 3 amusing | grep -v Author \
     | grep -v Description | grep -v "\-\-" | grep -v "File:" | grep -v "^$" | grep https
```

## Frequently Used Tags

- #amusing, #redo
- #brain
- #todobrain

## Grow Influence
- Why people would want to use your GitHub repo?
  TODO: think about it!

## Similar Websites
- http://brain.dennyzhang.com
- http://bangbingsyb.blogspot.com
- https://en.wikipedia.org/wiki/Online_judge
- https://www.interviewbit.com
- http://www.geeksforgeeks.org
- https://careercup.com
- http://blog.csdn.net/linhuanmars
- https://siddontang.gitbooks.io/leetcode-solution/content/

# License
- Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).

<img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/magic.gif">
