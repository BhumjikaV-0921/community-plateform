number = int(input("Enter a number : "))

fl = 0
print(fl)
sl = 1
print(sl)



for i in range(number):
    tl = fl + sl
    fl = sl
    sl = tl
    print(tl)

