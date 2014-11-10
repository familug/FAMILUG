#!/bin/bash
# by Hung Nguyen Viet <hvn@familug.org>
# Nov 8 2014

echo "FAMILUG's list of essential Linux utilites 1.0"
BASIC="man ls cd pwd grep head tail cut cat uniq sort wc tar less file ln rm"
BASIC+=" cp mkdir find xargs test time uname chmod chown groups locate basename"
BASIC+=" touch top"
LEARNER="whatis whereis which"
PROGRAMMER="git ctags diff patch"
ADVANCE="sed awk"
NETWORK="ip ss iptables ngrep dig host whois ping traceroute curl wget telnet"
NETWORK+=" nc nmap"
SYSADMIN="su sudo ps kill ssh scp tmux screen nohup df du fdisk ar gdb "
SYSADMIN+="strace ulimit useradd crontab logger md5sum xxd yes iostat"
CRYPTO="openssl shasum base64 gpg"
ALL_UTILS="$BASIC $LEARNER $PROGRAMMER $ADVANCE $NETWORK $SYSADMIN $CRYPTO"
echo "TOTAL: $(echo $ALL_UTILS | wc -w)"

for util in $ALL_UTILS;
    do whatis $util
done
