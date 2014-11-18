#!/usr/bin/python3

# -------------------------------------------------------------
# notes
# -------------------------------------------------------------
# operator precedence:  !, =, &, |, IMP, IFF
# quantifiers: ALL, EXISTS
# variables: lowercase ex (x, a, s)
# Constants: start with an uppercase letter ex (John, A, X1)

#  symbol   |    name
#   IMP     |  implies
#   IFF     | if and only if
#   AND     |    and
#   OR      |     or
#   ()      |   changes order of operation

# ---------------------------------------------------------------
# Grammar of First Order Logic
# ---------------------------------------------------------------
# Sentence -> AtomicSentence | ComplexSentence
# AtomicSentence -> Predicate | Predicate(Term, ...) | Term = Term
# ComplexSentence -> (Sentence) | [Sentence]
                 # | !Sentence
                 # | Sentence & Sentence
                 # | Sentence | Sentence
                 # | Sentence => Sentence
                 # | Sentence <=> Sentence
                 # | Quantifier Variable, ... Sentence
# Term -> Function(Term, ...)
      # | Constant
      # | Variable
# Quantifier -> ALL | EXISTS
# Constant -> A | X1 | John
# Variable -> a | x | s
# Predicate -> True | False | After | Loves | Raining
# Function -> Mother | LeftLeg

import re
import lifting_rules

def Lookup(Sentence):
   print("lookup")

def Implies(LHS, RHS):
   print("implies")

def Iff(LHS, RHS):
   print("iff")

def Not(predicate):
   print("not")

def And(LHS, RHS):
   print("and")

def Or(LHS, RHS):
   print("or")

def Equals(LHS, RHS):
   print("equals")

def Exists(variable, sentence):
   print("exists")

def All(variable, sentence):
   print("all")

def Tell(sentence):
   print("TEll")

def Ask(sentence):
   print("Ask")

def AskVars(sentence):
   print("AskVars")

def ProcessInput(sentence):
   breakdown = str.partition(sentence[:-1], "(")
   function = breakdown[0]
   parameters = breakdown[2]
   print("Breakdown is: " + str(function) + ", " + str(parameters))
   globals()[function](parameters)



class BinaryNode():
   Name = ""
   LHS = ""
   RHS = ""

# want to parse my psuedo language
# should be able to get away with only function parsing
def ParseTree(code):

   Tree
   while (code = str.partition(code, "(")):
      














