def get_stats(scores):
    avg=sum(scores) / len(scores)
    hi=max(scores)
    lo=min(scores)
    order=sorted(scores)
    return avg,hi,lo,order
scores=[85,92,78,90,66,88]
avg,hi,lo,order=get_stats(scores)

print(avg,hi,lo,order)