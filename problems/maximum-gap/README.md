# Leetcode: Maximum Gap     :BLOG:Hard:


---

Maximum Gap  

---

Similar Problems:  
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic)m, [#bucketsort](https://code.dennyzhang.com/tag/bucketsort)

---

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.  

Try to solve it in linear time/space.  

Return 0 if the array contains less than 2 elements.  

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/maximum-gap)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-gap/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: bucket sort

**General Thinkings:**  

    Put each element into a list of buckets. Each bucket track the min and max.
    
    The scan the bucket kist, we get the maximum gap.
    
    Some improvements:
    To get the mininum bucket count, we avoid placing min and max into any buckets.
    
    Bucket count: n-1, bucket size: int((max-min)/(n-1))

**Walk Through Testdata**  
![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/bucket_sort.png)  

**Key Observations:**  

    - Duplicate elements doesn't matter
    - Instead of total order, we maintain partial order in bucket-sort. 
      Actually we don't even sort. We can compare items with pilots

    // Blog link: https://code.dennyzhang.com/maximum-gap