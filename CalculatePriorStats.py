from numpy import sqrt,array,median,ndarray,exp
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import expit
from scipy.stats.mstats import mquantiles

#number of equiprobable values
n=1000
#p-values corresponding to equiprobable values.  Each value represents and equal amount of probability space.
p=[(i+.5)/n for i in range(n)]

#Mortality rate
lnM=[norm.ppf(t,loc=-3.8,scale=1) for t in p]
M=[exp(t) for t in lnM]

#x and y are used to orthogonalize sigma and T. Generate equi-probable values of both arrays
x=[ norm.ppf(t,loc=0,scale=1/sqrt(.05))  for t in p]
y=[ norm.ppf(t,loc=0,scale=1/sqrt(.057120))  for t in p]

#sigma.  Use all possible combinations of x and y to generate equi-probable values of equiprob_lnsigma
equiprob_lnsigma=[]
for s in y:
    equiprob_lnsigma+=[ 3+.36207*t-.36207*s  for t in x]
#Thin to n-values
equiprob_lnsigma.sort()
equiprob_lnsigma= [equiprob_lnsigma[  int((t+.5)*n)] for t in range(n)]
sigma=[exp(t) for t in equiprob_lnsigma ]

#T.  Use all possible combinations of x and y to generate equi-probable values of T
T=[]
for s in y:
    T+=[ 7+.84483*t+.15517*s  for t in x]
#Thin to n-values
T.sort()
T= [T[  int((t+.5)*n)] for t in range(n)]
ro=[ expit(t)  for t in T]



def CalcOmega(sigma,ro):
    if isinstance(sigma,(list,ndarray)):
        result=[ CalcOmega(s,ro)  for s in sigma]
        return(result)
    if isinstance(ro,(list,ndarray)):
        result=[ CalcOmega(sigma,w)  for w in ro]
        return(result)
    result=sigma*sqrt(1-ro*ro)
    return(result)
    

omega=CalcOmega(sigma,ro)
print(min([min(t) for t in omega]))
print(median(omega))
print(max([max(t) for t in omega]))
q=[.1+.1*i for i in range(9)]
print(mquantiles(omega,prob=q))
x=[ro for t in omega]
y=[sigma for t in omega]
print()
print(median(omega),CalcOmega(median(sigma),median(ro)),median(sigma),median(ro  ))
print()
print('M', mquantiles(M,prob=[.025,.500,.975]))
print()
print('sigma', mquantiles(sigma,prob=[.025,.500,.975]))
print()
print('T', mquantiles(T,prob=[.025,.500,.975]))
print()
print('ro', mquantiles(ro,prob=[.025,.500,.975]))
print()
print('omega', mquantiles(omega,prob=[.025,.500,.975]))

