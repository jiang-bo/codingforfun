#!/bin/sh
PROGNAME=`basename $0`

if [ $# -lt 1 ]; then
    echo "Usage: $PROGNAME <file> [-r rev]"
    exit;
fi

filename=$1
pid=$$
TEMP=/tmp/tmp.$pid.`basename $filename`
pv=

trap 'rm -f $TEMP' 0 1 2 15

if [ $# -eq 3 ] && [ $2 = "-r" ]; then
    pv="-r $3"
fi
svn cat $filename $pv > $TEMP
vimdiff $TEMP $filename
