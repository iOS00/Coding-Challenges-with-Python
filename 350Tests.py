# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:36:44 2022

@author: winpr
"""

import sys
print (sys.version.split()[0])

pi = 3.1415 

a = float (round(pi,2))
print (a)

print("version".upper())

radius = 5
pi = 3.14
Area = pi*radius**2
print (Area)


body = 1000
rate = .03
t = 5
amount = body
for i in range (1, (t+1),1):
    amount = amount+amount*rate
print(f"The future value of the investment: {round(amount, 2)} USD")


total = []
for n in range (1, 11, 1):
    sum10 = 10 + 4*n
    total.append(sum10)
sum10 = sum(total)
print(f"The sum of the first 10 elements in a sequence: {sum10:.1f}")

############# Calculations in Python ###################################

a = 1
b= 5
c= 4
import math
D = b**2-4*a*c
x1=(-b+math.sqrt(D))/2*a
x2=(-b-math.sqrt(D))/2*a
print (f"x1 + x2 = {x1+x2:.1f}\nx1x2 = {x1*x2:.1f}")


# Calculate the midpoint of the segment with ends at the points: A = (2, 4), B = (-4, 6)

A = (2,4)
B = (-4,6)

M = ((A[0]+B[0])/2, (A[1]+B[1])/2)
print(f'The middle point: {M}')

# Calculate the distance of two points A = (3, 2), B = (- 1, -1) 

import math #or  **0.5 == math.sqrt()
A = (3,2)
B = (-1,-1)

d = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
print(f'The distance between points A and B: {d:.1f}')

# Find the roots of the quadratic equation: x**2+5*x+4 = 0

a=1
b=5
c=4

D = b**2 - 4*a*c
print(D) # D > 0: there are 2 real and distinct roots

roots = ((-b+D**0.5)/(2*a), (-b-D**0.5)/(2*a))
print(f'x1={roots[0]}\nx2={roots[1]}')
    
# Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5

numbers= [4,3,4.5,5]

GM = 1
for num in numbers:
    GM=GM*num
    
GM = GM**(1/len(numbers))
print(f'Geometric average of the given numbers: {GM:.2f}')

# Calculate the sum of the infinite geometric sequence

# 1, 1/2, 1/4, 1/8, ...

a1 = 1
a2 = 1/2
q = a2 / a1
S = a1 / (1 - q)
print(f'The sum of the sequence: {S}')

#Calculate the standard deviation of the following set: 10, 11, 9

data = [10,11,9]

m= sum(data)/len(data)

stdev= 0
for num in data:
    stdev = stdev + (num - m)**2
    
stdev = (stdev/len(data))**0.5
print(f'The standard deviation: {stdev:.2f}')


##################### print () function ################################

string = '1 0 0 1 0 1'
string_new = int(string[::2],2)
print(f"Number found: {string_new}")

## reverse slicing
text = 'Python Course'
print (text[::-1])

#find multiple 
text = 'python is a popular programming language.'
number=text.count("p")
print(f"Number of occurrences: {number}")

#bool
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
bool1 = code1[-4:]=="2020"
bool2 = code2[-4:]=="2020"
print(f"code1: {bool1}")
print(f"code2: {bool2}")

#remember different types of " ' inside 
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
print (f"path1: {path1.find('scientist')}")
print (f"path2: {path2.find('scientist')}")
print (f"path3: {path3.find('scientist')}")

#is alphanumeric?
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f"code1: {code1.isalnum()}")
print(f"code2: {code2.isalnum()}")


url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
print ((url.split("/")[-1]).replace("-"," "))

subjects = {'mathematics', 'biology'}
subjects.add('english')
print(subjects)

#difference between sets
text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text=text.lower()
text=text.replace(".", "")
text = text.replace(" ","")
letters = set(text)
number=len(letters.difference(vowels))
print(f'Number of items: {number}')

#SET - Symmetric difference of two sets
A = {2, 4, 6, 8}
B = {4, 10}
symmetric_difference = A.symmetric_difference(B)
print (f"Symmetric difference: {symmetric_difference}")

#SETs intersection

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
intersec = is_clicked.intersection(is_bought)
print(f"Customer ID: {intersec}")

#TUPLES
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
print (dji1+(dji2))

#Nested tuples
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
print(tuple((dji1, dji2)))

#Count> Number of occurrences
default = ('YES', 'NO', 'NO', 'YES', 'NO')
print (f"Number of occurrences: {default.count('YES')}")

#Tuples are immutable - create new to get sorted
names = ('Monica', 'Tom', 'John', 'Michael')
new_tuple_sorted= tuple(sorted(names))
print (new_tuple_sorted)

#Sort nested by age (using lambda)
info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Ascending: {asc}')
print(f'Descending: {desc}')


#SET comprehension (in stead of using loops)

x = set (i*2 for i in range(4) if i%2==0)#%-modulus
print(x)

x = set ((a,b) for b in range(3) for a in range(2)) #1st for -external loop, 2nd for - internal(remember:set - unordered!)
print(x)

#dictionary comprehension  
#example convert temperature from feh to cel:
#complicated example WITHOUT using comprehension ( with lambda, zip):
    
feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
cel = list(map(lambda x:(float(5)/9)*(x-32), feh.values()))
cel_dict= dict(zip(feh.keys(), cel))
print (cel_dict)

#example above with using dictionary comprehension: 
feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in feh.items()}
print(cel_dict)

#comprehensions with if statement

dict = {'a':1,'b':2, 'c':3, 'd':4}
new_dict = {k:v for (k,v) in dict.items() if v>3}
print (new_dict)

#comprehension with if statement
dict = {'a':1,'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
new_dict = {k:("Even No" if v%2== 0 else "Odd No") for (k,v) in dict.items()}
print(new_dict)

#comprehension with multiple if statements
dict = {'a':1,'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
new_dict = {k:v for (k,v) in dict.items() if v>3 if v%2==0}
print(new_dict)

#Nested dictionary comprehension
dict = {'one':{'a':10},'two':{'b':20}}
for (external_key, external_value) in dict.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})
dict.update({external_key:external_value})
print (dict)

#####Lists#####
cities = ['Los Angeles', 'New York', 'Chicago']
cities.append('Houston')
print(cities)

text = 'Python programming'
text = text.lower()
text=text.replace(" ", "")
unique=list(set(text))
print(sorted(unique))

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print (techs)

hashtags = ['summer', 'time', 'vibes']
print("#"+"#".join(hashtags))

#Function within a function

def addition (a,b):
    def add (x,y):
        return x+y
    print (f'The result is: {add(a,b)}')#here arguments (a,b) are passed into add function (x,y)
    
print(addition(2,3))

# Function passed as argument to another function
def func1(function):#important to determine argument class (function)
    return print("I am func1")

def func2():
    return print("I am func2")

print(func1(func2())) # executs in following order: func2, func1

# Function returns another function - example 1
def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function
z=outer_function(2) # value 2 is stored as argument of outer_function(a)
answer1 = z(4) # value 4 is passed as argument of inner_function (b) (z-is variable/object storing outer_function(a=2) ) 
print(answer1)

# Function returns another function - example 2
def outer_function(a, b, c):
    def inner_function(x):
        return a*x**2+b*x+c 
    return inner_function
z=outer_function(1,2,3) 
answer1 = z(4) # object z already stored values of (a,b,c) so we just pass argument d
print(answer1)

# Encapsulation of example above

def outer_function(a):
    def inner_function(b):
        return a+b 
    return inner_function

def repeatable_function (c):
    x = outer_function ("Hello ") # here we passing argument a = "Hello " to outer_function
    d = x(c) # argument c passed in as argument b of inner function
    print (d)
print (repeatable_function ("World"))

# add attribute to the existing function using decorator - "encapsulation" (without rewriting source function)

# let's assume that we want to add  parameter c = 1 into add function using function decorator:


def source_function (a,b): #source function which we don't want to modify
    return a+b+source_function.c # +source_function.c - our modification

def my_func (function):
    function.c = 1
    return source_function

my_func (source_function) # we have to pass source_function as argument to my_func and call it

print (source_function (5,4)) # source_function with pre-set c = 1

# validate function's input parameters through encapsullation/decoration:

def outer_function(a):
    validate_a = "Hello "# create condition that a just == "Hello "
    if a != validate_a:
        a = validate_a
    def inner_function(b):
        validate_b = "World"
        if b != validate_b:
            b = validate_b
        return a+b 
    return inner_function

def repeatable_function (c):
    x = outer_function (c) # here we passing argument a = "Hello " to outer_function
    d = x(c) # argument c passed in as argument b of inner function
    print (d)
repeatable_function ("Hi!")

###DICTIONARIES####

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print (stocks.get('MSFT.US').get('Microsoft Corp'))

#or alternative

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks['MSFT.US']['Microsoft Corp'])

#update value by key
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks ['MSFT.US']['Microsoft Corp'] = 190
print (stocks ['MSFT.US'])

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks['V.US']={'Visa Inc': 185}
print (stocks.values())

tickers = ['AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
        'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
        'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
    ]
print(list(enumerate(tickers)))

# enumerate list and transform list to a dictionary
tickers = ['AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
           'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
           'GS.US', 'HD.US', 'IBM.US', 'INTC.US']
d = {k:v for (k,v) in enumerate(tickers)}
print(d)

#get unique sorted values

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
list = sorted(set(project_ids.values()))
print(list)

# remove value by key
stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
del(stats["traffic"])
print (stats)

# get value by key. If key doesn't exist - predefine value as "indefinite"
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
print(users.get('004', 'indefinite'))

### METACLASS ###

class inherit: #class to be inherited
    def func(self):
        print("I am the inherited method")
        
def metafunc (): #external function that we want to include into metaclass
    print ("I am the metaclass function")

#create metaclass:
#type("class name", (class to inherit), dict(attributes outside inherited class: name, metafunction*))
#*if needs to be called automatically, specify with (): metafunction= metafunc()
"""
metaobject = type('meta', (inherit, ), dict(name="my_own", metafunction= metafunc))

b=metaobject()#instanciate object of class "meta"

print(b)#returns specified above class name "meta"
"""

number = 1.0
if isinstance(number, int):
    print("YES")
else: print("NO")


item = '001'
items = ['001', '000', '003', '005', '006']
     
if item in items:
   items.remove(item)
print(items)

result = []
for i in range(10, 100):
    if i % 11 == 0:
       result.append(str(i))
print(','.join(result))     

numbers=[]
for n in range(10,100,1):
    if n%11==0 and n%3 !=0:
        numbers.append(str(n))
print(",".join(numbers)) 

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
odds = []
for i in items:
    if not i%2 !=0:
        odds.append(i)
print(odds)

items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
     
for item in items:
    if not item in result:            
        result.append(item)
print(result)

#split to a list, convert to lower and get first 4 elements
text = 'Python is a very popular programming language'
list = text.split()
new_list=[]
for w in list[0:4]:
    new_list.append(w.lower())
print(new_list)

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
values =[]
for i in probabilities:
    if i<.5:
        values.append(0)
    else:values.append(1)
print(values)

#count the number of occurrences and present as dictionary
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
distinct = set(items)
hist_dict= {}
for i in distinct:
    hist_dict[i]=items.count(i)
print(hist_dict)

#standardize, remove punctuation and print according to criteria
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""
string =text.lower().replace(".", "").replace(",", "")
list = string.split()
output=[]
for word in list:
    if word.isalpha() and len(word)>6:
        output.append(word)      
print(output)

#print if string contains string
indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]
for w in indexes:
    if ("DOW" in w) | ("S&P" in w):
        print(w)
        
# iterate through dictionary.items()
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for ticker, close in gaming.items():
    if close > 100.0:
        print(ticker)

#check if name contains just letters
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalpha():
        print(f'Hello {name}!')
        
###RANDOM MODULE###

#generate random sample of 3 elements from a list 

import random

list = ["a", "b", "c", "d", "e", "f"]

new_sample = random.sample(list, 3)
print(new_sample)

# pick random single value from a list:

list = ["a", "b", "c", "d", "e", "f"]

x = random.choice(list)

# pick random multiple random values from a list:

list = ["a", "b", "c", "d", "e", "f"]

x = random.choices(list, k =2)
print (x)

# generate random integers within a range

x = random.randint(-3,4) # -3, 4 included
print (x)

# generate random integers within a range (-3,4) #4 - not included!

x = random.randrange(-3,4)
print (x)

# Random - the same all time, until parameter seed is changed

x = random.seed(2)
print (x)

# Random - new call = new value

y = random.random()
print(y)

##BREAK###

#Break and return True if any match. Otherwise return False
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False
 
for item1 in list1:
    if item1 in list2:
        result = True
        print(result)
        break

#avoid printing each iteration    
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
d_type = True
for i in hashtags:
    if type(i)!=str():
        d_type = False
        break
print (d_type)

#for loop, continue
"""!!! while iterating dictionary use conventional item names: 
    for key in dict:
        for value in dict.values():
            for key,value in dict.items():"""
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
for key in gaming:
    if gaming[key][1] =='PLN':
        continue
    else:gaming[key]=[gaming[key][0]*4,'PLN']
print(gaming)

names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for i in names:
    if not isinstance(i, str): #remember, not str()
        continue
    else: print(i)

######################### while loop ####################################    

# minimum of function, derivativs, lambda     
max_iters = 10000 
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4
     
while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_prev - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1
     
print(f'A local minimum in point: {w_0:.2f}')

###
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None
     
while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
                end = mid - 1
     
if flag:
    print('Found')
else:
    print('Not found')
    

######################### Exception handling ##########################
  
#Use the try... except... to handle the ZeroDivisionError. In case of error
#print message: 'Division by zero.'

sum = 3000
counter = 0
 
try:
    result = sum / counter
    print(result)
except ZeroDivisionError:
    print('Division by zero.')

# When file doesn't exist the FileNotFoundError is raised

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found.')

# In case of a KeyError, print to the console the following message:
# 'The 004 key is not in the dictionary. Adding key ...'
# Then add this key to the dictionary with the value None and print the dictionary.

users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'
 
try:
    print(users[user_id])
except KeyError:
    print(f'The {user_id} key is not in the dictionary. Adding key ...')
    users[user_id] = None
print(users)
    
####################### Reading files ###################################

# Transform the content of the file to get a dictionary containing two keys: 'Date' and 'Close'

#   with open('playway.csv', 'r') as file:
#       content = file.read().splitlines()
content = ['Date,Open,High,Low,Close,Volume',
     '2020-03-02,305,324.5,283.5,310,64081',
     '2020-03-03,325.5,340.5,320,340.5,55496',
     '2020-03-04,324,340.5,315,330,36152',
     '2020-03-05,344,344,310,315,35992',
     '2020-03-06,306.5,307,291,305,32539',
     '2020-03-09,274,291,250,258,79402',
     '2020-03-10,278,284.5,256,264,35700',
     '2020-03-11,270,270,238.5,245,60445',
     '2020-03-12,218,228,196,197,94031',
     '2020-03-13,210,229,198.8,211,100412',
     '2020-03-16,205,248,197.8,240.5,50659',
     '2020-03-17,245,269,232.5,264,99480',
     '2020-03-18,264,280,251,270,70136',
     '2020-03-19,267,280,267,279.5,30732',
     '2020-03-20,297.5,307,280,280.5,43426',
     '2020-03-23,274,289,258,285,37098',
     '2020-03-24,305,309,296.5,309,31939',
     '2020-03-25,313,330,295,304,46724',
     '2020-03-26,300,309,295.5,300,27213',
     '2020-03-27,302,306.5,290,296,13466',
     '2020-03-30,299,300,287,300,10316',
     '2020-03-31,302.5,309,302,306.5,15698']

data = [
    (line.split(',')[0], line.split(',')[4]) for line in content
]

print (data)
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [
        float(data[1:][i][1]) for i in range(len(data) - 1)
    ],
}
print(result)

# Find the highest volume for a given month and print the result

#with open('playway.csv', 'r') as file:
#    content = file.read().splitlines()

content = ['Date,Open,High,Low,Close,Volume',
     '2020-03-02,305,324.5,283.5,310,64081',
     '2020-03-03,325.5,340.5,320,340.5,55496',
     '2020-03-04,324,340.5,315,330,36152',
     '2020-03-05,344,344,310,315,35992',
     '2020-03-06,306.5,307,291,305,32539',
     '2020-03-09,274,291,250,258,79402',
     '2020-03-10,278,284.5,256,264,35700',
     '2020-03-11,270,270,238.5,245,60445',
     '2020-03-12,218,228,196,197,94031',
     '2020-03-13,210,229,198.8,211,100412',
     '2020-03-16,205,248,197.8,240.5,50659',
     '2020-03-17,245,269,232.5,264,99480',
     '2020-03-18,264,280,251,270,70136',
     '2020-03-19,267,280,267,279.5,30732',
     '2020-03-20,297.5,307,280,280.5,43426',
     '2020-03-23,274,289,258,285,37098',
     '2020-03-24,305,309,296.5,309,31939',
     '2020-03-25,313,330,295,304,46724',
     '2020-03-26,300,309,295.5,300,27213',
     '2020-03-27,302,306.5,290,296,13466',
     '2020-03-30,299,300,287,300,10316',
     '2020-03-31,302.5,309,302,306.5,15698']
    
print(f'Max Vol: {max([int(volume.split(",")[-1]) for volume in content[1:]])}')

# Find the day with the highest volume value for the given month

#with open('playway.csv', 'r') as file:
#    content = file.read().splitlines()
content= ['Date,Open,High,Low,Close,Volume',
     '2020-03-02,305,324.5,283.5,310,64081',
     '2020-03-03,325.5,340.5,320,340.5,55496',
     '2020-03-04,324,340.5,315,330,36152',
     '2020-03-05,344,344,310,315,35992',
     '2020-03-06,306.5,307,291,305,32539',
     '2020-03-09,274,291,250,258,79402',
     '2020-03-10,278,284.5,256,264,35700',
     '2020-03-11,270,270,238.5,245,60445',
     '2020-03-12,218,228,196,197,94031',
     '2020-03-13,210,229,198.8,211,100412',
     '2020-03-16,205,248,197.8,240.5,50659',
     '2020-03-17,245,269,232.5,264,99480',
     '2020-03-18,264,280,251,270,70136',
     '2020-03-19,267,280,267,279.5,30732',
     '2020-03-20,297.5,307,280,280.5,43426',
     '2020-03-23,274,289,258,285,37098',
     '2020-03-24,305,309,296.5,309,31939',
     '2020-03-25,313,330,295,304,46724',
     '2020-03-26,300,309,295.5,300,27213',
     '2020-03-27,302,306.5,290,296,13466',
     '2020-03-30,299,300,287,300,10316',
     '2020-03-31,302.5,309,302,306.5,15698']

data_dict = {key:value for key, value in zip([date.split(",")[0] for date in content[1:]],
                                             [value.split(",")[-1] for value in content [1:]]) }

# now get dict key by the value

for key, value in data_dict.items():
    if int(value) == max([int(i) for i in data_dict.values()]):
        print(f'Date: {key}')

#################### Saving to file ###################################

# Generate all even numbers from 2 to 18 inclusive. 
#Then write each number on a separate line to the file called num.txt.

numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]
 
with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')
        
# save to stocks.json using the json package. Set the indent to 4.
# (indent specifies the spaces at the beginning of a line)

import json
 
stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
 
with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)
    
# Save the above data to the users.csv

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
 
with open('users.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')

    
# yield function: 
## used when next output should be returned with next call of function 

#Example of problem: "a", "b", "c" has to be returned with each call of function, but return statement doesn't work:
def x():
    return "a" # just 1st return statement is executed (function can have just 1 return)
    return "b" 
    return "c"
y = x()
for i in range (3):
    print (y)
    
#To fix the problem above yield statement should be used instead (+.__next__):
def x():
    yield "a" # just 1st return statement is executed (function can have just 1 return)
    yield "b" 
    yield "c"
y = x()
for i in range (3):
    print (y.__next__())# __next__ is build-in method to generate next value



"""create a function that increments number of calls received 
with each "yes" answer submitted (as input). Set time limit"""

""" problem with input function in spyder - try in jupyter
import time

def calls_received (received = None):
    a=0
    while True:
        if received =="yes":
            a = a+1
            received= yield a
        else: received= yield a
rec=calls_received()
rec.__next__() #!!!generating next call of the function

stoppage_time = time.time()+5*60 # set time limit 
while time.time()<stoppage_time:
    ans = input("did you receive a call? (type yes/no and press Enter)")
    print(str(rec.send(ans))) #use .send() to send output of input function into rec
    """

#iterate the string in reverse order:
def reverse(str):
    for i in range (len(str)-1,-1,-1): #used for reverse iteration
        yield str[i]
        
for char in reverse("Python"):
    print (char)
    
###GENERATORS###

""" IDE ERROR - list () doesn't work
#define generator that return just .txt files

fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
def file_gen(fnames):
    for i in fnames:
        if i.endswith(".txt"):
            yield i

a = file_gen(fnames)
print (list(a)) # works good in jupyter

"""

""" IDE ERROR - list () doesn't work
list1= ["TEN","CDR","BBT"]
def enum(list1):
    idx=0
    for i in list1:
        yield (idx, i)
        idx = idx+1
 
print(list(enum(list1)))
"""

""" IDE ERROR - list () doesn't work
#create genarator to return previous, current and next day by index (0 - "Mon")
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7] #condition: not grater than 6
        
print (list(dayname(0)))
"""

###SET COMPREHENSION####

#count the probability of getting >10 (2 dices)
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f'Probability: {len(sum_gt_10) / len(omega):.2f}')

desc = "Playway: Playway is a producer of computer games."
desc = desc.lower().replace(":", "").replace(".","")
print (len(set(desc.split())))

#count the probability of getting >45 (2 dice)
omega = {(f,j) for f in range (1,7) for j in range (1,7)}
get_45 = {pair for pair in omega if pair[0]**2+pair[1]**2>=45}
print(f'Probability: {len(get_45)/len(omega):.2f}')

#count the probability of getting sum divisible by 7 (3 dices)
omega = {(k,l,m) for k in range (1,7) 
         for l in range (1,7)
         for m in range (1,7)}
get_div_by_7= {pair for pair in omega if (pair[0]+pair[1]+pair[2])%7==0}
print(f'Probability: {len(get_div_by_7)/len(omega):.2f}')

#count the probability of getting sum of squares divisible by 3 (3 dices)
omega = {(k,l,m) for k in range (1,7) 
         for l in range (1,7)
         for m in range (1,7)}
get_div_by_7= {pair for pair in omega 
               if (pair[0]**2+pair[1]**2+pair[2]**2)%3==0}
print(f'Probability: {len(get_div_by_7)/len(omega):.4f}')

#probability of getting odd number if dice is thrown 3 times
omega = {(x, y, z) for x in range(1, 7) 
         for y in range(1, 7) 
         for z in range(1, 7)}
a = {(x, y, z) for x, y, z in omega if x % 2 != 0 
     and y % 2 != 0 and z % 2 != 0}
prob = round(len(a) / len(omega), 4)
print(f'Probability: {prob}')

### LIST COMPREHENSION ###
"""
#clean new line characters and get just not empty lines (missing .txt file for this example)
with open('gaming.txt','r') as file:
    text = file.readlines()
new_list = [i.replace("\n", "") for i in text]
clean_list = [line for line in new_list if len(line)>0]
print(clean_list)
"""
#calculate gross price
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price = [round(net*(1+tax), 2) for net in net_price]
print (gross_price)

#calculate future value of investments
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fv = [round(pv*(1+r)**n, 2) for r in rate]
print (fv)

#calculate the interests received
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

interests = [round(pv*(1+r)**n-pv, 2) for r in rate]
print (interests)

""" missing textfile

with open('plw.txt', 'r') as file:
    lines = file.read()
new_list= [lines.lower().replace(",", "").replace(".","").split()]
output = sorted([word for word in new_list[0] if len(word)>=8])
print (output)

"""
### DICT COMPREHENSION ###
"""
#error calling dict in spyder IDE.
#convert dict into list
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
result = [[key, val] for key, val in data.items()]
print(result)
"""

#create dictionary where i:i**2
list1 = list(range(1,8,1))
output=dict(zip(list1,[i**2 for i in list1]))
print(output)

#alternativ and more efficient sollution
result = {i:i**2 for i in range(1, 8)}
print(result)

stocks = ['Playway', 'CD Projekt', 'Boombit']

output={i:len(i) for i in stocks}
print (output)

#replace keys and values
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
output= {v:k for k,v in stocks.items()}
print(output)

stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:val for key, val in stocks.items() if val > 100}
print(result)

#nested comprehension!!!
data = [{i: i**j for i in range(1, 10)} for j in range(1, 4)]
print(data)

properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']

output = {k:{k1:None for k1 in properties } for k in indeks}
print(output)

index = ['WIG20', 'mWIG40', 'sWIG80']

output = {k:v for k, v in enumerate(index)}
print(output)

import os
path = os.getcwd()
print (path)

###SQLLite3####
import sqlite3

#sqlite3.connect('student_records.db') looks for existing db and creats
#new if doesn't exist
#use exeptions to try if creation/connection succeded 
try: 
    dbase = sqlite3.connect('student_records.db')
    print ("Connection Successful")
    dbase.close()
except:
    print("Connection Error")
    
#create table in existing db (start with connection)

try: 
    dbase = sqlite3.connect('student_records.db')
    dbase.execute('''CREATE TABLE students (ID INT PRIMARY KEY NOT NULL,
                  NAMES TEXT NOT NULL, 
                  MARKS TEXT NOT NULL, 
                  GRADES TEXT NOT NULL)''')#structure of SQL Query
    print ("Connection Successful")
    dbase.close()
except:
    print("Connection Error")
    
#insert data into DB. Start with connection
'''this command returns an error if applied twice (according to PRIMARY
KEY constraint can't add record with same ID)

connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(2, "Peter", "95", "A"))
connection.commit()#apply changes
connection.close()
'''

'''
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(3, "Ola", "86", "B"))
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(4, "Mary", "60", "C"))
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(5, "Tom", "50", "D"))
connection.commit()#apply changes
connection.close()
'''

#select from database

db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT NAMES, GRADES FROM students"""
cursor.execute(query)
Names_of_students = cursor.fetchall()
for names,grades in Names_of_students:
    print (names,grades)


# select all from table
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT * FROM students"""
cursor.execute(query)
Names_of_students = cursor.fetchone()#get row
while True:
    row = cursor.fetchone()
    if row ==None:
        break
    print (row)
    
#Order by
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT NAMES FROM students ORDER BY NAMES DESC"""
cursor.execute(query)
Names_of_students = cursor.fetchall()
for row in Names_of_students:
    print (row)
    
#SELECT DISTINCT with condition (WHERE)
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT DISTINCT * FROM students WHERE GRADES=='B' 
OR GRADES=='C'"""
cursor.execute(query)
print (cursor.fetchall()) # get list containing results

#limit output starting from row nr 2 (OFFSET 2)
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT DISTINCT * FROM students LIMIT 3 OFFSET 2"""
cursor.execute(query)
print (cursor.fetchall()) # get list containing results

# IN (NOT IN)

db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT * FROM students WHERE ID IN (1,2)"""
cursor.execute(query)
print (cursor.fetchall()) # get list containing results

#Text pattern matching (LIKE is not case sensitive!)
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT NAMES FROM students WHERE NAMES LIKE 'a%' """
cursor.execute(query)
print (cursor.fetchall())

query = """SELECT NAMES FROM students WHERE NAMES LIKE '%et%' """
cursor.execute(query)
print (cursor.fetchall())

#Text pattern matching (GLOB is case sensitive with own syntax!)
#Check GLOB rules and syntax for more info
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT NAMES FROM students WHERE NAMES GLOB '?l*'
OR NAMES GLOB 'A*' """ 
cursor.execute(query)
print (cursor.fetchall())

#AGGREGATE FUNCTIONS: AVG(), COUNT(), MAX()

db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT AVG (MARKS) FROM students WHERE ID <5""" 
cursor.execute(query)
print (cursor.fetchall())

db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT COUNT (*) FROM students WHERE ID <5""" 
cursor.execute(query)
print (cursor.fetchall())


db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT COUNT (DISTINCT MARKS) FROM students WHERE ID <4""" 
cursor.execute(query)
print (cursor.fetchall())

db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT COUNT (DISTINCT MARKS) FROM students WHERE ID <4""" 
cursor.execute(query)
print (cursor.fetchall())

#MAX() doesn't work on TEXT columns (returns wrong result if MAX (MARKS))
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT MAX (ID) FROM students""" 
cursor.execute(query)
print (cursor.fetchall())

#add new records to a table

'''
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(8, "John", "88", "B"))
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(9, "Philip", "60", "C"))
cursor.execute("""INSERT INTO students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(10, "Tim", "55", "D"))
connection.commit()#apply changes
connection.close()
'''

#Update multiple values in a table (UPDATE Students SET )
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
query = """UPDATE students SET MARKS = "89", GRADES="B" WHERE ID=3"""
cursor.execute(query)

connection.commit()#apply changes
connection.close()

#DELETE record
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
query = """DELETE FROM students WHERE ID=9"""
cursor.execute(query)

connection.commit()#apply changes
connection.close()

###for section of UNION, INTERSECT new table will be created:

#create table in existing db (start with connection)

"""
try: 
    connection = sqlite3.connect('student_records.db')
    dbase.execute('''CREATE TABLE new_students (ID INT PRIMARY KEY NOT NULL,
                  NAMES TEXT NOT NULL, 
                  MARKS TEXT NOT NULL, 
                  GRADES TEXT NOT NULL)''')#structure of SQL Query
    print ("Connection Successful")
    dbase.close()
except:
    print("Connection Error")
"""

'''
#add records to new table    
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""INSERT INTO new_students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(21, "George", "85", "B"))
cursor.execute("""INSERT INTO new_students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(22, "Linda", "60", "C"))
cursor.execute("""INSERT INTO new_students (ID, NAMES, MARKS,GRADES)
                   VALUES (?,?,?,?)""",(23, "Amanda", "95", "A"))
connection.commit()#apply changes
connection.close()
'''

#UNION : unique elements from both tables
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""SELECT NAMES FROM students UNION SELECT 
               NAMES FROM new_students""")

print (cursor.fetchall())

#INTERSECT : common elements for both tables
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
cursor.execute("""SELECT NAMES FROM students INTERSECT SELECT 
               NAMES FROM new_students""") #no common

print (cursor.fetchall())

#ALTER TABLE - rename table
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
query = """ALTER TABLE new_students RENAME TO students_new"""
cursor.execute(query)

connection.commit()#apply changes
connection.close()

#ALTER TABLE - add column
connection = sqlite3.connect('student_records.db')
cursor= connection.cursor()#command to make changes to db
query = """ALTER TABLE students_new ADD COLUMN AGE INT"""
cursor.execute(query)

connection.commit()#apply changes
connection.close()

#String Functions (in SQL 1st element has position 1)
#see more in SQL course
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT NAMES, SUBSTR (NAMES,2,3 ) FROM students"""#from NAMES
#starting at index 2 length 3 
cursor.execute(query)
print (cursor.fetchall())

#Negative string iteration
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT SUBSTR (NAMES,-1,4 ) FROM students"""#from NAMES
#starting at last index for 2 backward
cursor.execute(query)
print (cursor.fetchall())

#INSTR returns index of string
db = sqlite3.connect('student_records.db')
cursor= db.cursor()
query = """SELECT INSTR (NAMES,'o') FROM students"""#from NAMES
#starting at last index for 2 backward
cursor.execute(query)
print (cursor.fetchall())

###BUILT-IN PACKAGES###

#year calendar
import calendar
print (calendar.calendar(2023))

#month calendar
import calendar
print (calendar.month(2023,6))

#difference between dates

from datetime import date
     
date1 = date(2020, 6, 1)
date2 = date(2020, 7, 18)
diff = date2 - date1
print(diff)

#regular expressions

import re

string = 'Python 3.8'
print(re.findall('\d', string))

#get emails from string
import re
     
raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)

#Counter class
from collections import Counter
     
counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)

import math
     
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

#pick item randomly
import random

random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
print (random.choice(items))

#shuffle list

import random

random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']
random.shuffle(items)
print(items)

#save data to a pickle file
import pickle
     
ids = ['001', '003', '011']
     
with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)

#dump .JSON into string with indent 4 sorted by keys

import json

stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}

new_string = json.dumps(stocks, indent=4, sort_keys=True)
print (new_string)

#calculate accuracy
y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]
     
def accuracy(y_true, y_pred):
    counter = 0
    for i, j in zip(y_true, y_pred):
        if i == j:
            counter += 1
    return round(counter / len(y_true), 4)
     
print(accuracy(y_true, y_pred))

#implement Mean Absolute Error function
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
def mae(y_true, y_pred):
    count = 0
    total = 0
    for i in zip (y_true,y_pred):
        total=total+abs(i[1]-i[0])
        count = count+1
    return round(total/count, 3)
print(mae(y_true, y_pred))

#better solution
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
def mae(y_true, y_pred):
    return round(sum( [abs(i[1] - i[0]) for i in zip(y_true, y_pred)] ) 
                 /len(y_true), 3)
print(mae(y_true, y_pred))
        
# def Mean Squared Error (MSE) function
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
def mse(y_true, y_pred):
    return round(sum( [abs(i[1] - i[0])**2 for i in zip(y_true, y_pred)] ) / 
                 len(y_true), 3)
print(mse(y_true, y_pred))

#create a function that moves 0 to the end
items = [3,4,0,2,0,5,1,6,2]
def transfer_zeros(items):
    list1 = []
    list2 = []
    for i in items:
        if i != 0:
            list1.append(i)
        else: list2.append(i)
    for j in list2:
        list1.append(j)
    return list1
print(transfer_zeros(items))

#Eucledian Distance

x = [0,3]
y=[4,0]

def euclidean_distance(x, y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5
print (euclidean_distance(x, y))

def arange(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result
print (arange (0,10))

### OOP ###

# display the namecpace of the class (use __dict__)
import uuid

class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

for name in Product.__dict__:
    print (name)
print (Product.__dict__) 

# display the namecpace of the class instance (use __dict__)
import uuid

class Product:

    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"


product = Product('Mobile Phone', '54274', 2900)

print(product.__dict__)

#look through the names of arguments of a function
def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'
     
     
print(stock_info.__code__.co_varnames)

import builtins
      
help(builtins.sum)
print(builtins.sum([-4, 3, 2]))

#set correct scope of variable
counter = 1

def update_counter():
    global counter
    counter += 1
    print(counter)
    
update_counter()

#call function 40 times - function in list comprehension !!!
counter = 0
dot_counter = ''
     
def update_counter():
    global counter, dot_counter
    counter += 1
    dot_counter += '.'
     
[update_counter() for _ in range(40)]
print(counter)
print(dot_counter)

#nonlocal variables
def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''

    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'
    
    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)
    
display_info(10)


#* args implement function that takes any number of arguments 
#but uses some of them
def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = '#'.join(args)
    return result
     
print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))

# **kwargs  - keyword arguments (key,value pairs)
def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")
     
display_info(company='CD Projekt', price=100)

### Classes  - basic ###

#add documentation to the class

class Vehicle:
    """This is a Vehicle class."""
    
#display class name attribute
class Vehicle:
    """This is a Vehicle class."""
    
print (Vehicle.__name__)

#display all dict attribute keys
class Container:
    """This is a Container class."""

Container.__dict__.keys()

#display the value of module attribute

class Container:
    """This is a Container class."""
    
print(Container.__module__)

#create an instance
class Container:
    """This is a Container class."""
    
container = Container()
print(type(container))

#value of the class attribute of the instance

class Container:
    """This is a Container class."""
    
container = Container()
print(container.__class__)

#check isinstance
class Model:
    pass

model = Model()
print(isinstance(model, Model))

#check if object is an instance of one ofte two classes created
class Model:
    pass


class View:
    pass


object1 = Model()
object2 = [Model(), Model()]
object3 = {}

print(isinstance(object1, (Model,View)))
print(isinstance(object2, (Model,View)))
print(isinstance(object3, (Model,View)))

#check if class issubclass:    
class Model:
    pass

class View:
    pass

print(issubclass(Model, object))
print(issubclass(View, object))

### class attributes ###

#print the values of class attributes
class Phone:
    brand = "Apple"
    model = "iPhone X"
    
print(getattr(Phone, "brand"))
print(getattr(Phone, "model"))

#change values of class attributes:
class Phone:
    brand = 'Apple'
    model = 'iPhone X'
    
Phone.brand = 'Samsung'
Phone.model='Galaxy'

print(f'brand: {Phone.brand}')
print(f'model: {Phone.model}')

#change class attributes using setattr function
class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'
    
setattr(Laptop, "brand", "Acer")
setattr(Laptop, "model", "Predator")

print(f'brand: {Laptop.brand}')
print(f'model: {Laptop.model}')

#set class attributes and print all user-defined attribites' names

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
OnlineShop.country = 'USA'

print([attr for attr in OnlineShop.__dict__.keys() 
       if not attr.startswith("_") ])

#delete class attribute and print the rest

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
del OnlineShop.sector_code
print([attr for attr in OnlineShop.__dict__.keys() 
       if not attr.startswith("_")])

#alternative

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
delattr(OnlineShop, "sector_code")
print([attr for attr in OnlineShop.__dict__.keys() 
       if not attr.startswith("_")])

#get user-defined attribute names with their values:
class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
     
for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

# alternative with creating function:
    
class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

def describe_attrs():     
    for attr, value in OnlineShop.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')
            
describe_attrs()

#define a function as class attribute that returns class attribute value

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False
    
    def get_sector():
        return OnlineShop.sector

#implement another function as a class method
class HouseProject:
    number_of_floors = 3
    area = 100
    
    def describe_project():
        print(f'Floor number: {HouseProject.number_of_floors}\nArea: {HouseProject.area}')
        
HouseProject.describe_project()

### Instance Attributes ###

#add istance attributes
class Book:
    language = 'ENG'
    is_ebook = True
    
book = Book()
print(book.__dict__)

book.author = 'Dan Brown'
book.title = 'Inferno'
print(book.__dict__)
    
#display instance attributes according to given pattern
class Book:
    language = 'ENG'
    is_ebook = True

book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]
for i in books:
    for key,value in i.__dict__.items():
        print (key,"->",value)
    print (30*"-")
    
#alternative

class Book:
    language = 'ENG'
    is_ebook = True

book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]
for book in books:
    for attr in book.__dict__:
        print(f'{attr} -> {getattr(book, attr)}')
    print('-' * 30)
 
#set attributes from a list to an instance

class Book:
    language = 'ENG'
    is_ebook = True

books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003,
    },
]

book_1=Book()
book_2=Book()

for name,value in books_data[0].items():
    setattr(book_1, name, value)
for name,value in books_data[1].items():
    setattr(book_2, name, value)
    
    
print(book_1.__dict__)
print(book_2.__dict__)

#better solution
class Book:
    language = 'ENG'
    is_ebook = True
     
     
books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {
     'author': 'Dan Brown',
     'title': 'The Da Vinci Code',
     'year_of_publishment': 2003,
        },
    ]
     
books = []
for book_data in books_data:
    book = Book()
    for attr, value in book_data.items():
        setattr(book, attr, value)
    books.append(book)
     
for book in books:
    print(book.__dict__)
    
#implement a method to the class instance

class Book:
    language = 'ENG'
    is_ebook = True
    
    def set_title(self, title):
        self.title = title
        
book=Book()
book.set_title("Inferno")
print(book.title)

#set method above with VALIDATION
class Book:
    language = 'ENG'
    is_ebook = True
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError('The value of the title attribute must be of str type.')
        else: self.title = title  
        
book=Book()
book.set_title(123)
print(book.title)

#use exceptional handling for Error - print error message
class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError('The value of the title attribute must be of str '
                'type.')
        self.title = value
        
book = Book()

try:
    book.set_title(False)
except TypeError as error: #remember syntax !!!
    print(error)
    
### __init__()###

#implement class and method that displays name attributes

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def display_instance_atts(self):
        for name in self.__dict__:
            print(name)
            
laptop=Laptop("Dell", "Inspiron", 3699)

laptop.display_instance_atts()

# example above but method displays both names and values of attributes
class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def display_atts_with_values(self):
        for name,value in self.__dict__.items():
            print(name,"->",value)
            
laptop=Laptop("Dell", "Inspiron", 3699)

laptop.display_atts_with_values()
        
#better alternative
class Laptop:
 
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
 
    def display_attrs_with_values(self):
        for attr in self.__dict__.keys():
            print(f'{attr} -> {getattr(self, attr)}')
            
laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_attrs_with_values()

#implement the Vector class that takes any number of args with property
class Vector:
    def __init__(self, *components):
        self.components = components
        
v1 = Vector(1,2)
v2 = Vector (4,5,2)

print("v1 ->",v1.components)
print("v2 ->",v2.components)

#implement the Vector class that takes any number of kwargs with property
class Bucket:
        
    def __init__(self, **kwargs):
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)
     
bucket = Bucket(apple=3.5, milk=2.5, juice=4.9, water=2.5)
print(bucket.__dict__)

#set default value of the attribute
class Car:
    def __init__(self, brand,model,price,type_of_car='sedan'):
        self.brand=brand
        self.model=model
        self.price=price
        self.type_of_car=type_of_car
        
car=Car('Opel','Insignia',115000)
print(car.__dict__)

car=Car('Opel','Insignia',115000, 'SUV')
print(car.__dict__)

#attributes value validation
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model=model
        if not isinstance(price, (int,float))| price>0:
            raise TypeError('The price attribute must be a positive int or float.') 
        self.price=price
        
laptop=Laptop("Acer","Predator", 5490)

print(laptop.__dict__)

#use exceptional handling in case of error
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )

try:
    laptop=Laptop("Acer","Predator","5900")
except TypeError as error:
    print (error)
    
### bare, _protected and ___private attributes ###

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price=price
        
laptop = Laptop("Acer", "Predator", 5490)
print (laptop.__dict__)

#print attributes and their values:
class Laptop:
     
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
     
     
laptop = Laptop('Acer', 'Predator', 5490)
print(f'brand -> {laptop.brand}')
print(f'model -> {laptop._model}')
print(f'price -> {laptop._Laptop__price}')

#implement the method that displays all the private attributes of the instance
class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
    
    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)    
                
laptop = Laptop ("Acer", "Predator", "AC-100", 5490, 0.2)
laptop.display_private_attrs()

#implement the method that displays all the protected attributes of the instance
class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
    
    def display_protected_attrs(self):
        for attr in self.__dict__:
            if attr.startswith("_") and f'{self.__class__.__name__}' not in attr:
                print(attr)    
                
laptop = Laptop ("Acer", "Predator", "AC-100", 5490, 0.2)
laptop.display_protected_attrs()

### Encapsulation ###

#implement methods for setting end getting price of instance
class Laptop:
    def __init__(self, price):
        self._price = price
        
    def get_price(self):
        print(self._price)
        
    def set_price(self, new_price):
        self._price=new_price
        
laptop = Laptop(3499)
laptop.get_price()
laptop.set_price(3999)
laptop.get_price()

# implement class with methods with validation check
class Laptop:
    def __init__(self, price):
        self._price = price
    
    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError (
                'The price attribute must be an int or float type.')
        elif not price >0:
            raise ValueError (
                'The price attribute must be a positive int or float value.')
        else:
            self._price = price

    def get_price(self):
        return self._price
    
laptop=Laptop(3499)

try: 
    laptop.set_price('-3000')
except TypeError as error:
    print (error)
    
# alternative syntax to example above (new value is set also)
class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or '
                'float value.')
        
        self._price = value
        
laptop = Laptop (3499)
try:
    laptop.set_price(-3000)
except ValueError as error:
    print (error)
    
# implement validation also into __init__ method:
class Laptop:

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or '
                'float value.')
        self._price = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or '
                'float value.')
        
        self._price = value
        
try:
    laptop = Laptop(-3499)
except ValueError as error:
    print(error)
    
# implement class property (using property function)

class Person:
    def __init__(self, first_name):
        self._first_name=first_name
     
    def get_first_name(self):
        return self._first_name
         
    first_name = property(fget=get_first_name)

person = Person("John")
print(person.first_name)

# create a property that reads and modifies
class Person:
    def __init__(self, first_name):
        self._first_name = first_name
        
    def get_first_name(self):
        return self._first_name
        
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
        
    first_name = property(fget=get_first_name, fset= set_first_name)
    
person = Person ("John")
person.set_first_name("Mike")

print(person.first_name)

# create a property that reads and modifies
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    def get_first_name(self):
        return self._first_name
        
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name
        
    def get_last_name(self):
        return self._last_name
        
    def set_last_name(self, new_last_name):
        self._last_name = new_last_name
    
    first_name = property(fget=get_first_name, fset= set_first_name)
    last_name = property(fget=get_last_name, fset= set_last_name)
    
person = Person ("John", "Dow")
print(person.first_name)
print(person.last_name)

person.first_name = "Tom"
person.last_name = "Smith"
print(person.__dict__)

#create a property that removes attribute

class Person:

    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value
        
    def del_first_name(self):
        del self._first_name
        
    first_name = property(fget=get_first_name, fset=set_first_name,
                          fdel=del_first_name)
    
person= Person("Tom")
person.del_first_name()
print (person.__dict__)

#many properties
class Pet:
    def __init__(self, name, age):
        self._name=name
        self._age = age
        
    @property
    def name (self):
        return self._name
    
    @property
    def age (self):
        return self._name

pet = Pet("Max", 5)
print(pet.__dict__)

#create a class with property to read and modify

### setter ###

class Pet:
    def __init__(self, name):
        self._name=name
        
    @property 
    def name (self):
        return self._name
    
    @name.setter
    def name (self, value):
        self._name = value
        
pet = Pet ("Max")
pet.name="Oscar"
print(pet.__dict__)


# setter 2 attributes
class Pet: 
    def __init__(self, name, age):
        self._name= name
        self._age = age
        
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name (self, new_name):
        self._name = new_name
        
    @property
    def age (self):
        return self._age
    
    @age.setter
    def age (self, new_age):
        self._age = new_age
        
pet = Pet ("Max", 5)
print (pet.__dict__)

pet.name = "Tom"
pet.age = 8

print (pet.__dict__)

# property setter with multiple validation:
    
class Pet:

    def __init__(self, name, age):
        self._name = name
        if type(age)!= int:
            raise TypeError ("The value of age must be of type int.")
        elif age <= 0:
            raise ValueError ("The value of age must be a positive integer.")
        else: self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value)!= int:
            raise TypeError ("The value of age must be of type int.")
        elif value <= 0:
            raise ValueError ("The value of age must be a positive integer.")
        else: self._age = value
        
try:
    pet = Pet ("Max", "seven")
except TypeError as error:
    print (error)
except ValueError as error:
    print (error)
    
# read, modify and delete properties

class TechStack:
    def __init__(self, tech_names):
        self._tech_names=tech_names
        
    @property
    def tech_names(self):
        return self._tech_names
    
    @tech_names.setter
    def tech_names (self, value):
        self._tech_names=value
        
    @tech_names.deleter
    def tech_names(self):
        del self._tech_names
        
tech_stack=TechStack("python,java,sql")
print(tech_stack.tech_names)

tech_stack.tech_names = "python,sql"
print(tech_stack.tech_names)

del tech_stack.tech_names
print(tech_stack.__dict__)

###! access modifiers - example of RecursionError: 
class Pet:


    def __init__(self, name, age):

        self._name = name

        self.age = age #### here we create public  attribute age


    @property

    def name(self):

        return self._name


    @name.setter

    def name(self, value):

        self._name = value


    @property

    def age(self):

        return self.age # function calls itself 
    # by returning self.age (has to be self._age)

    @age.setter

    def age(self, value):

        self._age = value
     

pet = Pet ("Max", 7)

print(pet.age)  

#make sure that property area is calculated just once or after 
#radius attribute is being modified
import math
        
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
     
    @property
    def radius(self):
        return self._radius
     
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None
     
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius **2
        return self._area
         
circle = Circle(3)
print(f'{circle.area:.4f}')

#area of rectangle calculated first time or after modifying width or height
class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height = height
        self._area = None #!!!must be protected
        
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width (self, value):
        self._width=value
        self._area = None# each time when width is set self._area is set to None
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height (self, value):
        self._height=value
        self._area = None# each time when height is set self._area is set to None
        
    @property
    def area (self):
        if self._area == None:
            self._area = self._width*self._height
        return self._area
        
rectangle = Rectangle(3,4)
print (f'width: {rectangle.width}, height: {rectangle.height} -> area: {rectangle.area}')

### Class methods ###
### method decorators:  using @classmethod

class Person:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
Person.show_details()

### method decorators: alternative class classmethod:
    
class Person:
    
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
    show_details = classmethod(show_details)
        
Person.show_details()

# call the class method from the instance
class Container:

    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
container=Container()
container.show_details()

# append class variable with each class instanciation
class Person:
    
    instances=[]
    
    def __init__(self):
        Person.instances.append(self)
        
    @classmethod
    def count_instances(cls):
        return len(cls.instances)
        
person1=Person()
person2=Person()
person3=Person()

print(Person.count_instances())

# extend example above with adding instance attributes-first and last name

class Person:

    instances = []

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        Person.instances.append((self.first_name, self.last_name))
    
    @classmethod
    def count_instances(cls):
        return len(Person.instances)
        
person1=Person("Ivan", "Petrov")
person2=Person("John", "Smith")

print(Person.count_instances())

### static methods

#Solution 1: using class staticmethod

import time

class Container:
    
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())
    
    get_current_time=staticmethod(get_current_time)
    
print(Container.get_current_time())

#Solution2 using method decorator @staticmethod

class Container:
    
    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())
    
print(Container.get_current_time())

# another @staticmethod example

import uuid

class Book:

    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

book1 = Book('Inferno', 'Dan Brown')
print(book1.__dict__.keys())

# add an instance method that represents a class instance

import uuid
          
class Book:
     
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author
     
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"        
     
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
     
     
book1 = Book('Inferno', 'Dan Brown')
print(book1)

###################### Special methods ###########################

# __repr__() modify the way of how instance is displayed
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"
        
person= Person("Mike", "Smith")
print(person)   

#__str__() another method to print str about instance (return (f''))
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"
    
    def __str__(self):
        return f'First name: {self.fname}\nLast name: {self.lname}'
        
person=Person("John", "Doe")
print(person)

#create __repr__() method of class instance
class Vector:
    def __init__(self, *args):
        self.components = args
        
    def __repr__(self):
        return (f'Vector{self.components}')# return, not print !!!
        
v1 =Vector (-3,4,2)
print(v1)

#  __str__() method for instance representation (return (f''))

class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'
        
    def __str__(self):
        return f'{self.components}' # return, not print
        
v1=Vector (-3,4,2)
print (v1)

# __len__() returns the number of arguments (while using len(object))

class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'
        
    def __len__(self):
        return len(self.components)
        
v1=Vector (-3,4,2)
print (len(v1))

#implement __bool__() gives False if 1st arg. !=0 (or not defined)
class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)
        
    def __bool__(self):
        if len (self.components) ==0:
            flag = False
        elif self.components[0]==0:
            flag = False
        else: flag = True
        return flag
        
v1 = Vector()
v2 = Vector(3,2)
v3 = Vector(0,-3, 2)
v4 = Vector(5,0,-1)

print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))

#more advanced solution. REMEMBER bool(0)==False
class Vector:
 
    def __init__(self, *components):
        self.components = components
 
    def __repr__(self):
        return f'Vector{self.components}'
 
    def __str__(self):
        return f'{self.components}'
 
    def __len__(self):
        return len(self.components)   
 
    def __bool__(self):
        if not self.components:
            return False
        return False if not self.components[0] else True  
 
 
v1 = Vector()
v2 = Vector(3, 2)
v3 = Vector(0, -3, 2)
v4 = Vector(5, 0, -1)
 
print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))

# use try ... except for eventuell error

class Vector:

    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)
        
v1 = Vector(4,2)
v2 = Vector (-1,3)

try:
    v1+v2
except TypeError as error:
    print (error)
    
# implement __add__() for Vector class (adding same dimention vectors)

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)

v1 = Vector(4, 2)
v2 = Vector(-1, 3)
print(v1 + v2)

# try...except

class Vector:

    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)
        
v1=Vector(4,2)
v2=Vector(-1,3)

try:
    v1-v2
except TypeError as error:
    print (error)

# implement special subtraction method __sub__() for Vector class

class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components) 

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)
        
    def __sub__(self, other):
        components = tuple(x-y for x,y in zip (self.components, other.components))
        return Vector(*components) #here important to use * 
        
v1=Vector (4,2)
v2=Vector(-1,3)
print (v1-v2)

# implement __mul__() for vectors multiplication
class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)     

    def __sub__(self, other):
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return Vector(*components)
        
    def __mul__(self, other):
        components = tuple(x*y for x, y in zip(self.components, other.components))
        return Vector(*components)
v1=Vector (4,2)
v2=Vector(-1,3)
print (v1*v2)  

# __truediv__() for vector division
class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)     

    def __sub__(self, other):
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return Vector(*components) 

    def __mul__(self, other):
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return Vector(*components)
        
    def __truediv__(self, other):
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return Vector(*components)

v1=Vector (4,2)
v2=Vector(-1,4)
print (v1/v2)  

# __floordiv__() for vector division

class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*components)     

    def __sub__(self, other):
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return Vector(*components) 

    def __mul__(self, other):
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return Vector(*components)
        
    def __truediv__(self, other):
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return Vector(*components)
    
    def __floordiv__(self, other):
        components = tuple(x //y for x, y in zip(self.components, other.components))
        return Vector(*components)

v1=Vector (4,2)
v2=Vector(-1,4)
print (v1//v2) 

#spec .method __add__() for strings
class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'
        
    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)
        
doc1= Doc("Python")
doc2= Doc("3.8")
print(doc1+doc2)

#quite similar example: concatenate strings
class Hashtag:

    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'
    
    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)

hashtag1 = Hashtag("python")
hashtag2 = Hashtag("developer")
hashtag3 = Hashtag("oop")

print(hashtag1+hashtag2+hashtag3)

#implement __eq__() method to compare attributes' values
class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)
    
    def __eq__(self, other):
        return self.string == other.string

doc1= Doc("Python")
doc2= Doc("3.8")
print(doc1==doc2)

# __lt__(): if 1 inst. is smaller (little, shorter)

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)
    
    def __lt__(self, other):
        return len(self.string) < len(other.string)

doc1= Doc("sport")
doc2= Doc("activity")
print(doc1<doc2)

# __iadd__() for extended assignment like i =i+1

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'
    
    def __iadd__(self, other):
        return Doc(self.string + ' & ' + other.string)
    
doc1= Doc("sport")
doc2= Doc("activity")
doc1+=doc2
print(doc1)

# __str__() method to display information representation

import uuid
  
class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author
 
    def __repr__(self):
        return (
            f"Book(title='{self.title}', author='{self.author}')"
        )
 
    def __str__(self):
        return (
            f'Book ID: {self.book_id} | Title: {self.title} | '
            f'Author: {self.author}'
        )
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
book = Book('The Lord of the Rings', 'J.R.R. Tolkien')
print(book)

########################### Inheritance ############################

#check if class is subclass
class Container:
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

class CustomContainer:
    pass

print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))

# MRO -method resolution order (order of inheritance)

class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class SmallPlasticContainer(PlasticContainer):
    pass

print(SmallPlasticContainer.mro())

### __repr__() for inheritance. Also get clas name of an instance
class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'
        
    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"
    
class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'   


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    print(instance)
    
# almost similar to example above
class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'
        
    def display_info(self):
        print(f'{self.__class__.__name__} -> {self.category}')

class LandVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'

vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for vehicle in vehicles:
    vehicle.display_info()
    
#inheritance with overriding __init__() method (manually)
class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        
class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        self.brand=brand
        self.color=color
        self.year=year
        self.horsepower=horsepower
        
vehicle=Vehicle("Tesla", "red", 2020)
car=Car("Tesla", "red", 2020, 300)

print(vehicle.__dict__)
print(car.__dict__)

#inheritance with overriding __init__() method (using super())
class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        
class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower=horsepower
        
vehicle=Vehicle("Tesla", "red", 2020)
car=Car("Tesla", "red", 2020, 300)

print(vehicle.__dict__)
print(car.__dict__)

# create a method that iterates through attributes and values
class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        
    def display_attrs(self):
        for key,value in self.__dict__.items():
            print(f'{key} -> {value}')

class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower
        
car=Car("Opel", "black", 2018, 160)
car.display_attrs()

#override ordinary method from parent class
class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower
        
    def display_attrs(self):
        print(f'Calling from class: {self.__class__.__name__}')  
        super().display_attrs()
            
car = Car('Tesla', 'black', 2018, 260)
car.display_attrs()

#overriding class attribute
class Container:

    category = 'general purpose'


class TemperatureControlledContainer(Container):
    temp_range = (-25.0, 25.0)


class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25.0, 5.0)
    
print(getattr(RefrigeratedContainer, "temp_range"))

#Inheritance from multiple classes (order matters!)
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age = age


class Department:
    pass


class Worker(Person, Department):
    pass

worker=Worker("John", "Doe", 35)
print(worker.__dict__)

#!!!How does MRO of multiple inheritance work?
class First(object):
    def __init__(self):
        print ("first")

class Second(object):
    def __init__(self):
        print ("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print ("that's it")

print(Third.mro())

###inheritance of __init__ of 2 parent classes:
class Person:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):
    def __init__(self, first_name, last_name, age, dept_name,
                 short_dept_name):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self,dept_name, short_dept_name)

worker = Worker("John", "Doe", 30, "Information Technology", "IT")
print(worker.__dict__)

###### ABSTRACT CLASSES ######

from abc import ABC, abstractmethod
     
     
class Figure(ABC):
     
    @abstractmethod
    def area(self):
        pass
     
     
class Square(Figure):
     
    def __init__(self, a):
        self.a = a
     
    def area(self):
        return self.a * self.a
     
     
try:
    Figure()
except TypeError as error:
    print(error)
    
#create abstract class with abstract methods and implement them

from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a
        
    def perimeter(self):
        return 4*self.a
        
square=Square(10)

print(square.area())
print(square.perimeter())

# abstract class with defined __init__()
from abc import ABC, abstractmethod

class TaxPayer(ABC):
    #also allowed to specify self.salary=salary
    def __init__(self, salary):
        pass 
    
    @abstractmethod
    def calculate_tax(self):
        pass
    
class Employee(TaxPayer):
    
    def __init__(self, salary):
        self.salary=salary
        
    def calculate_tax(self):
        return self.salary*0.20
    
employee = Employee(3000)
print(employee.calculate_tax())

#another example of using abctract class and method
from abc import ABC, abstractmethod
     
     
class TaxPayer(ABC):
     
    def __init__(self, salary):
        self.salary = salary
     
    @abstractmethod
    def calculate_tax(self):
        pass
     
     
class StudentTaxPayer(TaxPayer):
     
    def calculate_tax(self):
        return self.salary * 0.15
     
        
class DisabledTaxPayer(TaxPayer):
     
    def calculate_tax(self):
        return min(self.salary * 0.12, 5000.0)
     
     
disabled = DisabledTaxPayer(50000)
print(disabled.calculate_tax())

#use abstract class and methods. Iterate through instances

from abc import ABC, abstractmethod
     
     
class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary
     
    @abstractmethod
    def calculate_tax(self):
        pass
     
     
class StudentTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary * 0.15
     
     
class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary * 0.12
     
     
class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self):
        if self.salary < 80000:
            return self.salary * 0.17
        else:
            return 80000 * 0.17 + (self.salary - 80000) * 0.32
     
tax_payers = [
        StudentTaxPayer(50000),
        DisabledTaxPayer(70000),
        WorkerTaxPayer(68000),
        WorkerTaxPayer(120000),
    ]
for tax_payer in tax_payers:
    print(tax_payer.calculate_tax())


### SUMMARY ###

#!!!sort the list by nested elements using lambda  !!!

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    Person('Tom', 25),
    Person('John', 29),
    Person('Mike', 27),
    Person('Alice', 19),
]

func = lambda x: x.age
people =sorted(people, key = func, reverse =False)

for i in people:
    print (f'{i.name} -> {i.age}')

# implement instance method to set the attributes values to 0
#implement __repr__() for instance representation

class Point:

    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def reset(self):
        self.x=0
        self.y=0

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
        
point = Point (4,2)
print (point)
point.reset()
print (point)

"""
!! another instance (self,self doesn't work!!!) within instance method 
implement the method that calculates the euclidean distance of two points 
"""
import math
 
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
 
    def reset(self):
        self.x = 0
        self.y = 0
 
    def calc_distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        )
 
 
p1 = Point(0, 3)
p2 = Point(4, 0)
print(p1.calc_distance(p2))
        
#method that returns the time of instance creation

import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )

note1 = Note('My first note.')
note2 = Note('My second note.')

# find if word in the text input (return True/False):

import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )
    
    def find(self, word):
         return word in self.content
            
note1 = Note("Object Oriented Programming in Python.")

print(note1.find('python'))
print(note1.find('Python'))

# task above but with find () case insencitive

import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )
    
    def find(self, word):
        word = word.lower()
        return word in self.content.lower()
            
note1 = Note("Object Oriented Programming in Python.")

print(note1.find('python'))
print(note1.find('Python'))

#implement new class that appends list with instances of another class
import datetime
 
 
class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )
 
    def __repr__(self):
        return f"Note(content='{self.content}')"
 
    def find(self, word):
        return word.lower() in self.content.lower()
 
 
class Notebook:
    def __init__(self):
        self.notes = []
 
    def new_note(self, content):
        self.notes.append(Note(content))
 
 
notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
print(notebook.notes)

# print the notes attributes
import datetime

class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S'
        )

    def __repr__(self):
        return f"Note(content='{self.content}')"

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))
        
    def display_notes(self):
        for i in self.notes:
            print (i.content)

notebook = Notebook()
notebook.new_note("My first note.")
notebook.new_note("My second note.")
notebook.display_notes()

# implement method that returnes list of notes containing spec. word
import datetime

class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def __repr__(self):
        return f"Note(content='{self.content}')"        

    def find(self, word):
        return word.lower() in self.content.lower()

    
class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))

    def display_notes(self):
        for note in self.notes:
            print(note.content)
   #here note is instance of Note() so we can apply find() of Note()         
    def search(self, value):
        return [note for note in self.notes if note.find(value)]
                
notebook = Notebook()

notebook.new_note("Big Data")
notebook.new_note("Data Science")
notebook.new_note("Machine Learning")

print(notebook.search("data"))

#class attribute and instance __repr__() method
class Client:
 
    all_clients = []
 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)
 
    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"
 
 
client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')        
print(Client.all_clients)

# implement search method that browses through instances of another class


class ClientList(list):
    
    def search_email(self, value):
        return [client for client in Client.all_clients
        if value in client.email]
        

class Client:

    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"
        
client1=Client('Tom', 'sample@gmail.com')
client2=Client('Donald', 'sales@gmail.com')
client3=Client('Mike', 'sales@yahoo.com')
client4=Client('Lisa', 'info@gmail.com')
print(Client.all_clients.search_email('sales'))

#print all clients with email containing 'gmail'
class ClientList(list):

    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result

class Client:

    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"
        
client1=Client('Tom', 'sample@gmail.com')
client2=Client('Donald', 'sales@gmail.com')
client3=Client('Mike', 'sales@yahoo.com')
client4=Client('Lisa', 'info@gmail.com')

for client in Client.all_clients.search_email('gmail.com'):
    print(client)

#print the list of clients names who's email contains 'sales'
class ClientList(list):

    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result

class Client:

    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}', email='{self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@gmail.com')
client3 = Client('Mike', 'sales@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')

email_sales = []
for client in Client.all_clients.search_email('sales'):
    email_sales.append(client.name)
print (email_sales)




####TEST JOB DATA SCIENTIST####

list = [[], (), {}, "", [False]]
for i in list:
    print(bool(i))

#example: method returns True if at least 1 element in the list
class CustomDict(dict):
    
    def is_any_str_value(self):
        string_values = []
        for value in self.values():
            if type(value) == str:
                string_values.append(value)
        return bool(string_values)
    
customdict = CustomDict (phone = "samsung")
customdict.is_any_str_value()

#alternative solution

class CustomDict(dict):
 
    def is_any_str_value(self):
        flag = False
        for key in self:
            if isinstance(self[key], str):
                flag = True
                break
        return flag

customdict = CustomDict (phone = "samsung")
customdict.is_any_str_value()

#extending and modifying parent class method
class StringListOnly(list):
 
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError(
                'Only objects of type str can be added to the list.'
            )
        super().append(string)
 
 
slo = StringListOnly()
slo.append('Data')
slo.append('Science')
print(slo)

'''
Create a class named StringListOnly that extends the built-in list class. 
Modify the behavior of the append() method so that only objects of str 
type an be added to the list. Replace all uppercase letters with lowercase
before adding the object to the list. 
If you try to add a different type of object raise TypeError with message:
'''

class StringListOnly(list):
 
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError(
                'Only objects of type str can be added to the list.'
            )
        super().append(string.lower())

 
slo = StringListOnly()
slo.append('Data')
slo.append('Science')
slo.append ('Machine Learning')
print(slo)


# To the Warehouse class, add a method named add_product() that allows 
# to add an instance of the Product class to the products list
# If the product name is already in the products list, skip adding

import uuid
  
class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
 
    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
class Warehouse:
    def __init__(self):
        self.products = []
 
    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))
 
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
print(warehouse.products)

# To the Warehouse class, add a method named remove_product() 
# that allows you to remove an instance of the Product class from the 
# products list with a given product name. If the product name is not in 
# the products list, just skip.

import uuid
 
 
class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
 
    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
class Warehouse:
    def __init__(self):
        self.products = []
 
    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))
 
    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)
 
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.remove_product('Mobile Phone')
print(warehouse.products)

# To the Product class, add a __str__() method that is an informal 
# representation of the Product class.

import uuid

class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"
        
    def __str__(self):
        return f'Product Name: {self.product_name} | Price: {self.price}'

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


class Warehouse:

    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        product_names = [product.product_name for product in self.products]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)
                
product = Product('Mobile Phone', 1990.0)
print(product)

#Add a method to the Warehouse class named display_products() that 
#displays all products in the products attribute of the Warehouse class.

import uuid
 
class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
 
    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )
 
    def __str__(self):
        return f'Product Name: {self.product_name} | Price: {self.price}'
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
class Warehouse:
    def __init__(self):
        self.products = []
 
    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))
 
    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)
 
    def display_products(self):
        for product in self.products:
            print(product) # ! inherits __str__() from Productc class
 
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.display_products()

# Add a method called sort_by_price() to the Warehouse class that returns
# an sorted list of products.

import uuid
 
 
class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
 
    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
class Warehouse:
    def __init__(self):
        self.products = []
 
    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))
 
    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)
 
    def display_products(self):
        for product in self.products:
            print(
                f'Product ID: {product.product_id} | Product name: '
                f'{product.product_name} | Price: {product.price}'
            )
 
    def sort_by_price(self, ascending=True):
        return sorted(
            self.products,
            key=lambda product: product.price,
            reverse=not ascending,
        )
 
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)

for product in warehouse.sort_by_price():
    print(product)


#Complete the implementation of the method named search_product() 
# of the Warehouse class that allows you to return a list of products 
#containing the specified name (query argument).    

import uuid
 
class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
 
    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )
 
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
 
 
class Warehouse:
    def __init__(self):
        self.products = []
 
    def add_product(self, product_name, price):
        product_names = [
            product.product_name for product in self.products
        ]
        if not product_name in product_names:
            self.products.append(Product(product_name, price))
 
    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)
 
    def display_products(self):
        for product in self.products:
            print(
                f'Product ID: {product.product_id} | Product name: '
                f'{product.product_name} | Price: {product.price}'
            )
 
    def sort_by_price(self, ascending=True):
        return sorted(
            self.products,
            key=lambda product: product.price,
            reverse=not ascending,
        )
 
    def search_product(self, query):
        return [
            prod
            for prod in self.products
            if query in prod.product_name
        ]
 
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
print(warehouse.search_product('M'))
  

####   LinkedIn Assessment ####
def funk (list1, list2):
    for l in list1:
        for k in list2:
            print (l,k)

funk (['a','b','c'], [1,2,3]) 

multipliers = []
for n in range(10):
    if 4**n in range (5,95):
        multipliers.append (4**n)
print (multipliers[0], multipliers[-1])


############# Built-in Functions #################################

# eval() evaluates the expression passed into it
x = -1.5
expression = 'x**2 + x'

eval (expression)

eval ("print ('Hello World')") # "print" hasn't returned, just expr.

#isinstance():

var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

# sorted(), min(), max() for string

characters = ['k', 'b', 'c', 'j', 'z', 'w']

print(f'First: {min(sorted(characters))}\nLast: {max(sorted(characters))}')

# zip() for combining lists, tuples etc.

ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

list = []
for item in zip(ticker, full_name):
    list.append(item)
    
print (list)

#better solution
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

a = list(zip(ticker, full_name))
print(a)

# all() - check if all items return True

items = (' ', '0', 0.1, True)

print(all(items))

# any () - check if any item returns True

items = ('', 0.0, 0, False) # ! every item returns False

print(any(items))

#count the number of "1" in binary number

number = 234
binary = bin(number)
binary = binary[2:]
print(binary.count('1'))

############### defining own function #############################

# implement a function that accepts iterables and multiplies elements

def multi(x):
    if type(x) in (tuple, list): 
        result = 1
        for i in x:
            result= result*i
        return result
    else: raise TypeError()

multi([1,2,3])

# count the words longer than 2 chars

def count_str(list):
    total = 0
    for item in list:
        if isinstance(item, str):
            length = len(item) 
            if length > 2:
                total += 1
    return total

count_str ([1, '#hello', '', 'python', 'go'])

# implement a function that checks if list contains only unique items

def is_distinct(items):
    return len(items) == len(set(items))

is_distinct([1, 2, 3])

### l = [] is a default value of an argument

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)
    
function(3)
function(5, ['a', 'b', 'c'])
function(6)

# function with *args, **kwargs - returns separately (), {}

def function(*args, **kwargs):
    print(args, kwargs)
    
function(3, 4)
function(x=3, y=4)
function(1, 2, x=3, y=4)

# a function that checks if a word is palindrome (sounds same reverse):

def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False
        
is_palindrome('level')

########## Lambda Expressions, Map(), Filter() #####################

#Using the map() and the lambda expression, transform the given list
# into a list containing the lengths of each word and print it 

stocks = ['playway', 'boombit', 'cd projekt']

print(list(map(lambda x: len(x), stocks)))

#Implement the sort_list() function that sorts a list of 
#two-element tuple objects according to the second element of the tuple.

def sort_list(items):
    return sorted(items, key=lambda item: item[1])

sort_list([(1, 3), (4, 1), (4, 2), (0, 7)])

#remake the function using lambda

def func_1(x, y):
    return x + y + 2

func_2 = lambda x,y: x+y+2

### sort nested list by grades and by names (if more than 1) using lambda:
    
records = [["Adam", 20], ["Maria", 50], ['Anna',50], ["Lucy", 40]]

print(sorted(records, key = lambda x: (x[1], x[0])))

#Sort the list by the growing sum of squares of numbers in each 
#tuple. Use the sort() method and the lambda expression and print sorted list to the console.

items = [(3, 4), (2, 5), (1, 4), (6, 1)]

sorted(items, key = lambda x: x[0]**2+x[1]**2)

# Sort the given list of dictionaries by price key using lambda

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks.sort(key = lambda x: x['price'])
print (stocks)

# !!! using filter() and lambda extract companies from the 'mWIG40' index

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(list(filter(lambda x: x['index']=='mWIG40', stocks)))

# Convert the list to a list of boolean values (True, False). True if the company belongs to the 'mWIG40'
# use map() and lambda

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(list(map(lambda x: x['index']=='mWIG40', stocks)))

# trim the "-" using map() and lambda

items = ['P-1', 'R-2', 'D-4', 'F-6']

print(list(map(lambda x: x.replace("-",""), items)))

# !!! map() for 2 lists!!! and lambda

#Using the map()function and lambda expression, create a list 
#containing the remainders of dividing the first list by the second
# (elementwise).
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

print(list(map(lambda m, n: m%n, num1, num2))) 