'''map function'''
numbers=[1,2,3,4,5]
def square(a):
    return a**2
    
# print(square(5))

# sq=map(square,numbers)
sq=list(map(square,numbers))
print(sq)


squared_numbers = map(lambda x: x**2, numbers)

print(list(squared_numbers))

# using list comprehension
new_list=[]
for  i in numbers:
    new_list.append(square(i))
print(new_list)

'''using inbuilit function in map'''

names=['abc','abcdef','pqr','stve']
length=map(len,names)


# length=list(map(len,names))

print(length)

for i in length:
#map do not use for loop. but it can work over map object , so this how we have used for loop in map
    print(i)
#by taking one more for loop j we understand map can take only one for loop

for j in length:
    print(j)


