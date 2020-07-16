num = int(input().strip())

# total = (num-1)%9+1
# print(total)
#
# print(32%9)

def sumint(num):
    numArr = sum(map(int,str(num)))

    print(numArr)
    if numArr<10:
        print(numArr)
    else:
        sumint(numArr)

sumint(num)