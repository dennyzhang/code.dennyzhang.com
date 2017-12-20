Table of Contents
=================

   * [Basic Intro](#basic-intro)
   * [About Code Interview](#about-code-interview)
      * [General Procedure](#general-procedure)
      * [Lessons Learned](#lessons-learned)
   * [Fundamental Prep](#fundamental-prep)
   * [About this Github Repo](#about-this-github-repo)
      * [Commands](#commands)
      * [Frequently Used Tags](#frequently-used-tags)
      * [Grow Influence](#grow-influence)
      * [Similar Websites](#similar-websites)
   * [License](#license)

# Basic Intro
<a href="https://github.com/DennyZhang?tab=followers"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/fork_github.png" /></a>

[![Build Status](https://travis-ci.org/DennyZhang/challenges-leetcode-interesting.svg?branch=master)](https://travis-ci.org/DennyZhang/challenges-leetcode-interesting) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![LinkedIn](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/linkedin.png)](https://www.linkedin.com/in/dennyzhang001) [![Slack](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/slack.png)](https://www.dennyzhang.com/slack) [![Github](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/github.png)](https://github.com/DennyZhang)

File me [tickets](https://github.com/DennyZhang/challenges-leetcode-interesting/issues) or star [the repo](https://github.com/DennyZhang/challenges-leetcode-interesting).

Solve all [leetcode.com](https://leetcode.com) problems in Python

http://brain.dennyzhang.com/contact

People will ask silly algorithm questions.

<a href="https://www.dennyzhang.com"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/dns.png"></a>

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

# Fundamental Prep
Check: [BASIC.md](BASIC.md)

# About this Github Repo
## Commands
- Find amusing tickets

```
find . -name *.py | xargs grep -C 3 amusing | grep -v Author \
     | grep -v Description | grep -v "\-\-" | grep -v "File:" | grep -v "^$" | grep https
```

<a href="https://www.dennyzhang.com"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/dns.png"></a>

## Frequently Used Tags

- #amusing, #redo
- #brain
- #todobrain

## Grow Influence
- Why people would want to use your GitHub repo?
  TODO: think about it!

<a href="https://www.dennyzhang.com"><img align="right" width="201" height="268" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/denny_201706.png"></a>

## Similar Websites
- http://brain.dennyzhang.com
- http://bangbingsyb.blogspot.com
- https://en.wikipedia.org/wiki/Online_judge
- https://www.interviewbit.com
- http://www.geeksforgeeks.org
- https://careercup.com
- http://blog.csdn.net/linhuanmars
- https://siddontang.gitbooks.io/leetcode-solution/content/
- https://github.com/algorhythms/LeetCode
- https://github.com/jw2013/Leetcode-Py

# License
- Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).

# Basic tests
- Binary search: https://leetcode.com/problems/search-a-2d-matrix/description/

# Basic Data Structure
- Bloom filter
- Hash
- bit-map
- heap
- Inverted index
- trie tree
- segment tree
