library("lme4", lib.loc="~/R/win-library/3.2")
afori<-c(0, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, 1, 1, 1, 3, 1, 5, 12, 
         23, 4, 1, 0, 2, 2, 2, 1, 3, 1, 2, 3, 0, 1, 1, 0, 3, 5, 3, 
         5, 4, 2, 6, 4, 11, 3, 2, 4, 3, 4, 3, 2, 5, 2, 4, 1, 3, 1, 
         1, 3, 4, 4, 0, 1, 4, 6, 1, 6, 11, 13, 5, 6, 6, 6, 14, 21, 
         7, 4, 3, 3, 14, 6, 1, 2, 22, 39, 1, 2, 5, 2, 2, 1, 1, 2, 
         2, 1, 2, 1, 2, 2, 2, 0, 1, 0, 2, 8, 1)

af<-afori
nyear<-length(af)
yb<-1:nyear
data<-data.frame(yb=yb,af=af)

result<-glm(af~yb,family=poisson,data=data)
summary(result)

cat('##############')


result<-glmer(af~yb+(1|yb),family=poisson,data=data)
summary(result)

cat('##############')
