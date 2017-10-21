#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-15 15:15:37
# @Author  : jingray (lionel_jing@163.com)
# @Link    : http://www.jianshu.com/u/01fb0364467d
# @Version : $Id$

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

def plot_uniform(x_minimum, x_maximum, tick_interval):

    x = range(x_minimum, x_maximum + 1)

    # TODO: Using x_maximum and x_minimum, calculate the height of the
    # rectangle that represents the uniform probability distribution
    # Recall that the rectangle area should be 1 for a uniform continuous
    # distribution
    y = 1/(x_maximum - x_minimum)

    plt.bar(x_minimum, y, bottom=0, width= (x_maximum - x_minimum), align='edge', alpha=0.5)
    plt.xlabel('Degrees')
    plt.ylabel('Probability Distribution')
    plt.title('Uniform Probability Distribution \n for a Spinning Bottle')
    plt.xticks(np.arange(min(x), max(x)+1, tick_interval))
    plt.ylim(0, .3)
    plt.show()

plot_uniform(5, 10, 1)


import matplotlib.pyplot as plt
import numpy as np

def bar_heights(intervals, probabilities, total_probability):

    heights = []

    # normalize probability intervals
    total_relative_prob = sum(probabilities)  # calculate the sum of a list very concise!!!

    for i in range(0, len(probabilities)):

        bar_area = probabilities[i]*total_probability/total_relative_prob

        heights.append(bar_area/(intervals[i+1]-intervals[i]))

    return heights

def plot_discrete(intervals, probabilities, total_probability):
    heights = bar_heights(intervals, probabilities, total_probability)
    freqs = np.array(heights)
    bins = np.array(hour_intervals)
    widths = bins[1:] - bins[:-1] #calculate the time interval widths, very good!!!
    freqs = freqs.astype(np.float)

    tick_interval = 1
    plt.bar(bins[:-1], freqs, width=widths, align='edge', edgecolor='black', alpha=0.5)
    plt.xlabel('Interval')
    plt.ylabel('Probability Distribution')
    plt.title('Probability Distribution')
    plt.xticks(np.arange(min(bins), max(bins)+1, tick_interval))

    plt.show()

hour_intervals = [0, 5, 10, 16, 21, 24]
probability_intervals = [1, 5, 3, 6, 1/2]
accident_probability = 0.05
plot_discrete(hour_intervals,probability_intervals,accident_probability)


# Robot World 1-D
import matplotlib.pyplot as plt
import numpy as np

def initialize_robot(grid_size):

    #grid = [1/grid_size for i in range(0,grid_size)]
    grid = [1/grid_size] * grid_size
    return grid

def grid_probability(grid, position):
    try:
        return grid[position]
    except:
        return None
def output_map(grid):

    x_labels = range(len(grid))
    #x_data = np.array(x_labels)
    #y_data = np.array(grid)

    #plt.bar(x_data, y_data, width=0.7, edgecolor='black')
    plt.bar(x_labels, height=grid, width=0.7, edgecolor='black')
    plt.xlabel('Grid Space')
    plt.ylabel('Probability')
    plt.title('Probability of the robot being at each space on the grid')
    plt.xticks(np.arange(min(x_labels), max(x_labels)+1, 1))
    plt.show()
def update_probabilities(grid, updates):
    #for i in range(len(updates)):
       # grid[updates[i][0]]=updates[i][1]
    for update in updates:
        grid[update[0]] = update[1]
    return grid
print(update_probabilities([0.2, 0.2, 0.2, 0.2, 0.2], [[0, .25], [4, 0.15]]))

#2-D Self-Driving Car World

import matplotlib.pyplot as plt
from pandas import DataFrame

class SelfDrivingCar():
    def __init__(self, rows, columns):
        self.grid = []
        self.grid_size = [rows,columuns]
        self.num_elements = rows * columns

    def initialize_grid(self):
        probability = 1/self.num_elements
        for i in range(self.grid_size[0]):
            list = []
            for j in range(self.grid_size[1]):
                list.append(probability)
            self.grid.append(list)
        return self.grid

    def output_probability(self, grid_point):

        try:
            return self.grid[grid_point[0]][grid_point[1]]
        else:
            return None

    def update_probability(self, update_list):
        for update in update_list:
            self.grid[update[0]][update[1]]=update[2]
        return self.grid

    def visualize_probability(self):

        if not self.grid:
            self.grid = [[0],[0]]
        else:
            plt.imshow(self.grid, cmap='Greys', clim=(0,.1))
            plt.title('Heat Map of Grid Probabilities')
            plt.xlabel('grid x axis')
            plt.ylabel('grid y axis')
            plt.show()
car = SelfDrivingCar(5,4)

car.initialize_grid()

# should output 0.05
print(car.output_probability([2,3]))

# should output 0.05
print(car.output_probability([1,2]))

car.update_probability([[2,3,.2], [1,2,.1]])

# should output 0.2
print(car.output_probability([2,3]))

# should output 0.1
print(car.output_probability([1,2]))

# should output a heat map
car.visualize_probability()

#Central Limit Theorem
#normal distribution, also called a Gaussian distribution.
#The normal distribution appears throughout self-driving car applications
#especially with sensor measurements and tracking objects that move around the vehicle.
# import libraries used in the notebook
%matplotlib inline

import numpy as np
from scipy import stats
from matplotlib import mlab
import matplotlib.pyplot as plt

# Set figure height and width
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size

x = np.linspace(-12, 12, 100)
plt.title('Normal distribution \n mean = 0 \n standard deviation = ' + str(3))
plt.xlabel('value')
plt.ylabel('distribution')
plt.plot(x,mlab.normpdf(x, 0, 3))



###Probability Distributions###
x = np.linspace(-12, 12, 100)

plt.subplot(221)
plt.plot(x,mlab.normpdf(x, 0, 3))
plt.title('Normal Distribution')

plt.subplot(222)
plt.plot(x,stats.uniform.pdf(x,-5,10))
plt.title('Uniform Distribution')

plt.subplot(223)
plt.plot(x[x > -1],stats.chi2.pdf(x[x>-1],3))
plt.title('Chi2 Distribution')

plt.subplot(224)
plt.plot(x[x > -1],stats.lognorm.pdf(x[x > -1],3))
plt.title('Logarithmic Distribution')

plt.subplots_adjust(hspace=.5)

###different probability distributions still work with the central limit theorem
#
### Probability distributions

def random_uniform(low_value, high_value, num_samples):
    return np.random.uniform(low_value, high_value, num_samples)

### Poisson Distribution
def poisson_distribution(expectation, num_samples):
    return np.random.poisson(expectation, num_samples)

def binomial_distribution(result, probability, trials):
    return np.random.binomial(result, probability, trials)

uniform = random_uniform(1, 5, 100000)
poisson = poisson_distribution(6.0, 10000)
binomial = binomial_distribution(1, 0.5, 10000)


### Shows Central Limit Theorem: takes samples from a distribution and calculates the mean of each sample.
#
# variables:
# distribution => array containing values from a population
# iterations => number of times to draw samples and calculate the mean of the sample
# num_samples => sample size
# num_bins => controls number of bins in the histograms3
#
# outputs:
# (1) summary statistics of the population and the means of the samples
# (2) histogram of the population and means of the samples
# (3) normalized histogram of the means and line chart of equivalent normal distribution with same mean and stdeviation
# (4) probability plot of the original distribution and the means of the samples
#
###

def sample_means_calculator(distribution, iterations, num_samples, num_bins):

    # take samples from the distribution and calculate the mean of each sample
    sample_means = []

    # iterate through picking samples and calculating the mean of each sample
    for iteration in range(iterations):

        samples = []

        # iterate through for the sample size chosen and randomly pick samples
        for sample in range(num_samples):
            samples.append(distribution[np.random.randint(1,len(distribution))])

        # calculate the mean of the sample
        sample_means.append(np.mean(samples))


    # Calculate summary statistics for the population and the sample means
    population_mean = np.average(distribution)
    population_median = np.median(distribution)
    population_deviation = np.std(distribution)

    sample_mean = np.mean(sample_means)
    sample_median = np.median(sample_means)
    sample_deviation = np.std(sample_means)

    print('population mean ', population_mean, ' \n population median ', population_median, '\n population standard deviation ', population_deviation)
    print('\n mean of sample means ', sample_mean, '\n median of sample means ', sample_median, '\n standard deviation of sample means ', sample_deviation)

    # histogram of the population and histogram of sample means
    fig = plt.figure(figsize=(8, 4))

    ax1 = plt.subplot(121)
    plt.hist(distribution, bins=num_bins)
    plt.title('Histogram of the Population')
    plt.xlabel('Value')
    plt.ylabel('Count')

    ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
    plt.hist(sample_means, bins=num_bins)
    plt.title('Histogram of the Sample Means')
    plt.xlabel('Value')
    plt.ylabel('Count')

    plt.show()

    # normalized histogram of the sample means and an equivalent normal distribution with same mean and standard deviation
    fig = plt.figure(figsize=(8, 3))

    plt.hist(sample_means, bins=num_bins, normed=True)
    plt.title('Normalized Histogram of Sample Means and \n Equivalent Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Count')

    x = np.linspace(min(sample_means), max(sample_means), 1000)
    plt.plot(x,mlab.normpdf(x, sample_mean, sample_deviation))

    plt.show()

    # probability plots showing how the sample mean distribution is more normal than the population mean
    fig = plt.figure(figsize=(8, 3))

    ax5 = plt.subplot(121)
    stats.probplot(probability_distribution, plot=plt)
    ax6 = plt.subplot(122)
    stats.probplot(sample_means, plot=plt)

    ax5.set_title('Probability Plot of the Population')
    ax6.set_title('Probability Plot of the Sample Means')

    plt.show()

    ### Take samples and calculate the sample means for central limit theorem
sample_means_calculator(uniform, 100000, 50, 100)
sample_means_calculator(random_uniform(1,10,100000), 10000, 50, 100)
sample_means_calculator(poisson_distribution(6.0,500000), 10000, 90, 100)
sample_means_calculator(binomial_distribution(1, 0.5, 10000), 10000, 200, 100)
