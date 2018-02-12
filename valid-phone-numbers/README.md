# Leetcode: Valid Phone Numbers     :BLOG:Medium:


---

Word Frequency  

---

Similar Problems:  
-   Tag: [#shell](https://brain.dennyzhang.com/tag/shell)

---

Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.  

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)  

You may also assume each line in the text file must not contain leading or trailing white spaces.  

For example, assume that file.txt has the following content:  

    987-123-4567
    123 456 7890
    (123) 456-7890

Your script should output the following valid phone numbers:  

    987-123-4567
    (123) 456-7890

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-phone-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-phone-numbers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/valid-phone-numbers
    grep -iE '^\([0-9][0-9][0-9]\) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$' file.txt