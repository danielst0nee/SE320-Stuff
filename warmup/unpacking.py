#1 unpacking into seperate variables
first, second, third = [1, 2, 3]

#2 Using asterisk(*) for unpacking into sub-collection
first, *all_middle, last = [1, 2, 3, 4, 5]
print(first) #1
print(all_middle) # [2, 3, 4]
print(last) #5
print("")

#3 Unpacking while ignoring some elements
first, *_, last = [1, 2, 3, 4, 5]
print(first) #1
print(last) #5
print("")

#4 Unpacking into function arguments
def power(x, y):
    return x ** y

numbers = [4, 3]
result = power(*numbers) #same as calling power(4, 3)
print(result)  # 64
print("")

#5 Unpacking to make newer collection
# making a list from other lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ['a', 'b']
combined = [*list1, *list2, *list3] #using asterisk to unpack
print(combined)
print("")