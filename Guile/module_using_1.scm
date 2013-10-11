#!/usr/bin/guile \
-s
!#

; by HVNSweeting <hvn@familug.org>
; at Sat Oct 12 00:29:46 ICT 2013

(use-modules (ice-9 popen))
(use-modules (ice-9 rdelim))
(define p (open-input-pipe "ls -l /etc"))
(display (read-line p)) (newline)
(display (read-line p)) (newline)
(display (read-line p)) (newline)
(display (read-line p)) (newline)

#!
hvn@archhvn: ~/Github/FAMILUG/Guile (master) $ ./module_using_1.scm
total 1504
-rw-r--r-- 1 root root  12491 Mar 30  2013 abcde.conf
-rw-r--r-- 1 root root     44 Jun 20 08:21 adjtime
drwxr-xr-x 2 root root   4096 Aug  4 15:01 adobe
!#
