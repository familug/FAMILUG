###iptables — administration tool for IPv4 packet filtering and NAT

Each 'chain'is a list of rules which can match a set of packets.
Each rule specifies what to do with a packet that matches.
This is called a 'target', which may be a jump to a user-defined chain in the same table.  

## Targets
user defined chain or ACCEPT, DROP, QUEUE or RETURN.

## tables:
-t table

filter (default)
nat
mangle

## Command
-A chain rule-spec  : append rule(s) to the end of chain
-D chain rule-spec  : delete rule
-L [chain]          : list all rules in selected chain, used with -n avoid DNS lookup
-N chain            : new chain
-X chain            : delete chain
-P chain target     : set policy

## Paramater
-p  :protocol
-s  :source
-d  :des
-o  :out iface
-j  :target
-n  :numberic output
-v  :verbose
-line-numbers:  add linenubmer
