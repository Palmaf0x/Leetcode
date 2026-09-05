nums = [4,1,2,1,2]

dictionary = {}

# loop to collect elem
for num in nums :
    if num not in dictionary :
        dictionary[num] = 1
    elif num in dictionary :
        dictionary[num] += 1

# loop to ge the unique one elem
for key,values in dictionary.items() :
    if values == 1 :
        output = key
        print(output)
        break