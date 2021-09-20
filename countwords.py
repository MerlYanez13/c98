def countwords():
    fname=input("please enter your file name")
    count=0
    file=open(fname, 'r')
    for line in file:
        words=line.split()
        count=count+len(words)
    print("now ",count)
countwords() 
