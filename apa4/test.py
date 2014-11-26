#!/usr/bin/python3

import Forrester
import SimplePlayers
import roundRobin
import tournament

players = [
           Forrester.Forrester4,
           SimplePlayers.Defect,
           SimplePlayers.Cooperate,
           SimplePlayers.Ten,
           SimplePlayers.Twenty,
           SimplePlayers.Thirty,
           SimplePlayers.Forty,
           SimplePlayers.Fifty,
           SimplePlayers.Sixty,
           SimplePlayers.Seventy,
           SimplePlayers.Eighty,
           SimplePlayers.Ninety,
           SimplePlayers.Bad,
          ]

#roundRobin.roundRobin(players, 1000, 0.2, 0.001)
roundRobin.tournament(players, 1000, 0.0, 0.001)
