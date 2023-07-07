MIN_STR_LENGTH = 100
length_of_string = 0
main_string = ''
symbol = 0
alpha = ''
while length_of_string < MIN_STR_LENGTH:

    string = input("Print a random string containing 0 or 1:\n")
    main_string += string.translate({ord(i): i for i in string if i in '01'})
    length_of_string = len(main_string)
    symbol_left = (MIN_STR_LENGTH - length_of_string)
    if symbol < 0 or symbol_left == 0:
    #   main_string = main_string[:-abs(symbol)]
      break

    print('Current data length is',length_of_string,end ='')
    print(',',symbol_left,'symbols left.')
    
print('Final data String:')
print(main_string)

final_string_splitted =[main_string[symbol:symbol+4] for symbol in range(0, len(main_string))] 
triads = {'000': {0: 0, 1: 0}, '001': {0: 0, 1: 0}, '010': {0: 0, 1: 0}, '011': {0: 0, 1: 0},
         '100': {0: 0, 1: 0}, '101': {0: 0, 1: 0}, '110': {0: 0, 1: 0}, '111': {0: 0, 1: 0}}

for i in range(len(main_string)-3):
  triads[main_string[i:i+3]] [int(main_string[i+3])] +=1
   

# Print the dictionary in the specified format

for key in triads:
   print(f"{key}: {triads[key][0]},{triads[key][1]}")
