'''
An implementation of the multinomial distribution for use with pymc2.
The original pymc implementation gave me problems which I don't exactly 
remember right now.  I think they were related to the small probabilities and 
the many classes.

'''


#Taken from http://stackoverflow.com/questions/3037113/python-calculate-multinomial-probability-density-functions-on-large-dataset
from numpy import array, log, exp
from scipy.special import gammaln



import  numpy as np
from pymc import  *
from pylab import *

def log_factorial(x):
    """Returns the logarithm of x!
    Also accepts lists and NumPy arrays in place of x."""
    return gammaln(array(x)+1)

def multinomial(n, xs, ps):
    xs, ps = array(xs), array(ps)
    result = log_factorial(n) - sum(log_factorial(xs)) + sum(xs * log(ps))
    return (result)
#End of what I took from StackOverFlow

def multinomial_like2(value,logp):
	x2=array(value)
	n2=sum(x2)
	
	maxlogp=max(logp)
	p1=[exp(q-maxlogp) for q in logp]  
	
	psum=sum(p1)
	
	#Give zeros a negligable small value
	p2=[q*(q>1e-100)+1e-100*(q<1e-100) for q in p1]  
	psum=sum(p2)
	p3=[q/psum  for q in p2]
	result=float(multinomial(n2, x2, p3))
	return(result)
	
def WCHMulti(name,value,lp):
	result=Stochastic(\
		logp=multinomial_like2,\
		observed=True,\
		value=value,\
		dtype=int,\
		name=name,\
		random=None,\
		parents={'logp':lp},\
		doc='A version of Mutinomial where logs of probabilities are given. Normalization not required')
	return(result)