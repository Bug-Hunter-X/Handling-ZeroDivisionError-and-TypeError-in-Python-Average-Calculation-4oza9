def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with potential error:
my_numbers = [10, 20, 30, 0] 
result = calculate_average(my_numbers) 
print(f"Average: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"Average: {result}")

my_numbers = [10,20,30,'a']
result = calculate_average(my_numbers)
print(f"Average: {result}")