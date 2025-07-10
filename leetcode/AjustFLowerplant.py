flowerbed=list(map(int,input("enter flowerbed adjustment(0,1)sequence:").strip().split()))
adjust_plot=int(input("Enter how many plots adjust:"))
def adjustflower(flowerbed,adjust_plot):
    flower=[0]+flowerbed+[0]
    for i in range (1,len(flowerbed)+1):
        if flower[i] == flower[i+1] == flower[i-1] == 0:
            adjust_plot-= 1
            flower[i]=1
            if adjust_plot == 0:
                return flower[1:-1]
                break
    else:
        return "no plots adjustment"
print(adjustflower(flowerbed,adjust_plot))
