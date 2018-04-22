# LintCode: Radar Detection     :BLOG:Basic:


---

Radar Detection  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

There is a bunch of radars on a 2D plane(Radar has x, y coordinates, and a radius r which is the range can be detected). Now, there is a car that passes through the range of y = 0 and y = 1 and cannot be detected by the radar. If the car is detected, return YES, otherwise NO.(You can consider that the car is a line segment of length 1 and goes straight from x = 0 to the right)  

Notice  
-   The number of radars is n, n <= 1000
-   The radar's coordinate x is a non-negative integer, y is an integer, and r is a positive integer.

Example  

    Given coordinates = [[0,2]], radius = [1], return "NO".
    
    Explanation:
    There is a radar at (0,2) that can detect a circle with a radius of 1 centered on (0,2) and the car will not be detected.

    Given coordinates = [[0,2],[1,2]], radius = [1,2], return "YES"
    
    Explanation:
    There is a radar at (0,2) that can detect a circular area with a radius of 2 with a center of (0,2). Radars at (1,2) can detect (1,2) as Center, circular area with 2 radius. The No. 2 radar can detect the passing of the car.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/radar-detection)  

Credits To: [leetcode.com](http://www.lintcode.com/en/problem/radar-detection/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/radar-detection
    ## Basic Ideas: only check the height
    ## Complexity: Time O(n), Space O(1)
    """
    Definition for a point.
    class Point:
        def __init__(self, a=0, b=0):
            self.x = a
            self.y = b
    """
    
    class Solution:
        """
        @param coordinates: The radars' coordinate
        @param radius: Detection radius of radars
        @return: The car was detected or not
        """
        def radarDetection(self, coordinates, radius):
            for i in range(len(coordinates)):
                y = coordinates[i].y
                r = radius[i]
                start, end = y-r, y+r
                if start<=0 and end>=1:
                    return "YES"
            return "NO"