
# Leetcode: Design Snake Game     :BLOG:Medium:

---

Design Snake Game  

---

Similar Problems:  

-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign), [game](https://code.dennyzhang.com/tag/game)

---

Design a [Snake game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) that is played on a device with screen size = width x height. [Play the game online](http://patorjk.com/games/snake/) if you are not familiar with the game.  

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.  

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.  

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.  

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.  

Example:  

    Given width = 3, height = 2, and food = [[1,2],[0,1]].
    
    Snake snake = new Snake(width, height, food);
    
    Initially the snake appears at position (0,0) and the food at (1,2).
    
    |S| | |
    | | |F|
    
    snake.move("R"); -> Returns 0
    
    | |S| |
    | | |F|
    
    snake.move("D"); -> Returns 0
    
    | | | |
    | |S|F|
    
    snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
    
    | |F| |
    | |S|S|
    
    snake.move("U"); -> Returns 1
    
    | |F|S|
    | | |S|
    
    snake.move("L"); -> Returns 2 (Snake eats the second food)
    
    | |S|S|
    | | |S|
    
    snake.move("U"); -> Returns -1 (Game over because snake collides with border)

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/design-snake-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/design-snake-game/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/design-snake-game
    ## Basic Ideas: queue + hashmap
    ##              queue: coordinates for all parts of the snake
    ##              set: check whether snake will hit itself
    ##
    ##  Assumption: If snake hit itself, it will die
    ##
    ## Complexity:
    class SnakeGame:
    
        def __init__(self, width, height, food):
    	"""
    	Initialize your data structure here.
    	@param width - screen width
    	@param height - screen height 
    	@param food - A list of food positions
    	E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    	:type width: int
    	:type height: int
    	:type food: List[List[int]]
    	"""
    	self.width, self.height = width, height
    	self.foods = collections.deque(food)
    	self.snake_points = collections.deque([(0, 0)])
    	self.snake_points_set = set([(0, 0)])
    	self.food_index = 0
    
        ## Complexity: Time O(1), Space O(k), k is the length of the snake
        def move(self, direction):
    	"""
    	Moves the snake.
    	@param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    	@return The game's score after the move. Return -1 if game over. 
    	Game over when snake crosses the screen boundary or bites its body.
    	:type direction: str
    	:rtype: int
    	"""
    	offsets = {'U':(-1, 0), 'L':(0, -1), 'R':(0, 1), 'D':(1, 0)}
    	x, y = self.snake_points[-1][0], self.snake_points[-1][1]
    	x2, y2 = x+offsets[direction][0], y+offsets[direction][1]
    
    	# hit the border
    	if x2<0 or x2>=self.height or y2<0 or y2>=self.width: return -1
    
    	# hit itself. Notice: Need to check the first node of the snake
    	if (x2, y2) in self.snake_points_set and (x2,y2) != self.snake_points[0]:
    	    return -1
    
    	# get no food
    	if len(self.foods) == 0 or [x2, y2] != self.foods[0]:
    	    first_point = self.snake_points.popleft()
    	    self.snake_points.append((x2, y2))
    
    	    self.snake_points_set.remove(first_point)
    	    self.snake_points_set.add((x2, y2))
    	    return self.food_index
    
    	# get food
    	self.foods.popleft()
    	self.food_index += 1
    
    	# update snake points
    	self.snake_points.append((x2, y2))
    	self.snake_points_set.add((x2, y2))
    
    	return self.food_index
    
    # Your SnakeGame object will be instantiated and called as such:
    # obj = SnakeGame(width, height, food)
    # param_1 = obj.move(direction)

