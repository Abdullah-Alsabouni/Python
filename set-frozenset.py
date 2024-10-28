# # set is an unorded colection of unique elements

# basket = {"orange", "apple", "mango", "orange"}
# # basket[0] ==> Error

# a = set()
# a.add(1)
# a.add(2)
# print(a) # a = {1, 2}

# a = {} # type(a) => <class 'dict'>

# a = {'something'} # type(a) => <class 'set'>

# numbers = [1, 2, 3, 4, 2, 3, 4]
# unique_numbers = set(numbers)
# print(unique_numbers) # {1, 2, 3, 4}

# fs = frozenset(numbers)
# print(fs)
# # fs.add(5) # Error

# x = {"a", "b", "c"}

# print("a" in x) # True

# for i in x:
#     print(i)
    

# y = {"a", "g", "h"}

# print(x | y) # Union of x and y ==> {'a', 'h', 'g', 'b', 'c'}
# print(x & y) # Intersection of x and y ==> {'a'}

# print(x - y) # {'c', 'b'}

# x = {'h', 'g'}

# print(x < y) # is x a subset of y ===> True


set1 = frozenset({1,2,3,4,5})
set2 = frozenset({4,5,6,7,8})


print("diffrence between set1 and set2 is",set1.difference(set2))
