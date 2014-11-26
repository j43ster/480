#!/usr/bin/python2
import lifting_rules
import parser


# initialize rules and facts
kb = lifting_rules.LiftingRules()
kb.initialize()

open('dynamicfacts', 'a').close()

dynamicfacts = open('dynamicfacts', 'r+')
for fact in dynamicfacts:
   kb.tell(fact)

dynamicfacts.close()
dynamicfacts = open('dynamicfacts', 'a')

client_name = raw_input("Hi, I'm an AI bot that knows about weight lifting. What is your name? ")
kb_name = "'%s'" % client_name.lower()

# if this is a returning person, welcome them back
returning = kb.ask("lifter(%s)" % kb_name)

if (len(returning)):
   print "Welcome Back, %s" % client_name
else:
   kb.tell("lifter(%s)" % kb_name)
   print "robot: I'm glad you've decided to talk to me!"

# in either case, tell them how you work. i.e. ? to ask a question, period to tell me something
# maybe provide a list of common keywords to talk about that are included in the ontology 

while(True):
   sentence = raw_input(client_name + ": ")

   if (sentence == "quit" or sentence == "exit"):
      break

   # split sentences up 
   # for each sentence in response, send it through nltk
   # to try to pull out FOL queries, facts, and rules
   #print kb.query(sentence) 
     
   # send FOL through rules moduqe 
   if (sentence.startswith("try: ") or sentence.find("(") == -1):
      if sentence.startswith("try: "):
         sentence = sentence.partition("try: ")[2]
      #processed = parser.ie_preprocess(sentence)
      #print processed
      #if (sentence.lower().find("i ") != -1): 
      #   nouns = [i for (i, j) in processed[0] if j == "NN"]
      #   #print str(nouns)
      #   for noun in nouns:
      #      action = "%s(%s)" % (noun, kb_name)
      #      print action
      #      kb.tell(action)
      #
      #else:
      #   print "robot: I could not make sense of your sentence :("
      meaning = parser.extract_meaning(sentence, kb_name) 
      print(str(meaning))
      kb.tell(meaning)
      dynamicfacts.write(meaning)
   elif (sentence[-1] == "?"):
      result = kb.ask(sentence[:-1])

      if (result == []):
         print "robot: False"
      elif (len(result) >= 1 and isinstance(result[0], str) and len(set(result)) == 1):
         print "robot: True"
      else:
         print "robot: %s" % str(result)

   else:
      if (sentence[-1] == "."):
         sentence = sentence[:-1]

      kb.tell(sentence)
      dynamicfacts.write(sentence)
      dynamicfacts.write("\n")
      
# any responses to the client       
print("Goodbye, " + str(client_name))

# cleanup
dynamicfacts.close()
