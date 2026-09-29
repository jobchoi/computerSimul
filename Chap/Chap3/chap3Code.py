from random import randint, choice
from statistics import mean
from numpy import cumsum
from numpy import arange
from matplotlib.pyplot import *


# # 3.1 Simulating the experiment of throwing a die. The output is shown as a comment on each line

# print(randint(1,6)) # outcome =?
# print(randint(1,6)) # outcome =?
# print(randint(1,6)) # outcome =?

# # 3.2 Approximating the probability of an outcome in the experiment of throwing a die.

# n = 1000000
# ne = 0

# for i in range(n):
#     outcome = randint(1,6)

#     if(outcome == 3) :      # Check for event of interst
#         ne += 1             # ne = ne + 1

# print("Prob = ",round(ne/ n ,4)) # = 0.1667


# 3.3 
# Simulation program for studying the running mean of the random experiment of tossing a coin. This program is also used to generate Figure 3.4.
n = 1000
observed = []

for i in range(n) :
    outcome = choice(['Head','Tail'])
    if outcome == 'Head' :
        observed.append(1)
    else :
        observed.append(0)

print("Prob = ", round(mean(observed),2))


## Part 2 : Computing the moving average

cum_observed = cumsum(observed)
moving_avg = []

for i in range(len(cum_observed)):
    moving_avg.append(cum_observed[i]/(i+1))

### Part 3 : Making the plot 

x = arange(0, len(moving_avg),1)            # x-axis
p = [0.5 for i in range(len(moving_avg))]   # Line

xlabel('Iterations',size = 20)
ylabel('Probability',size = 20)

plot(x,moving_avg)
plot(x,p, linewidth=2, color='black')

show()