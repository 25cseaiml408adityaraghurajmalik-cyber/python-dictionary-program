# Input number of terms
n = int(input("Enter number of terms: "))

# Lambda function
fib = lambda a, b: (b, a + b)

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = fib(a, b)
