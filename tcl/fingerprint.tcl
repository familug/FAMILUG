#!/bin/tclsh

set victim [lindex $argv 0]
puts "Fingerprinting $victim"

set SEP "-------------"
puts [exec ping -c 3 $victim]

puts $SEP

puts "Scanning open port..."
set nmap_out [exec nmap -sT $victim]

set found_80 [string match *80/tcp* $nmap_out]
if { $found_80 } {
    puts "WARNING 80 is OPEN"
}
puts $nmap_out
\
set victic_verson [exec nmap -v -O $victim]
puts $victic_verson


# get list of host scanned from gateway, find them all
