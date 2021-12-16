



# lists waxaa loo isticmaala in lagu keeydiyo multiple items
# adigoo isticmaalaya hal variable
# todo) lists waa data structure-ka loogu isticmaalka badanyhy

# ists are created using square brackets

# example 1
myLists=['Cambo','Liin','Qaro'] # this is the list

# list-ga waxaa ku keydin kartaa qiimiyaal kala duwan
# exmaple

myList2=[1,'String',True,90,'Geedi'] # You Can Store Different Items
print(myList2)

# output : [1,'String',True,90,'Geedi']

# list-ga waa iteration ayaa ku sameeyn kartaa adigoo isticmaalaya loop

#example of iteration

def myList(lists):  # functionn-kaan waxuu qaadanayaa 1 paramater as list
    # loop
    for list in lists:   # you can use for or while loop
        print(list)


list=[10,2,3,4,5,6,7]
iterate=myList(list)  # function-kaan 1 argument ayuu qaadanaya waana list
print(iterate)

# output:
# 10 2 3 4 5 6 7

# length function
# use len() to get the length of the list

_list_=[2,3,4,5,5]
print(len(_list_))

# output: 5


# accessing list
#  to access list use the index of the item
# todo) NOTE: the index of list starts 0
index=[2,3,4,5,6,True]
print(index[4])

# output : 6

## adding element to the list
# you can use  append() and insert() to add the item into the list

# example

addList=[1,2,3,4]
# append takes one argument is value
addList.append(100)

print(addList)
# output : [1,2,3,4,100]

# insert method
insert=[1,2,3,4]

# insert method takes two argument one is index and other is value

# example
insert.insert(0,'True')
print(insert)

# output : ['True',1,2,3,4]

# you can remove the item in the list using pop() and remove()

# pop() is deleted the specific index

# example
mylist3=[1,2,3,4]

mylist3.pop(0) # delete the index 0
print(mylist3)

# output : [2,3,4]

# remove() deleetd specific item
mylist4=[1,2,3,4]
mylist4.remove(3)  # delete the item of 3
print(mylist4)

# output: [1,2,4]



