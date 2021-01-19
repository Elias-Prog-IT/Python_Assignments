#Prints out the amount of '#' that the user inputs as integer.

n = int(input("n: "))

for i in range(n):
    for j in range(n):
        print("#", end="")
    print()
