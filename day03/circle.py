import math
import sys

# Get radius from command line arguments
if len(sys.argv) != 2:
    print("Usage: python your_script_name.py <radius>")
    sys.exit(1)  # Exit with error code 1

radius = float(sys.argv[1])

# Calculate area
area = math.pi * radius**2

# Calculate circumference
circumference = 2 * math.pi * radius

# Print the results
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)