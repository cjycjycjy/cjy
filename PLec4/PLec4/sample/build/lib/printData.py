
def printData(data,a=0):
    for item in data:
        if isinstance(item,list):
            printData(item,a+1)
        else:
            for  level in range(a):
                print("\t",end="")
            print(item)
            