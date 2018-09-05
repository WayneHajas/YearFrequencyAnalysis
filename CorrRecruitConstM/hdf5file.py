'''
Convergence was slow with 20180512 as a random seed.

If I specify a burn-in of 4000 iterations (on the MCMCs that were generated)then there is convergence.  
However, some of the other MCMCs do not have 4000 iterations.

I achieve more iterations overall if I just exclude 20180512 from the analysis

'''
hdf5file=[         	'../MCMC_20180510.hdf5',\
			'../MCMC_20180511.hdf5',\
#			'../MCMC_20180512.hdf5',\
			'../MCMC_20180513.hdf5',\
			'../MCMC_20180514.hdf5',\
			'../MCMC_20180515.hdf5']
burn=0
nthin=None
