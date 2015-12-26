# This function returns list of non unique numbers from a given list of integers
# If you want unique numbers instead you can replace 'return non_unique' with 'return unique'
# Or if you want both replace return with 'return unique, non_unique'

# Non Unique Examples
# [5, 5, 5, 5, 5] => [5, 5, 5, 5, 5]
# [10, 9, 10, 10, 9, 8] => [10, 9, 10, 10, 9]

def unique(list):
    unique = []
    non_unique = []
    for num in list:
        if list.count(num) == 1:
            unique.append(num)
        if list.count(num) > 1:
            non_unique.append(num)
    return non_unique
