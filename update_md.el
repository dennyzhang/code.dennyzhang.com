;; https://github.com/DennyZhang/challenges-leetcode-interesting/blob/master/automate.sh
;; Invoke elisp from command line: /Applications/Emacs.app/Contents/MacOS/Emacs-x86_64-10_9 --batch -l ../update_md.el
;; bash ./automate.sh update_md
(add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/emacs-lisp")
(add-to-list 'load-path "/Applications/Emacs.app/Contents/Resources/lisp/org")
(require 'ox-md)

(org-add-link-type
 "url-external" nil
 (lambda (path desc format)
   (cond
    ((eq format 'html)
     ;; <a href="https://www.linkedin.com/feed/update/urn:li:activity:6282693138029043712">https://www.linkedin.com/feed/update/urn:li:activity:6282693138029043712</a>
     ;; https://www.linkedin.com/feed/update/urn:li:activity:6282693138029043712
     (setq url (replace-regexp-in-string "<a href=\"" "" path))
     (setq url (replace-regexp-in-string "\".*" "" url))
     (format "<a href=\"%s\" target=\"_blank\" rel=\"nofollow\">%s</a>" url desc)))))

(progn
  (switch-to-buffer 
   (find-file "README.org")
   (goto-char (point-min))
   (org-export-to-file 'md "README.md")
   (if (file-exists-p "README.md~")
       (delete-file "README.md~"))
   (kill-buffer)
   (message "Finished")
   )
  )
