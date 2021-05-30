
# list1=[1,2,3,1,1,2,3,3,3]
# output- 
# 1=1 pair
# 2=1 pair
# 3=2 pair


list1=[1,2,3,1,1,2,3,3,3]
i=0
a=[]
b=[]
while i<len(list1):
    count=0
    m=list1[i]
    j=0
    while j<len(list1):
        n=list1[j]
        if m==n:
            b.append(n)
            count=count+1
        j=j+1
    k=0
    while k<1:
        if m not in a:
            a.append(m)
            count1=count-2 or count-1
            if count%2==0 or count%3==0:
                print(m,"=",count1,"pair")
            count1+=1
        k=k+1
    i=i+1
   


