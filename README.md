# YearFrequencyAnalysis
Code(primarily python) for building and applying Framework Analysis(FA) models for analysis of age frequency models.  

Note that these files use PYTHON3 and pymc2.

CorrRecruitConstM.py is an example of a full model.  The model can be implemted through pymc.  The submodels, recruitment, mortality and sampling, are integrated through multiple inheritance.  

AutoCorrelatedRecruit.py is an example of a recruitment submodel.  Must produce nodes called LogRecruit
ConstantMortality.py is an example of a mortality submodel.  Must produce nodes called ProbSurv
Multinomial.py is an example of a sampling mortality.

ExecuteModel is a library that actually executes a model and generates an MCMC.

seed.20180510.py  is an example of a file that puts it all together.  
  Data is extracted from a file.
  First and last years are specified.
  Random seeds, burn-ins and thinning are specified.
  Name of output file includes the  random seed.
  
CorrRecruitConstM is an example of how a directory can be set up to build and analyze MCMCs.
Thus far, MCMCs have been stored in hdf5 files.

Traditional is a directory where other methods of age-frequency-analysis are appled.  Chapman Robson.  The GLMM methods from Millar 2015.

There are libraries for analyzing the MCMCs.  
  Most importantly, GetParamStats.py retrieves values from hdf5 files.  If multiple hdf5 files are specified, then effectively, the MCMCs area just appended one after the other.
  
 There are batch-files in here - just because they make it easier to do things.  Within the batch-files, directory names will have to be changed in order for things to work.
 
 
 If you have questions, I can be reached at wayne.hajas@dfo-mpo.gc.ca
