import numpy as np
from matplotlib import pyplot as plt
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(data)
#print(data.dtype)

#print(np.ones((5,4), dtype = int))
#print(np.eye((5), dtype = int))
#print(np.diag(np.array([1,2,3,4])))
#print(data.T)

#d = np.array([1,2,3])
#print(d.T)
#print(np.arange(10,0,-1)[:, np.newaxis])

#print(np.arange(35).reshape(5,7))
#print(np.linspace(1,4,6))

#print(np.random.randn(4,4))

#data = np.loadtxt('data.txt')
#print(data)

#print(data)
#print(data[0])
#print(data[-1])
#print(data[0:2])
#print(data[:2])
#print(data[0:3:2])
#print(data[::-1])
#print(data[2][0])
#print(data[0:3:2,::3])

#x = np.arange(10,1,-1)
#print(x[np.array([3,3,1,8])])
#print(x[np.array([[1,1],[2,3]])])

#y = np.arange(35).reshape(5,7)
#print(y)
#print(y[np.array([0,2,4])])
#b = y>20
#print(y[b])

d = np.arange(36).reshape(6,6)
print(d)
mask = np.array(np.array([1,0,1,0,0,1],dtype = bool))
print(d[mask,3])
#mask1=np.array([3,4,5,3,4,5,3,4,5])
#mask2=np.array([0,0,0,2,2,2,5,5,5])
mask1=np.array([3,4,5])
mask2=np.array([0,2,5])
print(d[3: ,np.array([0,2,5])])