input = [1,2,0,0]
k = 34
output = []
print(type(input))
# convertin of the array
string = ''

for i in input :
    string = string + str(i)

print(string)

# convertion of string to integer
string = int(string)
num = string + k

num = str(num)

# add element in the output
for digit in num :
    output.append(int(digit))

print(output)