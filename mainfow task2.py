def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print("Is 1 prime?", is_prime(1))      
print("Is 2 prime?", is_prime(2))
print("Is 4 prime?", is_prime(4))    
print("Is 5 prime?", is_prime(5))      
print("Is 6 prime?", is_prime(6))   
print("Is 7 prime?", is_prime(7))    
print("Is 9 prime?", is_prime(9))  

#Sum of digits in a number

def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total
print()
print("Math version:")
print("168 →", sum_of_digits(168))
print("775 →", sum_of_digits(775))

#LLCM and GCD

import math

def compute_gcd(a, b):
    return math.gcd(a, b)

def compute_lcm(a, b):
   return abs(a * b) // compute_gcd(a, b) if a and b else 0
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd_result = compute_gcd(num1, num2)
lcm_result = compute_lcm(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")

#list reversal

def reverse_list(original_list):
    reversed_list = []
    for i in range(len(original_list)-1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list
print()
my_list = [32,5,65,48,77]
result = reverse_list(my_list)
print("Original list:", my_list)
print("Reversed list:", result)


#Sort a list

def sort_ascending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
print()
my_list = [99,55,22,45,68,32]
sorted_list = sort_ascending(my_list.copy())

print("Original list:", my_list)
print("Sorted list (ascending):", sorted_list)


#Remove duplicates

def remove_duplicates(input_list):
    seen = []
    for item in input_list:
        if item not in seen:
            seen.append(item)
    return seen
print()
original_list = [26,35,24,26,54,35,25,94,26]
unique_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List without duplicates:", unique_list)


#String Length

def string_length_v2(s):
    return sum(1 for _ in s)
print()
word = "samsung book"
print(f"\nString: '{word}'\nLength: {string_length_v2(word)}")


#Count of vowels

def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in text.lower():
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():  
            consonant_count += 1
    
    return vowel_count, consonant_count
print()
input_string = "Educational University"
vowels, consonants = count_vowels_consonants(input_string)

print(f"String: '{input_string}'")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
