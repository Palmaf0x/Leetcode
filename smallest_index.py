nums = [1,2,3]
smallest = -1
def sumNumber(num) :
    temp = str(num)
    temp_sum = 0
    for digit in temp :
        temp_sum += int(digit)
    return temp_sum

for i in range(0, len(nums)) :
    temp = sumNumber(nums[i])
    if temp == i :
        smallest = i
        break

print(smallest)
