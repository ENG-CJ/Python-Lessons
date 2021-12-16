

# dictionary Waxaa loo isticmaala in lagu keeydiyo qiimiyaal
# kuwaas oo ah key:value pairs

# dictionary do not allow duplicates but can change
# dictionary are created using curley brackets
# syntax
myDic={
    "name" : 'Abdulrahman haaji',
    "Occupation" : 'Editor & Developer'
}

# sidaas baa dictionary-ga loo abuuraa

# accessing dictionary
# si aad u access grayeesid dictionary waxad sheegaysa key mesha list-ga
# laga sheego index

#example
print(myDic['name'])

# output : 'Abdulrahman Haaji'

# using format string to print the full info
print(
    f"Name: {myDic['name']}\nOccupation: {myDic['Occupation']}"
)

# output
# Name: Abdulrahman haaji
# Occupation: Editor & Developer

# changing dic
# waxaan raaba inaan badalo magac aan ku badalo magac kale
# si aad ubadasho waxaad sheegaysaa (key) ama id aad rabto inaad
# kabadasho qiimaha
# example
myDic['name']='Mohamed'
print(myDic)

# output:
# {'name': 'Mohamed', 'Occupation': 'Editor & Developer'}


# adding key:value to the dic
myDic2={
    "carName" : "BMW",
    "Speed" : "200k/hr"
}

# waxaan rabaa inaan kuso daro key:value oo ah color iyo qiimihisa

# this is the syntax
myDic2['color']='Brown'
print(myDic2)

# output
# {'carName': 'BMW', 'Speed': '200k/hr', 'color': 'Brown'}

# Removes you can remove the item by providing the item key
# methods pop() or popItem()

# example
mydic3={
    "name" : 'ali',
    "univ" : 'Jamhuuriya'
}

# I want to Delete the univ
# syntax
mydic3.pop('univ') # pop delete the specific key
print(mydic3)

# output
# {'name': 'ali'}

# popItem() delete the last insertion item
mydic4={
    'name' : 'ahmed',
    "gender" : "male",
    'age' : 23
}
mydic4.popitem()
print(mydic4)

# output
# {'name': 'ahmed', 'gender': 'male'}

# looping through diction
def mydic(dictionary): # function-kan waxaan ubaas gareeyay data dictionary ah
    # loop
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")

dics={"name": 'hanmdi','age': 29}
loop=mydic(dics)
print(loop)

# name: hanmdi
# age: 29


# nedted dictionary
nested_dic={
    "microsoft":{
        "widnows 7",
        "window 10",
        "window 11"
    },
    "Amazon":{
        "MS-1",
        'MS-3',
        'MS-4'
    }
}
# you can print specific dictionary by using thier keys
# example
print(nested_dic['microsoft'])

# output
# {'window 10', 'window 11', 'widnows 7'}