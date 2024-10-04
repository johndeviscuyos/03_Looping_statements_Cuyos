


length = int(input("Enter the side length of the square: "))

for i in range(length):
    if i == 0 or i == length - 1:
        print("X" * length)
    else:
        print("X" + " " * (length - 2) + "X")

