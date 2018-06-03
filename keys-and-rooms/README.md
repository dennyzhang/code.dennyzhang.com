# Leetcode: Keys and Rooms     :BLOG:classic:


---

Keys and Rooms  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#dfs](https://code.dennyzhang.com/tag/dfs), [#classic](https://code.dennyzhang.com/tag/classic)

---

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, &#x2026;, N-1, and each room may have some keys to access the next room.  

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, &#x2026;, N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.  

Initially, all the rooms start locked (except for room 0).  

You can walk back and forth between rooms freely.  

Return true if and only if you can enter every room.  

Example 1:  

    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:  

    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.

Note:  

1.  1 <= rooms.length <= 1000
2.  0 <= rooms[i].length <= 1000
3.  The number of keys in all rooms combined is at most 3000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/keys-and-rooms)  

Credits To: [leetcode.com](https://leetcode.com/problems/keys-and-rooms/description/)  

Leave me comments, if you have better ways to solve.  

---

**General Thinkings:**  
In essence, the question is about whether a graph is connected for all nodes.  

-   Solution: DFS

    // Blog link: https://code.dennyzhang.com/keys-and-rooms
    // Basic Ideas: DFS
    // Complexity: Time O(V), Space O(n)
    func canVisitAllRooms(rooms [][]int) bool {
        visited := make([]bool, len(rooms))
        visited[0] = true
        stack := []int{0}
        for len(stack) != 0 {
            node := stack[len(stack)-1]
            stack = stack[0:len(stack)-1]
            for _, node2 := range rooms[node] {
                if visited[node2] == false {
                    visited[node2] = true
                    stack = append(stack, node2)
                }
            }
        }
        for _, isVisited := range visited {
            if isVisited == false { return false }
        }
        return true
    }

-   Solution: BFS

    // Blog link: https://code.dennyzhang.com/keys-and-rooms
    // Basic Ideas: BFS
    // Tree traversal
    // Complexity: Time O(V), Space O(n)
    //    V = edge count, n = node count
    func canVisitAllRooms(rooms [][]int) bool {
        visited := make([]bool, len(rooms))
        queue := []int{}
        queue = append(queue, 0)
        visited[0] = true
        for len(queue) != 0 {
            items := []int{}
            for _, node := range queue {
                for _, node2 := range rooms[node]{
                    if visited[node2] == false {
                        visited[node2] = true
                        items = append(items, node2)
                    }
                }
            }
            queue = []int{}
            for _, node := range items { 
                queue = append(queue, node)
            }
        }
        for _, isVisited := range visited {
            if isVisited == false { return false }
        }
        return true
    }