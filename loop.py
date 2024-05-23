Numbers = input("Enter the Values\n")
Number_list = Numbers.split()
for i in range(0, len(Number_list)):
    Number_list[i] = int(Number_list[i])
    print(Number_list[i])
High = 0
for i in Number_list:
    if i > High:
        High = i
print(f"Highest value is {High}")
