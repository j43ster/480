#!/usr/bin/python3

import random

payoffMatrix = [[('C','C'), (3,3)], [('C','D'), (0,5)], [('D','C'), (5,0)],[('D','D'), (1,1)]]

#evalMoves
def evalMoves(AMove,BMove):
   m1,m2 = AMove.upper(),BMove.upper()
   for moves, scores in payoffMatrix:
      if (m1,m2) == moves:
         return scores

def swapMove(move, F):
   if random.random() < F:
      if move == 'C':
         return 'D'
      else:
         return 'C'
   else:
      return move

#playMatch
def playMatch(player1, player2, matchTurns, F, I, verbose):
   score1 = [0, 0] # [p1, p2]
   score2 = [0, 0] # [p2, p1]
   history1 = [] # [[d1, d2]]
   history2 = [] # [[d2, d1]]
   for i in range(matchTurns):
      d1 = swapMove(player1(history1, score1), F)
      d2 = swapMove(player2(history2, score2), F)
      history1.append([d1, d2])
      history2.append([d2, d1])
      score1[0] += evalMoves(d1, d2)[0]
      score1[1] += evalMoves(d1, d2)[1]
      score2[0] += evalMoves(d2, d1)[0]
      score2[1] += evalMoves(d2, d1)[1]
      F -= I
      if (F < 0):
         F = 0
   return score1

#roundRobin
def roundRobin(agentDB, matchTurns=1000, F=0.5, I=0.001, verbose=0):
   scores = []
   for i in range(len(agentDB)):
      scores.append(0)
      scores[i] = 0

   # for a round robin have each player play each other once
   for idx1, player1 in enumerate(agentDB):
      for idx2, player2 in enumerate(agentDB[idx1+1:]):
         matchScore = playMatch(player1, player2, matchTurns, F, I, verbose)
         if (verbose):
            print("index 1 is: " + str(idx1) + ", index 2 is: " + str(idx1+idx2+1))
            print(str(player1(0, 0, True)) + " is playing " + str(player2(0, 0, True)))
            print("Match score: " + str(matchScore))
         scores[idx1] += matchScore[0]
         scores[idx1 + idx2 + 1] += matchScore[1] 

   sortedScores = sorted(zip(agentDB, scores),key=lambda x: x[1], reverse=True)

   print("Final Scores: ")
   for player in sortedScores:
      print(str(player[0](0, 0, True)) + ": " + str(player[1]))
