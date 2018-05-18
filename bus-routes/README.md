# Leetcode: Bus Routes     :BLOG:Basic:


---

Bus Routes  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs)

---

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.  

    For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.  

Example:  

    Input: 
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    Output: 2
    Explanation: 
    The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Note:  

-   1 <= routes.length <= 500.
-   1 <= routes[i].length <= 500.
-   0 <= routes[i][j] < 10 ^ 6.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/bus-routes)  

Credits To: [leetcode.com](https://leetcode.com/problems/bus-routes/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/bus-routes
    // Basic Ideas: BFS + hashmap
    //
    // map: from point to route id list
    // If we have examined all stops in one route, we mark the route as visited
    // If we have examined one stop, we mark the stop as visited
    //
    // Complexity: Time O(n), Space O(n)
    func numBusesToDestination(routes [][]int, S int, T int) int {
        m := make(map[int][]int)
        route_visited := make([]bool, len(routes))
        point_visited := make(map[int]bool)
        for i, route := range routes {
            for _, stop := range route {
                m[stop] = append(m[stop], i)
            }
        }
        // No need to take bus
        if S==T { return 0 }
        // No bus stop at the start point
        if len(m[S]) == 0 { return -1 }
        queue := []int{}
        // Initialize queue
        level := 1
        for _, route_id := range m[S] {
            if route_visited[route_id] == false {
                for _, stop := range routes[route_id] {
                    if stop == T { return level }
                    if point_visited[stop] == false {
                        queue = append(queue, stop)
                        point_visited[stop] = true
                    }
                }
                route_visited[route_id] = true
            }
        }
        for len(queue) != 0 {
            level++
            items := []int{}
            for _, stop := range queue {
                // find nex route to explore
                for _, route_id := range m[stop] {
                    if route_visited[route_id] == false {
                        for _, stop2 := range routes[route_id] {
                            if stop2 == T { return level }
                            if point_visited[stop2] == false {
                                items = append(items, stop2)
                                point_visited[stop2] = true
                            }
                        }
                        route_visited[route_id] = true
                    }
                }
            }
            queue = []int{}
            for _, stop:= range items {
                queue = append(queue, stop)
            }
        }
        return -1
    }