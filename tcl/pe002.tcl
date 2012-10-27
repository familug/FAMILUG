#!/usr/bin/env tclsh
#Today: Sat Oct 27 17:26:54 ICT 2012
set result 0

set a 0
set b 1
set c 1
set MAX 4000000
while {$c < $MAX} {
    if {$c % 2 == 0} {
        set result [expr {$result + $c}]
    }
    set c [expr {$a + $b}] 
    set a $b
    set b $c
    incr i -1
}

puts "PE002 Result is $result"
