#!/bin/bash

bg ()
# set zeroCount
{
	zeroCount=0
	zeroCountMax=0
	oneSeen=false
	n=$1

	until [ "$n" -eq 0 ]
	do
		let "bit = $n % 2"
		if [ "$bit" -eq "1" ]; then
			(($zeroCount > $zeroCountMax)) && zeroCountMax=$zeroCount
			zeroCount=0
			oneSeen=true
		elif [ "$oneSeen" = true ]; then
			let "zeroCount = $zeroCount + 1"
		fi
		#echo $bit, $zeroCount, $zeroCountMax, $n
		let "n = $n >> 1"
	done
	zeroCount=$zeroCountMax
}


bg 1041
if [ "$zeroCount" -ne "5" ]; then
	echo "1041 failed"
fi
bg 529
if [ "$zeroCount" -ne "4" ]; then
	echo "529 failed"
fi
bg 0
if [ "$zeroCount" -ne "0" ]; then
	echo "0 failed"
fi
bg 9
if [ "$zeroCount" -ne "2" ]; then
	echo "9 failed"
fi
