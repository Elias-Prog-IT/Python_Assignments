#multiplication table from 0 to 100 using nested for loop.

def main():

    for i in range(11):
         for j in range(11):
             multiply(i, j)

def multiply(x, y):
    product = x * y
    print(x, "*",  y, "=", product)


main()
