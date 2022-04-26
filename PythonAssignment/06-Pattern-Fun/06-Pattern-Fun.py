row_count = int(input("Enter number of rows"))
i=1
j=row_count
while i<=row_count:
    k = j
    while k > 0:
        print (i,end = " ")
        k-=1
    print("")
    j-=1
    i+=1

