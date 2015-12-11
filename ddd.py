set1 = ["a","b","c","d","e"]
set2 = ["a","b","f"]
set3 = []

for letter in set1:
    if letter in set2:
        set3.append(letter)

print set3
