#!/usr/bin/python3

ForresterStore = {}

def Forrester4 (hist=[], score=[], query = False):
   if query:
      return ["J4","Almost done"]
   else:
      if (len(hist) == 0):
         return 'C'
      else:
         return hist[-1][-1]
