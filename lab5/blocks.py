#!/usr/bin/python3

class Block():
   def __init__(self):
      self.clear = "?"
      self.on = "?"

   def set_clear(self, value):
      self.clear = value

   def is_clear(self):
      if self.clear:
         return True 
      else:
         return False

   def set_on(self, b):
      self.on = b

   def is_on(self, x):
      return self.on == x

   def __str__(self):
      return ""

   def __repr__(self):
       return str("{ Block: on = '" + str(self.on) + "', clear = '" + str(self.clear) + "' }")

class State():
   def __init__(self):
      self.blocks = {}

   def clear(self, b, value):
      if not b in self.blocks:
         self.blocks[b] = Block()

      self.blocks[b].set_clear(value)

   def is_clear(self, b):
      pass

   def on(self, b, x):
      if not b in self.blocks:
         self.blocks[b] = Block()

      self.blocks[b].set_on(x)

   def actions(self):
      # what actions can I do?
      # I can move a clear block to another clear block
      # I can move a clear block to the table 
      solution = []
      for block_name in self.blocks:
         block = self.blocks[block_name]
         print("block: " + str(block_name))
         print("clear?: " + str(block.is_clear()))
         print("on?: " + str(block.is_on("table")))
         if block.is_clear():
            if not(block.is_on("table")):
               solution.append("MoveToTable " + block_name + " " + block.on)
   
            for block_name2 in self.blocks:
               if (block_name == block_name2):
                 continue
 
               block2 = self.blocks[block_name2]
               if (block2.is_clear()):
                  solution.append("Move " + block_name + " " + block.on + " " + block_name2)


      return solution
       

# stuff from book
# Move(b, x, y)
# pre: on(b, x) , clear(b) , clear(y), block(b), block(y), (b != x), (b != y), (x != y)
# post: on(b, y), clear(x), !on(b, x), !clear(y)

# MoveToTable(b, x)
# pre: on(b, x), clear(b), block(b), block(x)
# post: On(b, Table), clear(x) , !On(b, x)

def ParseInput(filename):
   with open(filename) as f:
      lines = f.readlines()
   f.close()

   Init = State()
   Goal = State()
   Current = None

   for line in [x.strip().lower() for x in lines]: 
      if (line.startswith("#")):
         continue
      elif (line.startswith('init')):
         Current = Init
      elif (line.startswith('goal')):
         Current = Goal
      else:
         params = line.split(" ")
         if (params[0] == "clear"):
            Current.clear(params[1], True)
         elif (params[0] == "on"):
            Current.on(params[1], params[2])
            if (params[2] != "table"):
               Current.clear(params[2], False)
         else:
            # unknown instruction, skip line
            pass 

   return (Init, Goal)

# steps 
# 1. read in input file
(Init, Goal) = ParseInput("blocks1.txt")
print("Init: " + str(Init.blocks))
print("Goal: " + str(Goal.blocks))
# 2. see if I can get valid moves from state
print(Init.actions())
# 3. see if moves I make have the correct effect on state
# 4, state-space search

# simplest solution is to backtrack from goal 
# enumerating over all possible moves for each state
# and arriving at the best solution when a backtracked
# state is equivalent to the start state
