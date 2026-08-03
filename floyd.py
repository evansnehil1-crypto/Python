
print("Half Pyramid Pattern of Stars (num):")
n = int(input("enter the number of rows: "))

num = 1

for i in range(n): 

    for j in range(i+1):

        print(num , end=" ")
        num += 1
    print()