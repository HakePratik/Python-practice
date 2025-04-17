horses=list(range(1,26))
def grouprace(group):
    return sorted(group, reverse=1)
groups=[horses[i:i+5] for i in range (1,len(horses),5)]
groupwinner=[grouprace(group) for group in groups]
fastter=[winner[0] for winner in groupwinner]
print ("first is:",fastter[0])
print ("second is:",fastter[1])
print ("third is:",fastter[2])
