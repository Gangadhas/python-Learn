Numbers = int(input("Enter the Max Number\n"))
sum = 0
for i in range(0, Numbers):
    if i%2 == 0:
        print(i)
        sum += i

print(f"sum of even numbers is {sum}")

Numbers = int(input("Enter the Max Number\n"))
sum = 0
for i in range(2, Numbers + 1, 2):
    print(i)
    sum += i

print(f"sum of even numbers is {sum}")


