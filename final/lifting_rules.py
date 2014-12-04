#!/usr/bin/python2

import pyswip

#The Simple Rules:

class LiftingRules:

   p = pyswip.Prolog()

   def __init__(self):
      pass

   def initialize(self):
      self.p.consult("rules.pl")

   def ask(self, question):
      if not(question[-1] == '.'):
         question = question + "."
      return list(self.p.query(question))

   def tell(self, fact):
      self.p.assertz(fact)

   def query(self, query):
      return list(self.p.query(query))

def test():
    lines = [("assertz(father(michael,john)).","Michael is the father of John"),
            ("assertz(father(michael,gina)).","Michael is the father of Gina"),
            ("father(michael,john).","Is Michael father of John?"),
            ("father(michael,olivia).","Is Michael father of Olivia?"),
            ("father(michael,X).","Michael is the father of whom?"),
            ("father(X,Y).","Who is the father of whom?")]

    lines = [("assertz(benchpress_max(jeff, hundred)).", ""),
             ("benchpress_max(jeff, X).", "")]

    prolog = pyswip.Prolog()

    for code, comment in lines:
        print "?-", code, "[", comment, "]"
        print list(prolog.query(code))

    for r in prolog.query("father(X,Y)"):
        print r["X"], "is the father of", r["Y"]

