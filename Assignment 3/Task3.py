def count_case_letters(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper_count, lower_count = count_case_letters(sample_string)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
