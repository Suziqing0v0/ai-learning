class Stats:
    def __init__(self,nums):
        self.nums=nums

    def mean(self):
        return sum(self.nums)/len(self.nums)

    def median(self):
        c=sorted(self.nums)
        d=len(c)
        if d%2!=0:
            e=d//2+1
            return c[e-1]
        else:
            f=d//2
            g=d//2+1
            h=c[f-1:g]
            j=(h[0]+h[1])/2
            return j

    def stdev(self):
        k=self.mean()
        p=0
        for m in self.nums:
            p=p+(m-k)**2
        q=p/len(self.nums)
        r=q**0.5
        return r

    def count(self):
        return len(self.nums)

s=Stats([53,87,39,98,69,75,58,40])
print(s.mean())
print(s.median())
print(s.stdev())
print(s.count())
