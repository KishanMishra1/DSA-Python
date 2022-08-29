arr=[4,3,6,2,1,1] #Y Y2

n=6
sumofnele=(n*(n+1))/2 #X
sumofsqele=n*(n+1)*(2*n+1)/6 #X2

#X -missing ele
#Y -duplicate ele
val1=sumofnele-sum(arr)
val2=sumofsqele-sum([i*i for i in arr])
X=(val2/val1+val1)/2
Y=X-val1
print("Missing Value:",int(X),'Duplicate Value:',int(Y))


