#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-02-14 00:32:37 -0500 (Thu, 14 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab06/file_packager.bash $
#$Revision: 51881 $

s=$@
d=0
c=0

if (($# != 2))
then
    echo "Usage: file_packager.bash <directory> <file type>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable directory."
    exit 2
fi

r=$(mktemp -d XXXXX)

if ((mktemp != 0))
then
    echo "Error: Could not create working directory"
    exit 3
fi

find $1 -name \*\.$2 >> temp

while read file
do
    fl=${file##*/}
    for (( i=0; i<=$d; i++ ))
    do
        if [[ $fl == ${temp[i]} ]]
        then
            echo "Warning: $fl was already added to the archive"
            c=1
        fi
    done
    if ((c!=1))
    then
        temp[d]=$fl
        cp $file $r
        d=$d+1
    fi
    c=0
done <temp
tar -cf files.tar $r
if (( tar != 0))
then
    echo "Error: failed to create tar archive files.tar"
    exit 4
fi
gzip files.tar
if (( gzip !=0))
then
    echo "Error: failed to gzip tar archive files.tar"
    exit 5
fi

rm temp
exit 0
