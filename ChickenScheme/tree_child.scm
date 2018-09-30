(define-record person father mother name year)
;; born-2000-ancestor? : ftn -> boolean
;; to determine whether a-ftree contains a child
;; record with 2000 in year field
(define (born-2000-ancestor? one)
  (cond
    [(null? one) #f]
    [else (or (= (person-year one) 2000)
              (or (born-2000-ancestor? (person-father one))
                  (born-2000-ancestor? (person-mother one))))]))

(define ChiPheo (make-person '() '() 'Chi 1990))
(define ThiNo   (make-person '() '() 'No  2000))
(define VangAnh (make-person ChiPheo ThiNo 'Anh 2010))

(print (born-2000-ancestor? VangAnh))
(print (born-2000-ancestor? ChiPheo))
(print (born-2000-ancestor? '()))
