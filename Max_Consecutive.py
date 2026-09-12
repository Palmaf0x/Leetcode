
count = 0
max_conv = 0
for i in nums:
    if i == 1 :
        count += 1
        max_conv = max(max_conv, count)
    else:
        max_conv = max(max_conv, count)
        count = 0

return max_conv