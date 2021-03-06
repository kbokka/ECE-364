#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-17 15:55:52 -0500 (Sun, 17 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab07/statify.py $
#$Revision: 52016 $

import sys
import os

l=0
w=0
c=0

n=sys.argv[1:]

if len(sys.argv) != 3:
    print "Usage: statify.py"
    sys.exit(1)
if not os.access(n[0], os.R_OK):
    print "%s does not esixt!" % (n[0],)
    sys.exit(1)
if not os.path.isfile(n[0]):
    print "%s is not an ordinary file!" % (n[0],)
    sys.exit(1)
if os.path.exists(n[1]):
    print "%s already exists!" % (n[1],)
    sys.exit(1)

InFile = open(n[0], "r")
OutFile = open(n[1], "w+")

for line in InFile:
    l += 1
    OutFile.write("%d: %s" %(l,line,))
    words = line.split()
    w += len(words)
    for g in words:
        c += len(g)
        a=float(float(c)/float(w))
OutFile.write("--- Document statistics ----\n")
OutFile.write("Line count: %d\n" % (l,))
OutFile.write("Words count: %d\n" % (w,))
OutFile.write("Average word size: %.3f\n" % (a,))

InFile.close()
OutFile.close()

sys.exit(0)
