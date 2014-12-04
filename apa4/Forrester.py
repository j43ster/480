#!/usr/bin/python3

def Forrester4 (hist=[], score=[], query = False):

   period_1 = 60
   history_check = 10

   if query:
      return ["J4","Almost done"]
   else:
      if len(hist) == 0:
         ForresterStore = {}
         return 'C'
      elif len(hist) < period_1:
         return hist[-1][-1]
      elif len(hist) > (history_check + 1):

         tft_count = 0
         d_count = 0
         c_count = 0
         for i in range(1, history_check+1):
            if (hist[-i-1][0] == hist[-i][-1]):
               tft_count = tft_count + 1
            if (hist[-i][-1] == 'D'):
               d_count = d_count + 1
            if (hist[-i][-1] == 'C'):
               c_count = c_count + 1

         if (tft_count == history_check):
            return 'C'
         elif (c_count == history_check):
            return 'D'
         elif (d_count >= history_check): # defecter
            return 'D'

         return hist[-1][-1]
      else:
         return hist[-1][-1]
