def fibanocci_iterative(n):
    sum=0
    previous=0
    current = 1
    for item in range(0,n):
        sum = previous+current
        previous = current
        current = sum
        return sum

fibanocci_iterative(10)
#
# def fibanocci_recursion(n):
#     for item in range(0, n):
#         sum1=fibanocci_iterative(n)
#         # print(sum1)
#
# fibanocci_recursion(3)


# def fibonacci_iterative(n):
#     previous = 0
#     current = 1
#     for i in range(n - 1):
#         current_old = current
#         current = previous + current
#         previous = current_old
#     print(current)
# def fibonacci_recursive(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#           fibonacci_iterative(n)
#
#
# fibonacci_recursive(10)
