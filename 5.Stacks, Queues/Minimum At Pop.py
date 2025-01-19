#Back-end complete function Template for Python 3

def _push(lst,n):
	stk = []
	for i in lst:
		stk.append(i)
	return stk

def _getMinAtPop(s,n):
	v = []

	for i in range(n):
		x = s.pop()
		v.append(x)

	minstck = []

	s.append(v[-1])
	minstck.append(v[-1])
	for i in range(n-2,-1,-1):
		s.append(v[i])
		if(s[-1]<minstck[-1]):
			minstck.append(s[-1])
		else:
			minstck.append(minstck[-1])

	for i in range(n):
		print(minstck.pop(),end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3


		

if __name__ == "__main__":
	t = int(input())
	while(t>0):
		n = int(input())
		list1 = [int(i) for i in input().strip().split()]
		mys = _push(list1,n)
		_getMinAtPop(mys,n)
		print()
		t = t-1

# } Driver Code Ends