def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list or list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average}")

my_mixed_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average}")
