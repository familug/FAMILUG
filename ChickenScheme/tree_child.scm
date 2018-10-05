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

(define (count-persons a-tree)
  (cond
    [(null? a-tree) 0]
    [else (+ 1
             (count-persons (person-father a-tree))
             (count-persons (person-mother a-tree))
             )]))


(define ChiPheo (make-person '() '() 'Chi 1990))
(define ThiNo   (make-person '() '() 'No  2000))
(define VangAnh (make-person ChiPheo ThiNo 'Anh 2010))

(print (born-2000-ancestor? VangAnh))
(print (born-2000-ancestor? ChiPheo))
(print (born-2000-ancestor? '()))

(print (count-persons VangAnh))
