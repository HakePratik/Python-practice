
def check_status(a, b, flag):
    if ((a >= 0 or b >= 0) and not flag):
        return False 
    elif (a < 0 and b < 0 and flag):
        return True
    else:
        return False

print (check_status(10,-15,True))
#print (cheak_status.)