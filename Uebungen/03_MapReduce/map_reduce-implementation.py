#!/usr/bin/python

import sys
import re
try:
    import simplejson as json
except ImportError:
    import json

import __builtin__

#os.environ["HADOOP_HOME"]="/naslx/projects/pn69si/mnmda001/software/hadoop-2.7.5"
#os.environ["PATH"]="/naslx/projects/pn69si/mnmda001/software/hadoop-2.7.5/bin:"+os.environ["PATH"]

def map(line):
    try:
        wline = line.split()
        http_resp = wline[-2]
        emit(http_resp, str(1))
    except:
        pass
    
def reduce(key, values):
    emit(key, str(sum(__builtin__.map(int,values))))

# Common library code follows:

def emit(key, value):
    """
    Emits a key->value pair.  Key and value should be strings.
    """
    try:
        print "\t".join( (key, value) )
    except:
        pass

def run_map():
    """Calls map() for each input value."""
    for line in sys.stdin:
        line = line.rstrip()
        map(line)

def run_reduce():
    """Gathers reduce() data in memory, and calls reduce()."""
    prev_key = None
    values = []
    for line in sys.stdin:
        line = line.rstrip()
        key, value = re.split("\t", line, 1)
        if prev_key == key:
            values.append(value)
        else:
            if prev_key is not None:
                reduce(prev_key, values)
            prev_key = key
            values = [ value ]

    if prev_key is not None:
        reduce(prev_key, values)

def main():
    """Runs map or reduce code, per arguments."""
    if len(sys.argv) != 2 or sys.argv[1] not in ("map", "reduce"):
        print "Usage: %s <map|reduce>" % sys.argv[0]
        sys.exit(1)
    if sys.argv[1] == "map":
        run_map()
    elif sys.argv[1] == "reduce":
        run_reduce()
    else:
        assert False

if __name__ == "__main__":
  main()
