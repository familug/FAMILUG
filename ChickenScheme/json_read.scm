(use cjson)
(use http-client) ; requires install openssl

(define data (string->cjson (with-input-from-request "https://httpbin.org/get" #f read-string)))

(print "My user agent is")
(print (cdar (cdaddr (cjson-schemify data))))
