﻿import numpy as np
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

#d = np.arange(36).reshape(6,6)
#print(d)
#mask = np.array(np.array([1,0,1,0,0,1],dtype = bool))
#print(d[mask,3])
##mask1=np.array([3,4,5,3,4,5,3,4,5])
##mask2=np.array([0,0,0,2,2,2,5,5,5])
#mask1=np.array([3,4,5])
#mask2=np.array([0,2,5])
#print(d[3: ,np.array([0,2,5])])

##값이 두번 들어간다 곱하기 2하면 - list
#temp = [1,2,3,4]
#print(temp*2)

##행렬로 만들면 각 원소의 값이 두배로 커진다 곱하기 2하면 - 행렬
#print(data*2)
#print(data*data)
#print(data+2)

##행렬의 곱셈
#print(data.dot(data))

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = np.array([1,2,3,4])

##각 원소간의 비교
#print(a==b)
#print(a>b)


##행렬간에 같은지 다른지 비교
#print(np.array_equal(a,c))

#d = np.array([1,0,1,0], dtype = bool)
#e = np.array([1,1,0,0], dtype = bool)
#print(np.logical_or(d,e))
#print(np.logical_and(d,e))

##안의 리스트에 전부다 True여야 True 반환
#print(np.all([True,True,False]))
#any 는 하나라도 True면 True 반환
#print(np.any([True,True,False]))

## 초월 함수
#f = np.arange(5)
#print(np.sin(f))
#print(np.cos(f))
#print(np.exp(f))

##전이행렬
#t = np.triu(np.ones((3,3), dtype = int),1) #상삼각행렬
#print(t)
#print(t.T)

#print(np.sum(a))
#print(a.sum())

#x = np.array([[1,1],[2,2]])
#print(x)
#print(x.sum(axis=0)) # columns
#print(x.sum(axis=1)) # rows

#print(x[0,:].sum())
#print(x[1,:].sum())

#print(data)
#print(data.min())
#print(data.max())
#print(data.argmax())
#print(data.argmin())

#print(data.mean())# 원소들의 평균
#print(np.median(data))#원소들의 중간값
#print(np.median(data,axis=0))#축설정

#print(data.std())
##############################################################
#data = np.loadtxt('data.txt')
##print(data)

#year,hares,lynxes,carrots = data.T
#print(data)
#print(data.mean(axis=0))
#print(data.std(axis=0))
#print(year[hares.argmax()])
#print(year[lynxes.argmax()])
#print(year[carrots.argmax()])
#print(np.mean(hares))
#print(np.mean(lynxes))
#print(np.mean(carrots))
#print(np.std(hares))
#print(np.std(lynxes))
#print(np.std(carrots))


################################################################
#print(data.T) 
#plt.plot(year,hares,year,lynxes,year,carrots)
#plt.show()


#a =np.tile(np.arange(0,60,10),(6,1)).T
#print(a)
#b = np.array([0,1,2,3,4,5])
#data = a+b
#print(data)

#12/2 - Broadcasting 예

#mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])#print(mileposts[:, np.newaxis])#distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
#print(distance_array)

####

#x,y = np.arange(5), np.arange(5)[:,np.newaxis]
#distance = np.sqrt(x**2+y**2)
#print(distance)

#plt.pcolor(distance)
#plt.colorbar()
#plt.show()

####

#x,y = np.mgrid[0:5,0:5]
#x,y = np.mgrid[0:5,0:5]
#print(x)
#print(y)

#x,y = np.ogrid[0:5,0:5]
#print(x+y)

####
#a = np.array([[1,2,3],[4,5,6]])
#print(a.ravel())
#print(a.T)
#print(a.T.ravel())

#b = a.ravel()
#print(b)
#b = b.reshape((2,3))
#print(b)

####

#z =np.array([1,2,3])
#print(z)
#print(z[:,np.newaxis])
#print(z[np.newaxis,:])

#a = np.arange(4)
#print(a)
#a.resize(8)
#print(a)

####

#a =  np.array([[4,3,5,6],[1,7,2,5]])
#b = np.sort(a,axis=1)
#print(a)
#print(b)
#a.sort(axis=0)
#print(a)

#a = np.array([4,3,1,2])
#print(a)
#j = np.argsort(a)
#print(j)
#j_max = np.argmax(a)
#print(j_max)
#j_min = np.argmin(a)
#print(j_min)

#####

#p = np.poly1d([3,2,-1])
#print(p(0))
#print(p.roots)
#print(p.order)
#p = np.polynomial.Polynomial([-1,2,3])
#print(p(-1))

########

#x = np.linspace(0,1,20)
#y = np.cos(x)+ 0.3*np.random.rand(20)
#p = np.poly1d(np.polyfit(x,y,3))
#print(p)
#t = np.linspace(0, 1, 200)
#plt.plot(x, y, 'y*', t, p(t), 'k*')
#plt.show()
##############

#x = np.linspace(-1, 1, 2000)
#y = np.cos(x) + 0.3*np.random.rand(2000)
#p = np.polynomial.Chebyshev.fit(x, y, 90)
#t = np.linspace(-1, 1, 200)
#plt.plot(x, y, 'r.')
#plt.plot(t, p(t), 'k-', lw=3)
#plt.show()

############

img = plt.imread('image.png')
print(img.shape,img.dtype)

temp = img[50:100,:100]  #일부 이미지 가져올때 슬라이싱

plt.imshow(temp)
plt.show()





























