def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with potential error handling:
my_numbers = [10, 20, 30, 0] 
result = calculate_average(my_numbers) 
print(f"Average: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"Average: {result}")

try:
    my_numbers = [10,20,30,'a']
    result = calculate_average(my_numbers)
    print(f"Average: {result}")
except TypeError as e:
    print(f"Error: {e}")