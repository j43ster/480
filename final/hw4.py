#!/usr/bin/python

import re

# it doesnt need to be fast, it just needs to work

# some facts to test with
facts = [
         "Tell(Mother(Janice, Jeff))",
         "Tell(Father(Russ, Jeff))",
         "Tell(Father(Russ, Jake))",
         "Ask(Father(Russ))",
         "Ask(Father(Russ, Jeff))",
         "Ask(Father(Russ, Will))",
         "Ask(Father(Jeff))",
         "AskVars(Father(Russ))",
         "AskVars(Father(Russ, Jeff))",
         "AskVars(Father(Russ, Will))",
         "AskVars(Father(Jeff))",
        ]

rules = [
         "ALL(m, c) Mother(m, c) IFF Female(m) & Parent(m, c)",
         "ALL(f, C) Father(f, c) IFF Male(f) & Parent(f, c)",
         "ALL(c, p) Child(c, p) IFF Parent(p, c)",
         "ALL(g, c) Grandparent(g, c) IFF Exists(p) Parent(p, c) & Parent(g, p)
        ]

# dont really need all of these
class KnowledgeBase:
       Child = []
       Parent = []
       Male = []
       Female = []
       Mother = []
       Father = []

KB = KnowledgeBase()

def start():
   while(True):
      print("Do you have anything to tell me? ")
      fact = input()
      if (fact == "no"):
         break
      print("received a new fact: " + fact)

def Mother(KB, mother, child):
   KB.Mother.append((mother, child))
   KB.Child.append((child, mother))
   return mother + " is the mother of " + child

def Father(KB, father, child):
   KB.Father.append((father, child))
   KB.Child.append((child, father))
   return father + " is the father of " + child

def Ask(KB, question):
   breakdown = str.split(question[:-1], "(")
   relation = breakdown[0]
   parameters = [x.strip() for x in str.split(breakdown[1], ",")]

   result = "False"
   for item in getattr(KB, relation):
      count = 0
      for i, param in enumerate(parameters):
         if (param == item[i]):
            count = count + 1
      if (count == len(parameters)):
         result = "True"

   return result

def AskVars(KB, question):
   breakdown = str.split(question[:-1], "(")
   relation = breakdown[0]
   parameters = [x.strip() for x in str.split(breakdown[1], ",")]

   result = []
   for item in getattr(KB, relation):
      count = 0
      for i, param in enumerate(parameters):
         if (param == item[i]):
            count = count + 1
      if (count == len(parameters)):
         result.append(item)

   return result

def Tell(KB, fact):
   # get the name and parameters of the fact
   breakdown = str.split(fact[:-1], "(")
   relation = breakdown[0]
   parameters = [x.strip() for x in str.split(breakdown[1], ",")]

   methodToCall = globals()[relation]
   return methodToCall(KB, parameters[0], parameters[1])

def ProcessInput(KB, input):
   # get action from input
   breakdown = str.partition(input[:-1], "(")
   action = breakdown[0]
   details = breakdown[2]

   return globals()[action](KB, details)   

def test():
   for fact in facts:
      res = ProcessInput(KB, fact)
      print(str(fact) + ": " + str(res))
