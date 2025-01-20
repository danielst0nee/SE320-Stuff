from collections import Counter

#creating a dictionary that counts the number of instances in a word

word = "mississippi"
counter = {}
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print (counter)

#better
#setdefault returns value of item with the specified key
#if key doesn't exist, it inserts the key, with the specified value
for letter in word:
    counter[letter] = 1 + counter.setdefault(letter,0)
print(counter)

#even better
#Counter class from collections module
print(dict(Counter(word)))
