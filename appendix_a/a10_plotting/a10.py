# A.10 PLOTTINGo

# from random import *
# from math import *
# from matplotlib.pyplot import *
# from numpy import *

# def pdf(x,a,b,c):
#     if x < a:
#         return 0
#     elif x >= a and x < c:
#         return (2*(x-a) / ((b-a) * (c-a)))

#     elif x == c:
#         return 2 / (b-a)
#     elif x > c and x <= b:
#         return 0
#     elif x > b:
#         return 0
#     else:
#         print("Error")


# a=1
# b=10
# c=7

# X =arange(0, b+1, 0.1)
# Y= []

# xlabel("X", fontsize = 15)
# ylabel("f(x)", fontsize=15)

# gca().axes.get_xaxis().set_ticks(arange(0, b+1, 1.0))

# for x in X:
#     Y.append(pdf(x,a,b,c))

# plot(X,Y,linewidth=2)

# # Show figure on screen
# show()

# # Save figure to hard disk
# savefig("triangular_pdf.pdf",format="pdf",bbox_inches="tight")



# # A.10.2
# # Code for generating Figure 10.6(a)
# from random import *
# from math import *
# from matplotlib.pyplot import *
# from numpy import *

# def pdf(x):
#     k=10
#     theta = 1.0
#     return (x**(k-1) * theta**k * exp(-1 * theta * x))
#     factorial(k-1)
# X = arange(0, 50, 0.1)
# Y = []

# for x in X:
#     Y.append(pdf(x))

# xlabel("Y")
# ylabel("P(y)")


# # Hide numbers along y-axis
# gca().axes.get_yaxis().set_ticklabels([])

# #Remove ticks along y-axis
# gca().axes.yaxis.set_tick_params(width=0)

# plot(X, Y, linewidth=2)
# savefig("erlang_plot_pdf.pdf", format="pdf",bbox_inches="tight")

# # Compute the mean
# mean = 0
# for i in range(len(X)):
#     mean = mean + X[i] * Y[i]

# print("Mean = ",mean)


# A.10.3
# Code for generating Figure 10.6(b)
from random import *
from math import *
from matplotlib.pyplot import *
from statistics import *

def Erlang():
    k = 10
    theta = 1.0
    y = 0
    for i in range(k) :
        u = random()
        x = (-1 /theta) * log(u) # Exponetial variate
        y += x
    return y

N = 10000
v = []
for i in range(N) : 
    v.append(Erlang())

bins = 100

w = [1/len(v)] * len(v)

hist(v, bins, weights = w)

xlabel("Y")
ylabel("P(y)")

# Hide numbers along y-axis
gca().axes.get_yaxis().set_ticklabels([])
# Remove ticks along y-axis
gca().axes.get_yaxis().set_tick_params(width=0)

savefig("erlan_plot_hist.pdf", format="pdf", bbox_inches="tight")

print("Mean = ",mean(v))
