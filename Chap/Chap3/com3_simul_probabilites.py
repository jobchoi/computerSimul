from random import randint
from random import choice
from numpy import cumsum
from numpy import arange
from statistics import mean
from matplotlib.pyplot import *
import matplotlib
matplotlib.use('Agg') # GUI 백엔드 우회, 백그라운드에서 이미지만 생성



# 3.1
print("=========> 3.1")
print(randint(1,6)) # outcome = 1
print(randint(1,6)) # outcome = 3
print(randint(1,6)) # outcome = 5

print("=========> 3.2")
n = 1000000
ne = 0

for i in range(n):
    outcome = randint(1,6)
    if(outcome == 3):
        ne+=1

print("Prob = ", round(ne/n,4)) # = 0.1667

print("=========> 3.3")

## Part1 : Performing the  simulation experiment
print("Part 1 : Performing the  simulation experiment")
n = 1000
observed = []

for i in range(n):
    outcome = choice(['Head','Tail'])
    if outcome == 'Head':
        observed.append(1)
    else:
        observed.append(0)

print("Prob = ",round(mean(observed),2))

## Part 2 : Computing the moivg average
print("Part 2 : Computing the moivg average")

cum_observed = cumsum(observed)
moving_avg = []

for i in range(len(cum_observed)):
    moving_avg.append(cum_observed[i] /(i+1))

## Part 3 : Making the plot
x = arange(0, len(moving_avg),1) # x-axis
p = [0.5 for i in range(len(moving_avg))] # Line

xlabel('Interations', size=20)
ylabel('Probability', size=20)

plot(x, moving_avg)
plot(x, p, linewidth=2, color='black')

# show()
savefig('moving_avg_result.png') # 창을 띄우는 대신 폴덜에 이미지 파일로 저장