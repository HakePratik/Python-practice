def Gcd_in_str (str1,str2):
    if str1 + str2 != str2 + str1 :
        return "np divisor string avalable"
    len_gcd=min(len(str1),len(str2))
    return str1[:len_gcd]

str1="rararara"
str2="ra"
print(Gcd_in_str(str1,str2))