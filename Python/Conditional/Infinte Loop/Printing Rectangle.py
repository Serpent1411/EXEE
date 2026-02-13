height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Outer while loop to iterate over the height of the rectangle
i = 0
while i < height:

    # Inner while loop to iterate over the width of the rectangle
    j = 0
    while j < width:
        print("*", end="")
        j += 1

    # Move to the next line after printing the width of the rectangle
    print()

    # Move to the next row of the rectangle
    i += 1