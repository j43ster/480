#!/usr/bin/python3
import model, lifting_rules, fol_grammar

while(True):
   sentence = input("Would you like to tell me anything else: ")
   if (sentence == "no"):
      break

   print(sentence)    
   fol_grammar.ProcessInput(sentence)
     
