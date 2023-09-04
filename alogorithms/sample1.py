def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

print(is_even_or_odd(12))
print(is_even_or_odd(13))
print(is_even_or_odd(112))
print(is_even_or_odd(123))


def ordinalSuffix(number):
    # if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
    
    if number % 100 in (11, 12, 13):
        return str(number) + "th"
    elif number % 10 == 1:
        return str(number) + "st"
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number) + "th"

print(ordinalSuffix(1))
print(ordinalSuffix(2))
print(ordinalSuffix(3))
print(ordinalSuffix(31))
print(ordinalSuffix(111))
print(ordinalSuffix(112))
print(ordinalSuffix(113))
print(ordinalSuffix(115))
