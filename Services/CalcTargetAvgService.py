
class CalcTargetAvgService:
    def checkSum(self,Set,factors,target):
        sum=0
        for i in range(len(Set)):
            sum+=Set[i]*factors[i]
        return sum==target
    def getFactors(self,Set,factors,n,target):
        if n==1:
            return []
        result=[]
        copiedFactors=factors.copy()
        for i in range(factors[n-1]):
            if (copiedFactors[n-1]-1) >= 1:
                copiedFactors[n-1]-=1
                copiedFactors[n-2]+=1
            if self.checkSum(Set,copiedFactors,target):
                result=copiedFactors
                return result
            result=self.getFactors(Set,copiedFactors,n-1,target)
        return result
    def getTargetAvg(self,Set,n,target):
        t=n*target
        factors=[]
        factors.append(n-len(Set)+1)
        for i in range(len(Set)-1):
            factors.insert(0,1)
        resultFactors=self.getFactors(Set,factors,len(Set),t)
        if resultFactors==[]:
            print("there is no solution is found")
            return
        result=[]
        for i in range(len(Set)):
            for j in range(resultFactors[i]):
                result.append(Set[i])
        return result