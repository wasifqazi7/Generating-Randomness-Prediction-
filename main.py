MIN_STR_LENGTH = 100
length_of_string = 0
main_string = ''
symbol = 0

while length_of_string < MIN_STR_LENGTH:
    print('Print a random string containing 0 or 1:')
    string = input()
    main_string += string.translate({ord(i): None for i in 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUPpQqRrSsTtUuVvWwXxYyZz_23456789., '})
    length_of_string = len(main_string)
    symbol_left = (MIN_STR_LENGTH - length_of_string)
    if symbol < 0 or symbol_left == 0:
        break

    print('Current data length is', length_of_string, end='')
    print(',', symbol_left, 'symbols left.')
    
print('Final data String:')
print(main_string)

final_string_splitted = [main_string[symbol:symbol+4] for symbol in range(0, len(main_string))] 
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
zeros = [0, 0, 0, 0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(triads)):
    for j in range(len(final_string_splitted)):
        if final_string_splitted[j].startswith(triads[i]):
            if final_string_splitted[j][-1] == '0':
                zeros[i] += 1
            elif final_string_splitted[j][-1] == '1':
                ones[i] += 1

for i in range(len(triads)):
    print(f'{triads[i]}: {zeros[i]},{ones[i]}')
