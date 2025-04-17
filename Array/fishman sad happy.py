def countHS(fish_caught):
    happycount = 0
    sadcount = 0
    for i in range(len(fish_caught)):
        # Check if the current fish count is greater than all previous days
        if all(fish_caught[i] > fish_caught[j] for j in range(i)):
            happycount += 1
        else:
            sadcount += 1

    return happycount, sadcount

# Example Input
fish_caught = list(map(int,input("enter a fish caches in each day:"). split()))
happy, sad = countHS(fish_caught)

print(f"Happy days: {happy}")
print(f"Sad days: {sad}")