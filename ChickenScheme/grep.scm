(use irregex)
(use regex)
(use utils)

(define (grep-from-file pattern filename)
  (grep pattern (irregex-split "\n" (read-all filename))))

(define (display-lines lines)
  (for-each (lambda (x) (begin (display x) (newline)))
            lines))

(let ((args (argv)))
    (let ((pattern (car (cdr args))) (filename (car (cdr (cdr args)))))
      (display-lines (grep-from-file pattern filename))))
