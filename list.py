# in this i ll some list problems in python
#To find the max in the list

new=[1,2,3,4]
print(max(new))

#To swap two lists
new=[12,13,15]
new1=[1,2,3]

new,new1=new1,new
print(new,new1)
# same goes for a single list to if you want to swap the values of list(i.e use the indexes)

#To check any element exist on list or not
numbers=[1,2,3,4,5,55,66,98]
if 1 in numbers:
    print('It exist in the list')
else:
    print('1 is not in the list ')

#To sort a list
new=[1,2,3,444,55,6666,12]
new.sort()
print(new)

#To reverse a list
new=[1,2,3,4,5,55]
new.reverse()
print(new)

#To find Sum and avg of a list

new=[1,2,34,5,56,67,78,8]
addtion=sum(new)
avg=addtion/len(new)
print(addtion)
print(avg) #Sum is a built in fucntion to add

#To multiply number in the list,we need to insert math module
import math as m #to use math module faster we kinda gave it a nickname as 'm'
new=[1,2,3,4]
print(m.prod(new))

#To find the 2nd largest number in the list
new=[1,2,3,4,5]
new.sort(reverse=True) # this sets the list in descending order and then we take index 1 i.e 2nd greatest
print(new[1])

#To find even numbers in the list
new=[1,2,3,4,5,6,7,8,9,0]
filterr=[]
for val in new:
    if val%2==0:
        filterr.append(val)
print(filterr) # same process for Odd numbers

#To count even numbers in the list
new=[1,2,3,4,5,6,7,8,9,0]
filterr=[]
for val in new:
    if val%2==0:
        filterr.append(val)
print(f'There are {len(filterr)} even numbers in the list.') 

#To remove any element from list
new=[1,2,'ktm']
new.pop(0) #Index of 1
print(new)

#To count and add +ve and -ve numbers of the list
new=[1,2,3,4,5,0,-1,-55,-66]
positive=[]
negative=[]
for val in new:
    if val>0 or val==0:
        positive.append(val)
    else:
        negative.append(val)
print(positive)
print(negative)
print(f'The total no of positive number in given list is {len(positive)}')
print(f'The total no of negative number in given list is {len(negative)}')
#To understand loop methods we need to learn loops properly...for loop makes it easier to solve problems

#To remove elements from list

new=[1,2,3,4,5,6,7,8,9,0]
even=[2,4,6,8]
neww=[]
for num in new:
    if num not in even:
        neww.append(num)

print(neww)        

# To get a random element from a list using random module
import random
new=[1,2,4,5,6]
get=random.choice(new)
print(get)


# Thanks for watching this short list methods.