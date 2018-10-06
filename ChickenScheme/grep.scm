(use regex)
(use utils)

(define (grep-from-file pattern filename)
  (grep pattern (read-lines filename)))

(define (display-lines lines)
  (for-each (lambda (x) (begin (display x) (newline)))
            lines))

(let ((args (argv)))
    (let ((pattern (cadr args)) (filename (caddr args)))
      (display-lines (grep-from-file pattern filename))))
