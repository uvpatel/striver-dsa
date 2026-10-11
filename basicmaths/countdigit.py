n = int(input("Enter a number: "))

abs(n)  # Taking absolute value to handle negative numbers
count = 0

while n > 0:
    if n == 0 or n == 1:
        count = 1
        break

    n = n // 10
    count += 1

print(count)