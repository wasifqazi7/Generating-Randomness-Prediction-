MIN_STRING_LENGTH = 100
length_of_string = 0
main_string = ''
characters_left = 0
test_string_two = ''
len_test_str_two = 0
predictions = ''

while length_of_string < MIN_STRING_LENGTH:
    input_string = input("Please enter a random string with only 1's and 0's ...\n")
    main_string += input_string
    main_string = main_string.translate({ord(i): None for i in main_string if i not in '01'})
    length_of_string = len(main_string)
    characters_left  = MIN_STRING_LENGTH - length_of_string
    if characters_left < 0 or characters_left == 0:
        break
    print(f'Characters Left : { characters_left}')
    print(main_string)

print(f'Final String : \n {main_string}')
final_string_splitted = [main_string[i:i+4] for i in range (0,len(main_string))]
print(final_string_splitted)

triads = {'000': {0: 0, 1: 0}, '001': {0: 0, 1: 0}, '010': {0: 0, 1: 0}, '011': {0: 0, 1: 0},
         '100': {0: 0, 1: 0}, '101': {0: 0, 1: 0}, '110': {0: 0, 1: 0}, '111': {0: 0, 1: 0}}

for i in range(0, len(main_string)-3):
    triads[main_string[i:i+3]][int(main_string[i+3])] +=1

print(triads)

while len_test_str_two < 4:
    test_string_two = input("Please enter another test string (Length 4) conating 0's or 1's)\n")
    len_test_str_two = len(test_string_two)
    test_string_two = test_string_two.translate({ord(i): None for i in test_string_two if i not in '01'})

#print(len(test_string_two))
# split_str = [test_string_two[i:i+4] for i in range(0,len(test_string_two)-3)]
# print(split_str)
# 0101001010010101011111100010010110000101010101010100101
for i in range(0,len(test_string_two)-3):
    if triads[test_string_two[i:i+3]][0] > triads[test_string_two[i:i+3]][1]:
        predictions += '0'
    else:
        predictions += '1'
print('Predictions:')
print(predictions)


compare_str_one = test_string_two[3:]
count = 0
for i in range(0,len(compare_str_one)):
    if compare_str_one[i] == predictions[i]:
        count += 1

acc = count / (len(predictions))
acc = acc * 100

print(f'Computer guessed right {count} out of {len(predictions)} symbols ({acc:0,.2f})')
