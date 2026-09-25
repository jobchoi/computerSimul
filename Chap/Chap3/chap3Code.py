from random import randint, choice
from statistics import mean

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
    if coutcome == 'Head' :
        observed.append(1)
    else observed.append(0)

print("Prob = ", round(mean(observed),2))