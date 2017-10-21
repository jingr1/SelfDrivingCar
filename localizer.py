#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-21 22:37:30
# @Author  : jingray (lionel_jing@163.com)
# @Link    : http://www.jianshu.com/u/01fb0364467d
# @Version : $Id$

#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    height = len(beliefs)
    width = len(beliefs[0])
    new_beliefs = [[0.0 for i in range(width)] for j in range(height)]

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            hit = (grid[i][j]==color)
            new_beliefs[i][j] = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
    sums = 0
    for row in new_beliefs:
        sums = sums + sum(row)
    for i, row in enumerate(new_beliefs):
        for j, cell in enumerate(row):
            new_beliefs[i][j] = new_beliefs[i][j]/sums

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
