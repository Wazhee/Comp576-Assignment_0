import scipy.linalg
import numpy as np


# Task 3:
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,2,7,14])
plt.axis([0,6,0,20])


# Task 4:
x = np.linspace(-10, 10, 100) # define x bounds

y = x**2                        # define y

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'r')

plt.show()

# task 5:
username: Wazhee


