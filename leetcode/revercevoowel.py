string=str(input("enter a string:"))
word=list(string)
def reversevowel(word):
    vowel=['i','I','a','A','o','O','u','U','e','E']
    i=0
    j=len(word)-1
    while i<j:
        if word [i] not in vowel:
            i+=1
        elif word[j] not in vowel:
            j-=1
        else:
            word[i],word[j]=word[j],word[i]
            i+=1
            j-=1
    return ''.join(word)
print('reverse vowel is :',reversevowel(word))