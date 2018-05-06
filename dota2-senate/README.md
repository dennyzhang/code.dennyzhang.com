# Leetcode: Dota2 Senate     :BLOG:Basic:


---

Dota2 Senate  

---

Similar Problems:  
-   Tag: [#game](https://code.dennyzhang.com/tag/game)

---

In the world of Dota2, there are two parties: the Radiant and the Dire.  

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:  

-   Ban one senator's right:

A senator can make another senator lose all his rights in this and all the following rounds.  

-   Announce the victory:

If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.  
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.  

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.  

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.  

Example 1:  

    Input: "RD"
    Output: "Radiant"
    Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
    And the second senator can't exercise any rights any more since his right has been banned.
    And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:  

    Input: "RDD"
    Output: "Dire"
    Explanation:
    The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
    And the second senator can't exercise any rights anymore since his right has been banned.
    And the third senator comes from Dire and he can ban the first senator's right in the round 1.
    And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Note:  
-   The length of the given string will in the range [1, 10,000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/dota2-senate)  

Credits To: [leetcode.com](https://leetcode.com/problems/dota2-senate/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/dota2-senate
    // Basic Ideas:
    //   ban_r: how many R should be banned in the following
    //   ban_d:
    //   r
    //   d
    // Complexity: Time O(n), Space O(1)
    func predictPartyVictory(senate string) string {
      ban_r, ban_d, r, d := 0, 0, 0, 0
      for _, ch := range senate {
        if ch == 'R' {
          if ban_r > 0 {
            ban_r -= 1
          } else {
            r += 1
    
            if d > 0 {
              d -= 1
            } else {
              ban_d += 1
            }
          }
        } else {
          if ban_d > 0 {
            ban_d -= 1
          } else {
            d += 1
            if r > 0 {
              r -= 1
            } else {
              ban_r += 1
            }
          }
        }
        // fmt.Println(ban_r, r, ban_d, d)
      }
    
      if d == r {
        if senate[0] == 'R' {
          return "Radiant"
        } else {
          return "Dire"
        }
      } else {
        if d>r {
          return "Dire"
        } else {
          return "Radiant"
        }
      }
    }