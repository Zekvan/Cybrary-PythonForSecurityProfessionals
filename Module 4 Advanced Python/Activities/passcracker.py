# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hashlib import md5
import sys


def passcrack(pass_hash):
    for i in range(1001):#try 1-1000
        m = md5()
        m.update(str(i))
        test_hash = m.hexdigest()
        if (test_hash != pass_hash):
            print "Failed: %d\t=>\t%s\t != \t%s" % (i, test_hash, pass_hash)
        else:
            print "Success: %d\t=>\t%s " % (i, test_hash)
            return

m=md5()
m.update(str(sys.argv[1]))
passcrack(m.hexdigest())
