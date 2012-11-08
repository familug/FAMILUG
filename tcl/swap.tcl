#!/usr/bin/env tclsh
proc swap {a b} {
    upvar $a one
    upvar $b two
    set temp $one
    set one $two
    set two $temp
}

set x 5
set y 7
puts "X: $x Y: $y"
swap x y
puts "X: $x Y: $y"
