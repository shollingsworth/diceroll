#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import random

number_of_dice = 3
run_cycles = 100000
sides = 6
summary = {}

winnings_map = {
    0: -1,
    1: 1,
    2: 2,
    3: 3,
}

def getrun():
    retval = []
    for val in range(0,number_of_dice):
        retval.append(random.randint(1,6))
    return retval

def runcycle(run_cycles,bet_num):
    retval = []
    game_master_balance = player_balance = run_cycles
    number_set = {}
    while run_cycles:
        run = getrun()
        match_count = run.count(bet_num)
        win_res = winnings_map.get(match_count)
        if win_res < 0:
            player_balance += win_res
            game_master_balance += abs(win_res)
        else:
            game_master_balance += -win_res
            player_balance += win_res
        runstr = ':'.join([str(x) for x in run])
        retval.append([runstr,match_count,win_res,game_master_balance,player_balance])
        run_cycles += -1
    summary[bet_num] = [game_master_balance,player_balance]
    return retval

while sides:
    fn = "bet_on_number_" + str(sides).zfill(2) + '.csv'
    fh = open(fn, 'w')
    fh.write(','.join(['run set','number of matches','winning result','game master balance','player balance'])+"\n")
    cycles = runcycle(run_cycles,sides)
    for row in cycles:
        fh.write(','.join([str(x) for x in row])+"\n")
    sides += -1

fh = open("summary.csv", 'w')
fh.write("{},{},{}\n".format('bet on number','game master balance','player balance'))
for bet_num,arr in summary.items():
    gm = arr.pop(0)
    player = arr.pop(0)
    fh.write("{},{},{}\n".format(bet_num,gm,player))
