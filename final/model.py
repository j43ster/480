#!/usr/bin/python3

class Program():
   Name = ""
   Purpose = ""
   
   Lifts = {} # 
   # sample lift
   # Lifts = { "1" = { "1" = {Name = "Bench Press", Sets = 5, Reps = 10}}, }

class Lifter():
   # general information
   Name = ""
   Sex = ""
   weight = 0

   # other information
   Type = "" # Powerlifter, Bodybuilder 

   # 4 main lift maxes
   BenchMax = 0
   SquatMax = 0
   OHPMax = 0
   DeadliftMax = 0

   # Program Information
   Program = ""
