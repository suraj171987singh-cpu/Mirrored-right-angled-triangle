def mirrored_triangle_nested(rows):
    # This loop handles each row
    for i in range(1, rows + 1):
        # This loop handles each column in that row
        for j in range(1, rows + 1):
            # Print spaces until we reach the triangle's edge
            if j <= rows - i:
                print(" ", end="")
            else:
                print("*", end="")
        # Move to the next line after finishing a row
        print()

print("mirrored right angled triangle")
num_rows = int(input("Enter the number of rows: "))
mirrored_triangle_nested(num_rows)
