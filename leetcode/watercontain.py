def container(height):
    area=0
    minimum=0
    maximum=len(height)-1
    while maximum > minimum:
        width= maximum - minimum
        water=width*min(height[minimum],height[maximum])
        area=max(area,water)
        if height[maximum]>height[minimum]:
            minimum+=1
        else:
            maximum-=1
    return area
height=[1,8,6,2,5,4,8,3,7]
print(container(height))
