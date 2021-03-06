#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: Friday December 17th of January 2020

Author: Daniel Cortild (https://github.com/DanielCortild)

TicTacToe Functions Module
Available Functions: train, compete, play
"""

import numpy as np
from modules.progress import progress
from modules.judger import Judger
from modules.players import AIPlayer, RandomPlayer, HumanPlayer, DLPlayer

def train ( P1, P2, saveP1='model1', saveP2='model2', epochs = 500 ):

    judger = Judger( P1, P2, learning = True )

    P1Win = 0.0
    P2Win = 0.0
    Draws = 0.0

    for i in range(epochs):

        winner = judger.play( show = False )

        if winner == 1:
            P1Win += 1
        if winner == -1:
            P2Win += 1
        if winner == 0:
            Draws += 1

        judger.reset()

        progress( count = i+1, total = epochs,
                 status1 = 'Game %s/%s' % ( str(i+1).zfill(int(np.ceil(np.log10(epochs+1)))), epochs),
                 status2 = 'P1Wins: %.2f, P2Wins: %.2f, Draws: %.2f' % (
                     P1Win/(i+1), P2Win/(i+1), Draws/(i+1) ) )

    print()
    P1.savePolicy(saveP1)
    P2.savePolicy(saveP2)

def compete ( P1, P2, epochs = 500, loadP1='model1', loadP2='model2' ):

    judger = Judger( P1, P2, learning = False )

    P1.loadPolicy(loadP1)
    P2.loadPolicy(loadP2)

    P1Win = 0.0
    P2Win = 0.0
    Draws = 0.0

    for i in range(epochs):

        winner = judger.play( show = False )

        if winner == 1:
            P1Win += 1
        if winner == -1:
            P2Win += 1
        if winner == 0:
            Draws += 1

        judger.reset()

        P1WinPercent, P2WinPercent, DrawsPercent = np.ceil( [100*P1Win/(i+1), 100*P2Win/(i+1), 100*Draws/(i+1)] ) / 100

        progress( count = i+1, total = epochs,
                 status1 = 'Game %s/%s' % ( str(i+1).zfill(int(np.ceil(np.log10(epochs+1)))), epochs),
                 status2 = 'P1Wins: %.2f, P2Wins: %.2f, Draws: %.2f' % (
                     P1WinPercent, P2WinPercent, DrawsPercent ) )
    print()

def play ( P1, P2, loadP1 = 'model1', loadP2 = 'model2' ):

    judger = Judger( P1, P2, learning = False )

    P1.loadPolicy(loadP1)
    P2.loadPolicy(loadP2)

    winner = judger.play( show = True )

    if winner == 1:
        print( "Player 1 (X) wins" )
    elif winner == -1:
        print( "Player 2 (O) wins" )
    else:
        print( "Tie!" )

    print()
