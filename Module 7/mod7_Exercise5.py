def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

filtered_list = filter_even_numbers(original_list)
    

print("Original list:", original_list)
print("List with even numbers only:", filtered_list)


#