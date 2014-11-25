#!/usr/bin/python3

import copy
import sys

# description words
INIT = 'INIT'
GOAL = 'GOAL'
CLEAR = 'CLEAR'
ON = 'ON'
TABLE = 'Table'

# action names
MOVE = 'Move'
MOVE_TO_TABLE = 'MoveToTable'

class Block():
   def __init__(self):
      self.clear = "?"
      self.on = "?"

   def __eq__(self, other):
      return (self.on == other.on and self.clear == other.clear)

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
      return str("{ Block: on = '" + str(self.on) + "', clear = '" + str(self.clear) + "' }")

   def __repr__(self):
      return str("{ Block: on = '" + str(self.on) + "', clear = '" + str(self.clear) + "' }")

class State():
   def __init__(self):
      self.blocks = {}

   def __eq__(self, other):
      return self.blocks == other.blocks

   def clear(self, b, value):
      if (b == TABLE):
         return

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
         if block.is_clear():
            if not(block.is_on(TABLE)):
               solution.append(MOVE_TO_TABLE + " " + block_name + " " + block.on)
   
            for block_name2 in self.blocks:
               if (block_name == block_name2):
                 continue
 
               block2 = self.blocks[block_name2]
               if (block2.is_clear()):
                  solution.append(MOVE + " " + block_name + " " + block.on + " " + block_name2)


      return solution

   # move block b from block x to the table
   def moveToTable(self, b, x):
      new_state = copy.deepcopy(self)
 
      # not checking to make sure this is a valid move
      new_state.on(b, TABLE)
      new_state.clear(x, True)

      return new_state

   # move block b from block x to block y
   def move(self, b, x, y):
      new_state = copy.deepcopy(self)

      # not checking to make sure this is a valid move
      new_state.on(b, y)
      new_state.clear(y, False)
      new_state.clear(x, True)

      return new_state
       

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

   for line in [x.strip() for x in lines]: 
      if (line.startswith("#")):
         continue
      elif (line.startswith(INIT)):
         Current = Init
      elif (line.startswith(GOAL)):
         Current = Goal
      else:
         params = line.split(" ")
         if (params[0] == CLEAR):
            Current.clear(params[1], True)
         elif (params[0] == ON):
            Current.on(params[1], params[2])
            if (params[2] != TABLE):
               Current.clear(params[2], False)
         else:
            # unknown instruction, skip line
            pass 

   return (Init, Goal)

def FindSolution(initial, goal, reverse):
   # paths = [(depth, state, path = [])]

   start = initial
   finish = goal

   if (reverse):
      start = goal
      finish = initial

   paths = [(0, start, [])] 
   result = None
   solution = False

   iterations = 0

   while (not(solution)):
      iterations = iterations + 1
      # sort paths to priority queue based on depth

      # pull shortest path from paths
      (depth, state, path) = paths[0]

      # remove current from paths
      paths = paths[1:]

      # execute actions from current
      for action in state.actions():
         parts = action.split(" ")

         if (parts[0] == MOVE):
            result = state.move(parts[1], parts[2], parts[3])
         elif (parts[0] == MOVE_TO_TABLE):
            result = state.moveToTable(parts[1], parts[2])

         paths.append((depth+1, result, path + [action]))
         if (result == finish):
            return paths[-1]

def reverse_path(path):
   path = path[::-1] 
   new_path = []

   for action in path:
      part = action.split(" ")
      if (part[0] == MOVE):
         if (part[2] == TABLE):
            new_path.append(MOVE_TO_TABLE + "(" + part[1] + ", " + part[3] + ")")
         else:
            new_path.append(MOVE + "(" + part[1] + ", " + part[3] + ", " + part[2] + ")")
      elif (part[0] == MOVE_TO_TABLE):
         new_path.append(MOVE + "(" + part[1] + ", " + TABLE + ", " + part[2] + ")")

   return new_path
            
# steps 
# 1. read in input file
infile = None
if len(sys.argv) > 1:
   infile = sys.argv[1]
else:
   print("No input file provided, exiting.")
   exit()

(Init, Goal) = ParseInput(infile)
# 2. see if I can get valid moves from state
#current = Init 
#actions = current.actions()
#print("actions: " + str(actions))
# 3. see if moves I make have the correct effect on state

#for action in actions:
#   parts = action.split(" ")
#
#   print()
#   print(action)
#   
#   if (parts[0] == MOVE):
#      print(str(current.blocks))
#      result = current.move(parts[1], parts[2], parts[3])
#      print(str(result.blocks))
#   elif (parts[0] == MOVE_TO_TABLE):
#      print(str(current.blocks))
#      result = current.moveToTable(parts[1], parts[2])
#      print(str(result.blocks))

# 4, state-space search

# simplest solution is to backtrack from goal 
# enumerating over all possible moves for each state
# and arriving at the best solution when a backtracked
# state is equivalent to the start state

reverse = True
(moves, state, path) = FindSolution(Init, Goal, reverse)

if reverse:
   path = reverse_path(path)

for step in path:
   print(step)










#




