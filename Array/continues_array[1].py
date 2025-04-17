def continues(arr):
    remove_duplicate = set(arr)
    maximum=max(arr)
    minimum=min(arr)
    if maximum-minimum+1 == len(remove_duplicate):
        return True 
    else:
        return False
arr=list(map(int, input("enter a array:"). split( )))
if continues(arr):
    print ("continues array")
else:
    print ("not continues array")