str_example = 'aaabbccccdaa'
first_symbol = str_example[0]
count = 0
new_str = ''
for symbol in str_example:
    if symbol == first_symbol:
        count += 1
    else:
        new_str += first_symbol + str(count)
        first_symbol = symbol
        count = 1

new_str += first_symbol + str(count)
print(new_str)
