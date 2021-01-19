#Prints out the amount of '#' that the user inputs.

n = int(input("n: "))

for i in range(n):
    for j in range(n):
        print("#", end="")
    print()
