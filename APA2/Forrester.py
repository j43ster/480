#!/usr/bin/python3

import random

def Forrester (hist=[], score=[], query = False):
   if query:
      return ["J","Almost done"]
   else:
      return 'D'
      if (len(hist) == 0):
         return 'D'
      
      opponentDefects = 0
      for turn in hist:
         if str(turn[1]) == 'D':
            opponentDefects += 1 
      
      defectRate = opponentDefects/len(hist)
      
      if random.random() <= defectRate:
         return 'D'
      else:
         return 'C'
