input_string = input("Enter your string : ")
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

# Show Output
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))

Output: Enter your string : Mississippi
Per char frequency in 'Mississippi' is :
 {'M': 1, 'i': 4, 's': 4, 'p': 2}

