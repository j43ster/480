#!/usr/bin/python3

from Forrester import *
import SimplePlayers
import roundRobin
import tournament

players = [
#           Forrester4,
#           Forrester4,
#           Forrester4,
           Forrester4,
           Forrester4,
           SimplePlayers.TitForTat,
           SimplePlayers.TitForTat,
           SimplePlayers.TitForTat,
           SimplePlayers.TitForTat,
           SimplePlayers.TitForTat,
           SimplePlayers.TitForTat,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
#           SimplePlayers.Defect,
#           SimplePlayers.Defect,
           SimplePlayers.Fifty,
           SimplePlayers.Fifty,
           SimplePlayers.Cooperate,
          ]

roundRobin.tournament(players, 500, 0.38, 0.003)
#roundRobin.tournament(players, 1000, 0.0, 0.001)
