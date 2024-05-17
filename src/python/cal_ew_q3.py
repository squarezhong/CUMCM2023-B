import numpy as np
from sympy import symbols, Eq, solve

# alpha = 1.5 deg
length = 7408
width = 3704
center_depth = 110
alpha = 1.5*np.pi/180

# formula from question 1
c1 = 1/np.sin(np.pi/6 - alpha) * np.sin(np.pi/3) * np.cos(alpha)
c2 = 1/np.sin(np.pi/6 + alpha) * np.sin(np.pi/3) * np.cos(alpha)
c3 = c1 + c2

# solve for the fist interval
x = symbols('x')
equation = Eq(x + (center_depth - x * np.tan(alpha)) * c2, length/2)
x1 = solve(equation, x)
print(x1)

d1 = length/2 - x1[0]
w1 = (length/2 - x1[0]) / c2 * c3
print(d1, w1)   

# use d to get width
get_w = lambda d: c3 * (center_depth - (length/2 - d) * np.tan(alpha))

d_list, w_list = [], []
d_list.append(d1)
w_list.append(w1)
total_width, total_distance, d = 0, d1, 0

# get the rest of the intervals by iteration
while total_width < length:
    d = 0.9 * w_list[-1]
    total_distance += d
    d_list.append(d)
    w_list.append(get_w(total_distance))
    total_width = total_distance + w_list[-1] * c1 / c3

# print the result
print(type(d_list))
print(len(d_list))
print(d_list)
print(w_list)

