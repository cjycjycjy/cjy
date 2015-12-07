from matplotlib import pyplot as plt
import numpy as np


#X = np.arange(0.,5.,0.2)
#plt.plot(X, np.cos(X), color="blue", linewidth=2.5, linestyle="-", label="cosine")
#plt.plot(X, np.sin(X), color="red", linewidth=2.5, linestyle="-", label="sine")
#plt.legend(loc='upper left')



#def f(t):
# return np.exp(-t) * np.cos(2*np.pi*t)
#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)
#plt.figure(1)
#plt.subplot(311)
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#plt.subplot(312)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.subplot(313)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()

#ax = plt.gca() # gca stands for 'get current axis'
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0))
def f(x,y):
 return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


#n = 256
#x = np.linspace(-3, 3, n)
#y = np.linspace(-3, 3, n)
#X,Y = np.meshgrid(x, y)
#plt.axes([0.025, 0.025, 0.95, 0.95])
#plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
#C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
#plt.clabel(C, inline=1, fontsize=10)


n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='winter', origin='lower')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()