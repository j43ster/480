#!/usr/bin/python3

ForresterStore = {}

def Forrester4 (hist=[], score=[], query = False):

   N = 100

   if query:
      return ["J4","Almost done"]
   else:
      if (len(hist) < N):
         return 'C'
      elif (len(hist) < 2*N):
         return hist[-1][-1]
      else:
         # look at last few turns and choose what they chose more of
         c_count = 0
         d_count = 0
         for i in range(N-1):
             if hist[-1][len(hist[-1])-i] == 'C':
                c_count = c_count + 1
             else:
                d_count = d_count + 1            
         if d_count > c_count:
            return 'D'
         else:
            return 'C'
