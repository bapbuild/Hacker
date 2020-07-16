#############Sample1#######################
# str1 = input().strip()
# def reverser(s):
#     y =''.join(reversed(s))
#     return y
#
# print(reverser(str1))


#############Sample 2################
# str1 = input().strip()
#
# def reverser(word):
#     reword = word[::-1]
#     return reword
#
#
# print(reverser(str1))

######################Sample 3#################

str1 = input().strip()

def reverse(str1):
    reversed =''
    index= len(str1)
    while index>0:
         reversed += str1[index-1]
         index-=1
    print(reversed)

reverse(str1)