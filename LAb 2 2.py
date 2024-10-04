




size = int(input("Enter the size of the array: "))

elements = list(map(int, input("Enter the elements separated by spaces: ").split()))

if len(elements) != size:
    print(f"Error: You entered {len(elements)} elements, but the size specified was {size}.")
else:
    print("Cubes of the elements:")
    for element in elements:
        print(element ** 3)

