def count(a,mid):
    ans=0
    j=0
    for i in range(1,len(a)):
        while(j<i and a[i]-a[j] > mid):
            j+=1
        ans+=i-j

    return ans

def kthDiff(a, n, k):
    a.sort()
    l,r=0,a[len(a)-1]-a[0]

    while(r>l):
        mid = (l+r)//2
        if(count(a,mid)<k):
            l=mid+1
        else:
            r = mid
    return r