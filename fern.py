import matplotlib.pyplot as plt
from random import random

w = 300
e1 = 0.5 * w
e2 = 0.57 * w
e3 = 0.408 * w
e4 = 0.1075 * w
f1 = 0 * w
f2 = -0.036 * w
f3 = 0.0893 * w
f4 = 0.27 * w

imax = int(input("Enter the number of iterations (max 50000 : "))

if imax > 50000: imax = 50000

x = e1
y = 0.0
X = [x]
Y = [y]

for i in range(1, imax+1):
	r = random()
	if r <= 0.02:
		xn = 0*x + 0*y + e1; yn = 0*x + 0.27*y + f1
	elif (r > 0.02 and r <= 0.17):
		xn = -0.139*x + 0.263*y + e2; yn = 0.246*x + 0.224*y + f2
	elif (r > 0.17 and r <= 0.3):
		xn = 0.17*x - 0.215*y + e3; yn = 0.222*x + 0.176*y + f3
	else:
		xn = 0.781*x + 0.034*y + e4; yn = -0.032*x + 0.739*y + f4
	X.append(xn)
	Y.append(yn)
	x = xn
	y = yn

plt.plot(X, Y, 'r.')
# plt.savefig('fern.png')  # To save the plot.
plt.show()
