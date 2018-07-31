cd  /Users/zdenny/Dropbox/git_code/challenges/challenges-leetcode-interesting/
for f in $(find . -name "README.org"); do
   echo $f
   cat $f ./misc/sns.txt > $f.bak
   mv $f.bak $f
done
