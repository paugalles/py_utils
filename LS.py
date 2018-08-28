import numpy as np

def xy2leastSQ(x,y,deg=1):
	'''deg is the polynomial degree'''
	mytuple_degs = [(x**d).reshape(len(x),1) for d in range(deg+1)]
	X = np.matrix( np.concatenate( mytuple_degs , axis=1 ) )
	Y = np.matrix( y.reshape(len(y),1) )
	theta = np.linalg.inv(X.T*X)*X.T*Y
	#y_aprox = X*theta
	#y_aprox = np.polyval(p, x)
	return theta
