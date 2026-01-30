#Task 1
def add(a, b):
    return a + b

#Task 2
def count_capital_letters(some_string):
    capital_letters = 0
    for cp in some_string:
        if cp.isupper():
            capital_letters += 1
    return capital_letters

#Task 3
def decode_string(some_string):
    complete_string = ""
    for sb in some_string:
        similar_character_counter = 0
        for tsb in some_string:
            if tsb.lower() == sb.lower():
                similar_character_counter += 1
        if similar_character_counter <= 1:
            complete_string += "("
        else:
            complete_string += ")"

    return complete_string

#Task 4
def get_odd_count(some_string):
    even_numbers = 0
    for num in some_string:
        if (int(num) / 2) == int(int(num) / 2) and int(num) != 0:
            even_numbers += 1
    return even_numbers

#Tests

#Task 1 test
print(add(1,2))
print(add(2,2))
print(add(4,-7))

#Task 2 test
print(count_capital_letters('Hello World'))
print(count_capital_letters('   A   '))
print(count_capital_letters('qwerty'))

#Task 3 test
print(decode_string("din"))
print(decode_string("recede"))
print(decode_string("Success"))
print(decode_string("(( @"))

#Task 4 test
print(get_odd_count("2468"))
print(get_odd_count("13579"))
print(get_odd_count("01234567"))