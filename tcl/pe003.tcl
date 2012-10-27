#!/usr/bin/env tclsh
#Today: Sat Oct 27 17:36:11 ICT 2012

proc prime_factor num {
    set i 3
    while {$num > 1} {
        if {$num % $i == 0} {
            set num [expr {$num / $i}]
        }
        incr i 2
    }
    return [expr {$i - 2}]
}

set NUMBER 600851475143
puts [prime_factor $NUMBER]
