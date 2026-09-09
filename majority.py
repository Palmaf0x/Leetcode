input = [3,2,3]

# collet element in the list
elems = {}

for x in input :
    elems[x] = 0

# add on seen element
for num in input :
    for elem in elems.keys() :
        if num == elem :
            elems[elem] = elems[elem] + 1

max_val = 0
output = 0
for elem, val in elems.items() :
    print(elem, val)
    if val > max_val :
        max_val = val
        output = elem

print(output)