;; https://github.com/DennyZhang/challenges-leetcode-interesting/blob/master/automate.sh
;; Invoke elisp from command line: /Applications/Emacs.app/Contents/MacOS/Emacs-x86_64-10_9 --batch -l ../update_md.el
;; bash ./automate.sh update_md
(progn
  (add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/emacs-lisp")
  (add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/org")
  ;;(require 'org-install)
  (require 'ox-md)
  (switch-to-buffer 
   (find-file "README.org")
   (replace-string "[[url-external:" "" nil (point-min) (point-max))
   (replace-string "][challenges-leetcode-interesting]]" nil (point-min) (point-max))
   (replace-string "][leetcode.com]]" nil (point-min) (point-max))
   (goto-char (point-min))
   (org-export-to-file 'md "README.md")
   ;;(kill-buffer)
   (delete-file "README.md~")
   (message "Finished")
   )
  )
