import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=str(input())
        p=str(input())

        score = 0
        for char in p:
            score+=ord(char)-ord('a')+1

        a=[]
        for char in s:
            a.append(ord(char)-ord('a')+1)

        sub_arrays= []
        window_start = 0
        window_end = 0
        curr_sum = a[0]

        while(window_start<len(s) and window_end<len(s)):
            if curr_sum<score:
                window_end += 1
                if window_end == len(s):
                    break
                curr_sum+=a[window_end]


            elif curr_sum>score:
                while(window_start<=window_end and curr_sum>score):
                    curr_sum-=a[window_start]
                    window_start+=1

                if curr_sum>score:
                    assert(window_start==window_end)
                    while(window_end<len(s) and a[window_start]>score):
                        window_start+=1
                        window_end+=1
            else:
                # check for size of subarray.. should be equal to size of p
                if window_end-window_start+1==len(p):
                    sub_arrays.append([window_start,window_end])
                curr_sum -= a[window_start]
                window_start+=1

        for sub_arr in sub_arrays :
            print(s[sub_arr[0]:sub_arr[1]+1],sub_arr[0])
            
        if len(sub_arrays)==0:
            print(-1)
