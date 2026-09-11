array1 = [4,9,5]
print(array1)
array2 = [9,4,9,8,4]
print(array2)
output = []

# loop to add element in the output
for x in array1 :
    if x in array2 :
        if x not in output :
            output.append(x)

print(output)