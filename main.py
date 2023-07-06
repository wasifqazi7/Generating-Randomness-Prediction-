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
    
