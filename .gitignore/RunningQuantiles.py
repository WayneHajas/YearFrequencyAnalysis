from scipy.stats.mstats import mquantiles
import matplotlib.pyplot as plt

def RunningQuantile(x, prob=[.025,.975]):
    n=len(x)
    nhalf=int(n/2)
    LowStart=list(map(lambda i:mquantiles(x[: 1+i],prob=prob,alphap=1,betap=1)  ,range(nhalf)))    
    UppStart=list(map(lambda i:mquantiles(x[-i-1:],prob=prob,alphap=1,betap=1) ,range(nhalf)))
    
    nquant=len(prob)
    LowListQuant=list(map(lambda i:list(map(lambda LS:LS[i],LowStart))     ,range(nquant)))    
    UppListQuant=list(map(lambda i:list(map(lambda US:US[i],UppStart))     ,range(nquant)))
    result=[LowListQuant,UppListQuant]
    return(result)

def pltRunningQuantile(plt,x, prob=[.025,.975],LowCol='r',UppCol='r',alpha=0.25):
    RQ=RunningQuantile(x, prob=prob)
    
    SampSize=list(range(1,1+len(RQ[0][0])))
    
    #Start from beginning
    plt.fill_between(SampSize,RQ[0][0],RQ[0][-1],color=LowCol,alpha=alpha )
    for t in RQ[0]:
        plt.plot(SampSize,t,LowCol+'-',linewidth=3)   
    plt.plot( [SampSize[0],SampSize[-1]],2*[RQ[0][ 0][-1]],LowCol+'-',linewidth=3  )
    plt.plot( [SampSize[0],SampSize[-1]],2*[RQ[0][-1][-1]],LowCol+'-',linewidth=3  )
    
    #Start from end
    plt.fill_between(SampSize,RQ[1][0],RQ[1][-1],color=UppCol,alpha=alpha )
    for t in RQ[1]:
        plt.plot(SampSize,t,UppCol+'-',linewidth=3)    
    plt.plot( [SampSize[0],SampSize[-1]],2*[RQ[1][ 0][-1]],UppCol+'-',linewidth=3  )
    plt.plot( [SampSize[0],SampSize[-1]],2*[RQ[1][-1][-1]],UppCol+'-',linewidth=3  )

    
if __name__ == "__main__":
    x=list(range(10))
    prob=[.025,.975]
    
    plt.close()
    pltRunningQuantile(plt,x, prob=[.025,.975],LowCol='r',UppCol='b',alpha=0.25)
    plt.show()