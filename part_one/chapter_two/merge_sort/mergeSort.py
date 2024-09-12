#问题描述。输入n个数进行排序
import math
MAX = 100000 #正无穷 float("inf")           #负无穷 float("-inf")
n = int(input("输入n:"))
array = []
num = n
while num>0:
    nn = int(input())
    array.append(nn)
    num-=1
print(array)
def merge(A,p,q,r):
    L = [0]*(q-p+1)
    for i in range(q-p+1):
        L[i] = A[p+i]
    L.append(MAX)
    R = [0]*(r-q)    
    for i in range(r-q):
        R[i] = A[q+i+1]
    R.append(MAX)
    k=p
    n,m = 0,0
    while k<=r:
        if L[n]<=R[m]:
            A[k] = L[n]
            n+=1
        else:
            A[k] = R[m]
            m+=1
        k+=1
def mergeSort(A,p,r):
    if p<r:
        q = math.floor((r+p)/2)-1  #int() 向0取整，即结果一定比该数绝对值小
        if(q<p): q=p               #感觉这样取整有点刻意，明天想想
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
mergeSort(array,0,n-1)
print(array)
