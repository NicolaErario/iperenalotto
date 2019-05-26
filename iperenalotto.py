from random import sample

#set a list of magic numbers
magic_numbers = [
    32, 33, 40, 41, 42, 44, 49, 51, 52,
    59, 60, 61, 62, 63, 72, 73, 74, 75,
    76, 77, 79, 81, 82, 85, 86, 87, 89
]

#extract 5 unique numbers random from magic list
print(sample(magic_numbers,5))



