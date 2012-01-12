#!/bin/sh
#Script to print battery info everyday. Should be used by cron
#By HVNSweeting
TODAY=$(date +%Y%m%d)
LOGDIR="batlog"
TAILNAME="_bat.log"
cat /proc/acpi/battery/BAT0/info > ~/$LOGDIR/$TODAY$TAILNAME
echo "Logged battery $TODAY"

