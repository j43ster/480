#!/usr/bin/python3

import Forrester
import SimplePlayers
import roundRobin

players = [Forrester.Forrester,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
           SimplePlayers.Defect,
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
           SimplePlayers.Ninety]

roundRobin.roundRobin(players, 1000, 0.2, 0.001)
