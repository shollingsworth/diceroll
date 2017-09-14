#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import __future__
import sys
import os
import random

number_of_runs = 10
run_cycles = 100000
number_of_dice = 3

def runcycle(run_cycles):
    number_set = {}
    while run_cycles:
        dice_roll = 0
        for  val in range(0,number_of_dice):
            roll = random.randint(1,6)
            dice_roll += roll
        if not number_set.get(dice_roll):
            number_set[dice_roll] = 0
        number_set[dice_roll] += 1
        run_cycles += -1
    return  number_set

while number_of_runs:
    fn = "run_number_" + str(number_of_runs).zfill(2) + ".csv"
    fh = open(fn,'w')
    for num,count in runcycle(run_cycles).items():
        fh.write("{},{}\n".format(num,count))
    fh.close()
    number_of_runs += -1
