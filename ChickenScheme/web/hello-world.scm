(cond-expand
  (chicken-4 (use awful))
  (chicken-5 (import awful)))

(define-page (main-page-path)
 (lambda () "Hello world!"))
