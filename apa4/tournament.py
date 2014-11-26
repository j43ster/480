#!/usr/bin/python3

import roundRobin

def tournament(agentDB, matchTurns=1000, F=0.5, I=0.001, verbose=0):

   result = []

   currentPlayers = agentDB
   while len(currentPlayers):
      roundResult = roundRobin.roundRobin(currentPlayers, matchTurns, F, I, verbose)
      
      result = [roundResult[-1]] + result

      currentPlayers, roundScores = zip(*roundResult)
      currentPlayers = currentPlayers[0:-1]

   for i, player in enumerate(result):
      print(str(i+1) + ": " + str(player[0](0, 0, True)))
