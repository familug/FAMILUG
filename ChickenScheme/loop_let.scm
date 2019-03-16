					; Print to ten
(let loop ((i 0))
  (if (> i 10) #f
      (begin
	(print i)
	(loop (+ i 1)))))

					; Print to zero
(let countdown ((i 10))
  (if (= i 0) 'tada
      (begin
	(print i)
	(countdown (- i 1)))))

					; Using when for shorter, i.e   (if TEST (begin EXP1 EXP2 ...))

(let loop ((i 0))
  (when (< i 10)
	(print i)
	(print "When")
	(loop (+ i 1))
	)
  )
