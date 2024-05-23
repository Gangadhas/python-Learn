height = input("Enter the height of the students\n")
heights = height.split()
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
    print(heights[i])
sum = 0
for i in heights:
    sum += i
print(f"sum is {sum}")
number = 0
for i in heights:
    number += 1
print(f"number is {number}")

Avg = round(sum / number)
print(f"Avg height is {Avg}")
