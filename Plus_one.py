input = [1,2,3]
output = []

# converte the array into string
string = ""
for i in input:
    string = string + str(i)

# converte the string back in number
string = int(string)

# add plus on to the number
string = string + 1
string = str(string)

# put the digits into the array as number
for digits in string :
    output.append(int(digits))

# output the result
print(f"The type is {type(output[0])} : {output}")
