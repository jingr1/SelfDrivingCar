#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 20:54:56
# @Author  : jingray (lionel_jing@163.com)
# @Link    : http://www.jianshu.com/u/01fb0364467d
# @Version : $Id$

import random as rd

# Coin flips
def simulate_coin_flips(num_trials):
    heads = 0
    tails = 0
    p_heads = 0.5
    for i in range(num_trials):
        random_number = rd.random()
        if random_number < p_heads:
            heads = heads + 1
        else:
            tails += 1
    percent_heads = heads / num_trials
    return percent_heads

percentage = simulate_coin_flips(2000000) # calling the function
print(percentage)


# Simulating Probabilities

def simulate_dice_rolls(N):
    roll_counts = [0,0,0,0,0,0]
    for i in range(N):
        roll = rd.choice([1,2,3,4,5,6])
        index = roll - 1
        roll_counts[index] = roll_counts[index] + 1
    return roll_counts

def show_roll_data(roll_counts):
    number_of_sides_on_die = len(roll_counts)
    for i in range(number_of_sides_on_die):
        number_of_rolls = roll_counts[i]
        number_on_die = i+1
        print(number_on_die, "came up", number_of_rolls, "times")

roll_data = simulate_dice_rolls(60000)
show_roll_data(roll_data)


from matplotlib import pyplot as plt

def visualize_one_die(roll_data):
    roll_outcomes = [1,2,3,4,5,6]
    fig, ax = plt.subplots()
    ax.bar(roll_outcomes, roll_data)
    ax.set_xlabel("Value on Die")
    ax.set_ylabel("# rolls")
    ax.set_title("Simulated Counts of Rolls")
    plt.show()

roll_data = simulate_dice_rolls(500)
visualize_one_die(roll_data)


# Calculating Probabilities for Bayes' rule

# The complement P(~A) function takes in the probability of an event P(A).
def complement(p_A):
    complement = 1 - p_A
    return complement

# Test code - do not change
import solution

test_value = 0.4265

# This line calls your function and stores the output
comp = complement(test_value)
correct_comp = solution.complement(test_value)

# Assertion, comparison test
try:
    assert(comp == correct_comp)
    print('That\'s right!')
except:
    print ('Your code returned that the complement is: ' +str(comp)
           + ', which does not match the correct value: ' +str(correct_comp))


# Test 2
comp2 = complement(solution.test_value)
correct_comp2 = solution.complement(solution.test_value)

# Assertion, comparison test
try:
    assert(comp2 == correct_comp2)
    print('That\'s right!')
except:
    print ('For test 2, your code returned that the complement is: ' +str(comp2)
           + ', which does not match the correct value.')


## Complete this joint function
def joint(p_A, p_B):

    ## calculates the joint probability of
    ## any variables p_A, p_B, WHEN THOSE PROBABILITIES
    ## ARE INDEPENDENT (this code wouldn't work
    ## for probabilities that depend on each other).
    joint = p_A * p_B

    return joint

# Test values
test_A = 0.15
test_B = 0.42

# This line calls your function and stores the output
j = joint(test_A, test_B)
correct_j = solution.joint(test_A, test_B)

# Assertion, comparison test
try:
    assert(j == correct_j)
    print('That\'s right!')
except:
    print ('Your code returned that the joint probability is: ' +str(j)
           + ', which does not match the correct value.')


# The inputs to total probability are given descriptive names

def total_probability(p_disease, p_pos_given_disease, p_pos_given_no_disease):

    ## calculates the total probability of a positive test result
    ## You may use other variable in this function as well as long
    ## as total is correct
    total = p_disease * p_pos_given_disease + (1 - p_disease) * p_pos_given_no_disease

    return total

# Test code - do not change
import solution

p_disease = 0.1
p_pos_given_disease= 0.9
p_pos_given_no_disease= 0.2

# This line calls your function and stores the output
total = total_probability(p_disease, p_pos_given_disease, p_pos_given_no_disease)
correct_total = solution.total_probability(p_disease, p_pos_given_disease, p_pos_given_no_disease)

# Assertion, comparison test
try:
    assert(total == correct_total)
    print('That\'s right!')
except:
    print ('Your code returned that the total probability is: ' +str(total)
           + ', which does not match the correct value.')


# Given three input probabilities, complete this function
# so that it returns the posterior probability

def bayes(p_A, p_B_given_A, p_notB_given_notA):

    ## TODO: Calculate the posterior probability
    ## and change this value
    p_notA = 1-p_A
    p_B_given_notA = 1-p_notB_given_notA
    p_B = p_A*p_B_given_A + p_notA*p_B_given_notA
    posterior = p_A*p_B_given_A/p_B

    return posterior

# Test code - do not change
import solution

test_p_A = 0.4
test_p_B_given_A = 0.7
test_p_notB_given_notA = 0.9

# This line calls your function and stores the output
posterior = bayes(test_p_A, test_p_B_given_A, test_p_notB_given_notA)
correct_posterior = solution.bayes(test_p_A, test_p_B_given_A, test_p_notB_given_notA)

# Assertion, comparison test
try:

    assert(abs(posterior - correct_posterior) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the posterior is: ' +str(posterior)
           + ', which does not match the correct value.')

# 2D Array
import numpy as np

# A simple robot world can be defined by a 2D array
# Here is a 5x6 world
world = np.array([ [0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0] ])

# Visualize the world
print(world)
# Print out some information about the world

print('The shape of this array is: ' + str(world.shape))
print('Notice that the x and y dimensions are in the opposite order than usual!')
print('It\'s height is: ' + str(world.shape[1]) +
      ', and it\'s length/width is: ' + str(world.shape[0]))

      # Access a location and read its value
value = world[3][0]
print('\n')
print('Value at index [3, 0] = ' +str(value))

# Read the first three items in the 3rd row
row = 2
column_index = 0
value_left = world[row, column_index]
value_middle = world[row, column_index + 1]
value_right = world[row, column_index + 2]

print('\nThe first three values in row 2 : ' +str(value_left)+', '
                                              +str(value_middle) +', '
                                              +str(value_right) )

# Compare the first two values and print the result
compare = world[0][0] == world[0][1]
print('\nDo the first two values match? ' + str(compare))

# Define a function to plant a tree
# and change the value of the array in that location
def plant_tree(y, x):
    # check that the indices are in the boundaries of the array dimensions
    if(y < world.shape[0] and x < world.shape[1]):
        world[y,x] = 1
        print('\n' + str(world)) # prints a newline and the current world

# Call the function at the location x = 3, and y = 2
# You can call this multiple times in a row
plant_tree(0, 2)

# This function uses nested for loops and knowledge
# about the shape of the array to print out each item with it's index
def iterate2D(world):
    # y-dimension (rows)
    for i in range(0, world.shape[0]):
        # x-dimension (columns)
        for j in range(0, world.shape[1]):
            print('Index ['+str(i)+']['+str(j)+'] = ' +str(world[i][j]))

# Call the iterate function
print('\n')
iterate2D(world)

# This function is similar to our iterate2D function,
# But looks for the first tree in the array and prints its location [x][y]
def first_tree(world):
    # iterates through all indices starting at the top-left [0][0]
    for i in range(0, world.shape[0]):
        for j in range(0, world.shape[1]):
            # check if a tree is found
            if(world[i][j] == 1):
                # if so, print the index and leave the loop with a return statement
                print('First tree found at location: ['+str(i)+']['+str(j)+']')
                return


# Call the first_tree function
print('\n')
first_tree(world)


import numpy as np

# A 5x4 robot world of characters 'o' and 'b'
world = np.array([ ['o', 'b', 'o', 'o', 'b'],
                   ['o', 'o', 'b', 'o', 'o'],
                   ['b', 'o', 'o', 'b', 'o'],
                   ['b', 'o', 'o', 'o', 'o'] ])

# Sensor measurement
measurement = ['b', 'o']

# This function takes in the world and the sensor measurement.
# Complete this function so that it returns the indices of the
# likely robot locations, based on matching the measurement
# with the color patterns in the world

def find_match(world, measurement):
    # Empty possible_locations list
    possible_locations = []

    ## TODO: Iterate through the world
    ## Look at two adjacent indices at a time - the square the robot is
    ## on top of and the square to its right
    ## (Making sure not to go past the bounds of the world)
    for i in range(0,world.shape[0]):
        for j in range(0,world.shape[1]):
            if j<world.shape[1]-1 and [world[i][j],world[i][j+1]] == measurement:
                possible_locations.append([i,j])
    ## TODO: If two adjacent colors in the world match
    ## the two colors in the sensor measurement
    ## Add those indices to the possible_locations list
    ## Append them in the format [row_index, column_index], i.e. [0, 0]

    return possible_locations


# This line runs the function and stores the output - do not delete
locations = find_match(world, measurement)



# In numpy, this is easy to print COLUMN 0?

import numpy as np

np_grid = np.array([
    [0, 1, 5],
    [1, 2, 6],
    [2, 3, 7],
    [3, 4, 8]
])

# The ':' usually means "*all values*
print(np_grid[:,0])

# What if you wanted to change the size of the array?

# For example, we can turn the 2D grid from above into a 1D array
# Here, the -1 means fit all values into the length of this array
np_1D = np.resize(np_grid, (1, -1))

print(np_1D)


# We can also create a 2D array of zeros or ones
# which is useful for car world creation and analysis

# Create a 5x4 array
zero_grid = np.zeros((5, 4))

print(zero_grid)
