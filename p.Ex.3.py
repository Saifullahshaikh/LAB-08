def even(num):
    for i in range(num):
        if i%2 == 0:
            print(i, "is divisible by 2")
        elif i%3 == 0:
            print(i,"is divisible by 3")

print(even(20))