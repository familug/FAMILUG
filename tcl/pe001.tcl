# PE001 in tcl

set result 0

for {set i 0} {$i < 1000} {incr i} {
    if {$i % 3 == 0 || $i % 5 == 0} {
    set result [expr {$result + $i}]
    }
}

puts $result
