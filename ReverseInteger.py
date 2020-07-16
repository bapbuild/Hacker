#############Simple#################
#
# inp = input().strip()
#
# def reverseInt(inp):
#     reversedInt = inp[::-1]
#     return reversedInt
#
# print(reverseInt(inp))

###########################################
inp = int(input().strip())

if inp >= 2**31 or inp <= -2**31:
    print (0)
else:
    strg = str(inp)
    if inp>=0:
        rev = strg[::-1]
        print(rev)
    else:
        strg = strg[1::]
        tmp = strg[::-1]
        rev = '-'+tmp
        print(rev)

