def insertion_sort(A):
  for i in range(1,len(A)):
    curNum=A[i]
    j=i-1
    while j>=0 and curNum<A[j]:
      A[j+1]=A[j]
      j-=1
    A[j+1]=curNum
  return A

print(insertion_sort([2,3,5,1,4]))  

def selection_sort(B):
  for i in range(0,len(B)):
    min_index=i
    for j in range(i+1,len(B)):
      if B[min_index]>B[j]:
        min_index=j
    B[i],B[min_index]=B[min_index],B[i]
  return B

print(selection_sort([8,9,11,7,6]))

def bubble_sort(C):
  for i in range(0,len(C)-1):
    for j in range(0,len(C)-1-i):
      if C[j]>C[j+1]:
        C[j],C[j+1]=C[j+1],C[j]
  return C

print(bubble_sort([6,8,9,1,2]))





      
  
