#!/usr/bin/python3

import random

def RandomChoice(percentage):
   val = random.random()
   if (val < percentage):
      return 'D'
   else:
      return 'C'

def Defect (hist=[], score=[], query = False):
   if query:
      return ["D","I always Defect"]
   else:
      return 'D'

def Cooperate (hist=[], score=[], query = False):
   if query:
      return ["C","I always Cooperate"]
   else:
      return 'C'

def Ten (hist=[], score=[], query = False):
   if query:
      return ["10","I defect 10% of the time"]
   else:
      return RandomChoice(0.1)

def Twenty (hist=[], score=[], query = False):
   if query:
      return ["20","I defect 20% of the time"]
   else:
      return RandomChoice(0.2)

def Thirty (hist=[], score=[], query = False):
   if query:
      return ["30","30%"]
   else:
      return RandomChoice(0.3)

def Forty (hist=[], score=[], query = False):
   if query:
      return ["40","40%"]
   else:
      return RandomChoice(0.4)

def Fifty (hist=[], score=[], query = False):
   if query:
      return ["50","50/50"]
   else:
      return RandomChoice(0.5)

def Sixty (hist=[], score=[], query = False):
   if query:
      return ["60","60/40"]
   else:
      return RandomChoice(0.6)

def Seventy (hist=[], score=[], query = False):
   if query:
      return ["70","70/30"]
   else:
      return RandomChoice(0.7)

def Eighty (hist=[], score=[], query = False):
   if query:
      return ["80","80/20"]
   else:
      return RandomChoice(0.8)

def Ninety (hist=[], score=[], query = False):
   if query:
      return ["90","90/10"]
   else:
      return RandomChoice(0.9)

def Bad (hist=[], score=[], query = False):
   if query:
      return ["Bad","???"]
   else:
      return "?"
