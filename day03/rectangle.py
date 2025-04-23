import sys

# Get height and width from command line arguments
if len(sys.argv) != 3:
    print("Usage: python your_script_name.py <height> <width>")
    sys.exit(1)  # Exit with error code 1

height = float(sys.argv[1])
width = float(sys.argv[2])

# Calculate area
area = height * width

# Calculate perimeter
perimeter = 2 * (height + width)

# Print the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
