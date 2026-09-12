paragraph = "Bob. hIt, baLl"
paragraph = paragraph.lower()
points = [",", "!", "?", "'", ";", "."]
dictionary = {}
banned = []
# remove the pointuations
for p in points :
    paragraph = paragraph.replace(p, " ")
# create the array of words
paragraph = paragraph.split()
#  filtering the array
filtered_input = [word for word in paragraph if word not in banned]
# add the element in the dictionary
for word in filtered_input:
    if word not in dictionary :
        dictionary[word.lower()]  = 1
    elif word in dictionary :
        dictionary[word.lower() ] += 1
# return the most common
most = 0
for x,y in dictionary.items():
    if y > most :
        most = y
        output = x
print(output)