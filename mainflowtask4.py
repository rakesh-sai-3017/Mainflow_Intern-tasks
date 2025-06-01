#missing number
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
print("The missing number is:",find_missing_number([1, 2, 4, 5]))

#Check Balanced Paranthesis
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
print(is_balanced("{[()]}"))  
print(is_balanced("{[(])}"))

#Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
print("The longest word is:",longest_word("Python is an amazing language"))

#Count Words in a Sentence
def count_words(sentence):
    return len(sentence.split())
print("Count of Words:",count_words("Hello world this is Python"))

#Check Pythagorean Triplet
def is_pythagorean_triplet(a, b, c):
    nums = sorted([a, b, c])
    return nums[0]**2 + nums[1]**2 == nums[2]**2
print(is_pythagorean_triplet(3, 4, 5))

#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("The Sorted result is:", bubble_sort([5, 1, 4, 2, 8]))

#Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print("The result is:",binary_search([1, 3, 5, 7, 9], 5))

#Find Subarray with given sum
def subarray_with_sum(arr, target):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return (start, end)
    return -1
print("The Subarray is:",subarray_with_sum([1, 2, 3, 7, 5], 12))

#Log Analysis System
from collections import defaultdict

def analyze_log(file_path):
    ip_count = defaultdict(int)
    url_count = defaultdict(int)
    code_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            try:
                parts = line.split()
                ip = parts[0]
                url = parts[6]
                status_code = parts[8]

                ip_count[ip] += 1
                url_count[url] += 1
                code_count[status_code] += 1

            except IndexError:
                # Skip lines that do not conform to expected structure
                continue

    print("\n📍 Top 5 IP addresses:")
    for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{ip}: {count} requests")

    print("\n📍 Top 5 URLs accessed:")
    for url, count in sorted(url_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{url}: {count} hits")

    print("\n📍 HTTP Response Codes Summary:")
    for code, count in sorted(code_count.items()):
        print(f"{code}: {count} times")

# Call the function
analyze_log("webserver.log")








