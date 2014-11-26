#!/usr/bin/python2

import ast
import sys

infile = None

if (len(sys.argv) > 1):
   infile = sys.argv[1]

f = open(infile)

for line in f:
   line = line.strip()
   line = line.partition(": ")[2].strip()
   if line:
      line_list = ast.literal_eval(line)[0]
      (sentence, pos) = zip(*line_list)
      print(sentence)
      print(pos)
