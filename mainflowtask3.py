#table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

#swap of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print(f"After swapping: a = {a}, b = {b}")

#checking Substring
s1 = input("Enter main string: ")
s2 = input("Enter substring to check: ")
result = s2 in s1
print(result)

#decimal to binary
n = int(input("Enter a decimal number: "))
binary = bin(n)[2:] 
print(f"Binary representation: {binary}")

#Matrix Addition
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions"
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("result matrix is : ",matrix_addition(matrix1, matrix2))

#Matrix Multiplication
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Number of columns in A must equal number of rows in B"
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Result of matrix is:",matrix_multiply(A, B))

#Find a second largest number
def second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements"
    unique_sorted = sorted(list(set(numbers)), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else unique_sorted[0]
nums = [10, 5, 20, 20, 15]
print("The Second Largest Number is:",second_largest(nums))

#Check Anagram
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(is_anagram("listen", "silent"))  
