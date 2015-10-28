;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.





;; lisp-interaction-mode


(+ 1 2)
(+ 3 (+ 1 2))
(setq my-name "Bastien")
(insert "Hello!")
(insert "Hello" " world!")
(insert "Hello, I am " my-name)
(defun hello () (insert "Hello, I am " my-name))
(hello)
(defun hello (name) (insert "Hello " name))
(hello "you")
;; next
(switch-to-buffer-other-window "*test*")
(progn
  (switch-to-buffer-other-window "*test*")
  (hello "you"))
(progn
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (hello "there"))
(progn
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (hello "you")
  (other-window 1))
(let ((local-name "you"))
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (hello local-name)
  (other-window 1))
(format "Hello %s!\n" "visitor")
(defun hello (name)
  (insert (format "Hello %s!\n" name)))
(hello "you")
(defun greeting(name)
  (let ((your-name "Bastien"))
    (insert (format "Hello %s!\n\nI am %s."
		    name
		    your-name))))
(greeting "you")
(read-from-minibuffer "Enter your name: ")
(defun greeting (from-name)
  (let ((your-name (read-from-minibuffer "Enter your name:")))
    (insert (format "Hello!\n\nI am %s and you are %s."
		    from-name
		    your-name))))
(greeting "Bastien")
(defun greeting(from-name)
  (let ((your-name (read-from-minibuffer "Enter your name: ")))
    (switch-to-buffer-other-window "*test*")
    (erase-buffer)
    (insert (format "Hello %s!\n\nI am %s." your-name from-name))
    (other-window 1)))
(greeting "Bastien")
;; next




