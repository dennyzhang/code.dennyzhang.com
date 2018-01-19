;; https://github.com/DennyZhang/challenges-leetcode-interesting/blob/master/automate.sh
;; bash ./automate.sh update_md
(progn
  (add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/emacs-lisp")
  (add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/org")
  ;;(require 'org-install)
  (require 'ox-md)
  (switch-to-buffer 
   (find-file "README.org")
   (replace-string "[[url-external:" "")
   (replace-string "][challenges-leetcode-interesting]" "")
   (replace-string "][leetcode.com]" "")
   (org-export-to-file 'md "README.md")
   (delete-file "README.md~")
   )
  )
