# The Sum of  two numbers
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c=a+b
# Output: Their sum
print("Sum:",c)

#Odd or Even
num = int(input("Enter a number: "))
#Output: Odd or Even
if num%2==0:
    print("Even")
else:
        print("Odd")

# Factorial calculation
n = int(input("Enter a number: "))

# Output: Factorial of the number
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("Factorial:",factorial)


# Fibonacci sequence
n = int(input("Enter the number of Fibonacci terms: "))

# Output: List of n Fibonacci numbers
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

print("Fibonacci sequence:",fib[:n])

# Reverse a String
s = input("Enter a string: ")

# Output: Reversed string
print("Reversed string:",s[::-1])

# Palindrome Check
s = input("Enter a string: ")

# Output: True if palindrome, else False
print("Is palindrome:",s==s[::-1])

#Leap Year check
year = int(input("Enter the year: "))
#Output
if year % 4 == 0 and year % 100 == 0:
    print(year,"is a Leap year")
else:
    print(year,"is not a leap year")


# Armstrong number
num =  int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
        print(num,"is an Armstrong number")
else:
        print(num,"is not an Armstrong number")
        
        
    
