#!/usr/bin/python3

import string

#class Sentence:
#   def __init__(self, sentence):
#      self.sentence = sentence
#
#   def interpret(KB):
#      sentence.interpret(KB)
#
#   def print(self, pre = ""):
#      print(str(pre) + "Not:")
#      self.sentence.print(str(pre) + "   ")

class Not:
   def __init__(self, sentence):
      self.sentence = sentence

   def interpret(self, KB):
      value = self.sentence.interpret(KB)
      return not(value)

   def __str__(self):
      return str(self.sentence) 

   def print(self, pre = ""):
      print(str(pre) + "Not:")
      self.sentence.print(str(pre) + "   ")

class Equals:
   def __init__(self, lhs, rhs):
      self.lhs = lhs
      self.rhs = rhs

   def interpret(self, KB):
      v1 = self.lhs.interpret(KB)
      v2 = self.rhs.interpret(KB)
      # not sure how I compare these two items
      # if they are not bools or strings
      return (v1 == v2)

   def print(self, pre = ""):
      print(str(pre) + "Equals:")
      self.lhs.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class And:
   def __init__(self, lhs, rhs):
      self.lhs = lhs
      self.rhs = rhs

   def interpret(self, KB):
      v1 = self.lhs.interpret(KB)
      v2 = self.rhs.interpret(KB)
      return (v1 and v2)

   def print(self, pre = ""):
      print(str(pre) + "Equals:")
      self.lhs.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class Or:
   def __init__(self, lhs, rhs):
      self.lhs = lhs
      self.rhs = rhs

   def interpret(self, KB):
      v1 = self.lhs.interpret(KB)
      v2 = self.rhs.interpret(KB)
      return (v1 or v2)

   def print(self, pre = ""):
      print(str(pre) + "Equals:")
      self.lhs.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class Implies:
   def __init__(self, lhs, rhs):
      self.lhs = lhs
      self.rhs = rhs

   def interpret(self, KB):
      v1 = self.lhs.interpret(KB)
      v2 = self.rhs.interpret(KB)
      if v1:
         return (v2 == true)
      else:
         return True

   def print(self, pre = ""):
      print(str(pre) + "Equals:")
      self.lhs.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class Iff:
   def __init__(self, lhs, rhs):
      self.lhs = lhs
      self.rhs = rhs

   def interpret(self, KB):
      v1 = self.lhs.interpret(KB)
      v2 = self.rhs.interpret(KB)
      if ((v1 and v2) or (not(v1) and not(v2))):
         return True
      else:
         return False

   def print(self, pre = ""):
      print(str(pre) + "Equals:")
      self.lhs.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class All:
   def __init__(self, var, rhs):
      self.var = var 
      self.rhs = rhs

   def interpret(self, KB):
      # this one is annoying
      print("interpret All")

   def print(self, pre = ""):
      print(str(pre) + "All:")
      self.var.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class Exists: 
   def __init__(self, var, rhs):
      self.var = var 
      self.rhs = rhs

   def interpret(self, KB):
      # this one is annoying
      print("interpret Exists")

   def print(self, pre = ""):
      print(str(pre) + "Exists:")
      self.var.print(str(pre) + "   ")
      self.rhs.print(str(pre) + "   ")

class Value:
   def __init__(self, name):
      self.name = name

   def interpret(self, KB):
      # this one is annoying
      # lookup self.name in KB area where you store variables from quantifiers
      print("interpret Value")

   def __str__(self):
      return str(self.name) 

   def print(self, pre):
      print(pre + "Value: " + self.name)

def BinaryParse(node_type, fragment):

   lhs = None
   rhs = None

   separators = []
   separators.append((fragment.find("("), "("))
   separators.append((fragment.find(","), ","))
  
   separators = sorted(separators, key=lambda tup: tup[0])
   separators = [x for (i, x) in separators if i >= 0]
   separator = separators[0]
   (pre, separator, post) = str.partition(fragment, separator)

   print("Entered BinaryParse with type: " + str(node_type) + ", and fragment '" + str(fragment) + "'")
   print("   pre: '" + str(pre) + "'")
   print("   separator: '" + str(separator) + "'")
   print("   post: '" + str(post) + "'")

   remainder = None
   if (separator == "("):
      print("BinaryParse, found a '('")
      lhs, remainder = globals()[pre].parser(pre, post)
      #return (globals()[node_type](child_node), remainder)

   elif (separator == ","):
      print("BinaryParse, found a ','")
      # the pre is either a value or a variable 
      # for now just call them all values
      lhs = Value(pre)
      remainder = post

   # so far we have gotten the lhs
   # in the case Binary(Not(True), 2) we will have remainder ", 2)"
   # in the case Binary(a, b) we will have remainder " 2)"
   print("BinaryParse remainder after lhs: " + str(remainder))
   if (remainder[0] == ","):
      remainder = remainder[1:]

   # after the ',' is stripped we can process like a Unary operator
   separators = []
   separators.append((remainder.find("("), "("))
   separators.append((remainder.find(")"), ")"))
  
   print(str(separators))
   separators = sorted(separators, key=lambda tup: tup[0])
   separators = [x for (i, x) in separators if i >= 0]
   separator = separators[0]
   (pre, separator, post) = str.partition(remainder, separator)

   print("2: Entered BinaryParse with type: " + str(node_type) + ", and fragment '" + str(remainder) + "'")
   print("   pre: '" + str(pre) + "'")
   print("   separator: '" + str(separator) + "'")
   print("   post: '" + str(post) + "'")

   if (separator == "("):
      print("BinaryParse, found a '('")
      rhs, remainder = globals()[pre].parser(pre, post)

   elif (separator == ")"):
      print("BinaryParse, found a ')'")
      # the pre is either a value or a variable 
      # for now just call them all values
      rhs = Value(pre)
      remainder = post

   print("BinaryParse Complete")
   print("lhs: " + str(lhs))
   print("rhs: " + str(rhs))
   print("remainder: " + str(remainder))
   return (globals()[node_type](lhs, rhs), remainder)

def UnaryParse(node_type, fragment):

   separators = []
   separators.append((fragment.find("("), "("))
   separators.append((fragment.find(")"), ")"))
  
   separators = sorted(separators, key=lambda tup: tup[0])
   separators = [x for (i, x) in separators if i >= 0]
   separator = separators[0]
   (pre, separator, post) = str.partition(fragment, separator)

   print("Entered UnaryParse with type: " + str(node_type) + ", and fragment '" + str(fragment) + "'")
   print("   pre: " + str(pre))
   print("   separator: " + str(separator))
   print("   post: " + str(post))

   if (separator == "("):
      print("UnaryParse, found a '('")
      child_node, remainder = globals()[pre].parser(pre, post)
      return (globals()[node_type](child_node), remainder)

   elif (separator == ")"):
      print("UnaryParse, found a ')'")
      # the pre is either a value or a variable 
      # for now just call them all values
      return (globals()[node_type](Value(pre)), post)

def Parse(sentence):

   # set the parsers for the node types
   Not.parser = UnaryParse
   Equals.parser = BinaryParse
   And.parser = BinaryParse
   Or.parser = BinaryParse
   Implies.parser = BinaryParse
   Iff.parser = BinaryParse
   All.parser = BinaryParse
   Exists.parser = BinaryParse

   # remove all whitespace from the string
   sentence = sentence.replace(" ", "")
   # start the parse sequence by calling the parser for the first node 
   # in the tree
   parts = str.partition(sentence, "(")
   node_type = parts[0]
   fragment = parts[2]
   #tree, remainder = 
   (tree, remainder) = globals()[node_type].parser(node_type, fragment)
   #print(str(tree))
   tree.print()


# How do I parse the rules following the function only thing
# find the first "(" the text before this is the name of an operator
#  
# possibilities after parsing the "("
#    next separator = (
#       The start of a new node that is a child of this one
#       how do I parse this? 
#    next separator = ,
#       I finished an entire node and move on to the next one
#
#    next separator = )

