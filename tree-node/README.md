# Leetcode: Tree Node     :BLOG:Medium:


---

Tree Node  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

Given a table tree, id is identifier of the tree node and p\_id is its parent node's id.  

    +----+------+
    | id | p_id |
    +----+------+
    | 1  | null |
    | 2  | 1    |
    | 3  | 1    |
    | 4  | 2    |
    | 5  | 2    |
    +----+------+

Each node in the tree can be one of three types:  
-   Leaf: if the node is a leaf node.
-   Root: if the node is the root of the tree.
-   Inner: If the node is neither a leaf node nor a root node.

Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:  

    +----+------+
    | id | Type |
    +----+------+
    | 1  | Root |
    | 2  | Inner|
    | 3  | Leaf |
    | 4  | Leaf |
    | 5  | Leaf |
    +----+------+

Explanation  

-   Node '1' is root node, because its parent node is NULL and it has child node '2' and '3'.
-   Node '2' is inner node, because it has parent node '1' and child node '4' and '5'.
-   Node '3', '4' and '5' is Leaf node, because they have parent node and they don't have child node.

And here is the image of the sample tree as below:  

            1
          /   \
        2       3
      /   \
    4       5

Note  

If there is only one node on the tree, you only need to output its root attributes.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/tree-node)  

Credits To: [leetcode.com](https://leetcode.com/problems/tree-node/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/tree-node
    ## Basic Idea: Left join
    # In tree, each node can only one parent or no parent
    ## | id | p_id | id (child) |
    ## |----+------+------------|
    ## |  1 | null |          1 |
    ## |  1 | null |          2 |
    ## |  2 |    1 |          4 |
    ## |  2 |    1 |          5 |
    ## |  3 |    1 |       null |
    ## |  4 |    2 |       null |
    ## |  5 |    2 |       null |
    
    select t1.id, 
        case
            when isnull(t1.p_id) then 'Root'
            when isnull(max(t2.id)) then 'Leaf'
            else 'Inner'
        end as Type
    from tree as t1 left join tree as t2
    on t1.id = t2.p_id
    group by t1.id, t1.p_id