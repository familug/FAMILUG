(define-record user name age email)
(define pika (make-user 'Pika 12 "pika@pymi.vn"))
(print (user-name pika))
