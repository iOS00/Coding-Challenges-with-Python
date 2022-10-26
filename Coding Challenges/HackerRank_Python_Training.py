# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:45:36 2022

@author: winpr
"""
##############
n = int(input().strip())

if type(n) != int or n not in range (1,101,1):
    raise ValueError

if n%2 ==0 and n in range (2,6,1):
    print ("Not Weird")
elif n%2 ==0 and n in range (6,21,1):
    print ("Weird")
elif n%2 ==0 and n > 20:
    print ("Not Weird")
else: print ("Weird")

n

#############

a = int(input())
b = int(input())

if a not in range (1, (10**10+1),1):
    raise ValueError
elif b not in range (1, (10**10+1),1):
    raise ValueError

print(a+b)
print(a-b)
print (a*b)

a
b

#########

#define a leap year by 3 conditions:
"""    
In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""
    
def is_leap(year):
    leap = False
    
    if year%4 ==0:
        if year%100 !=0:
            leap = True
        elif year%100 ==0 and year%400 == 0:
            leap = True
            
    return leap

year = int(input())

is_leap(year)
    
    
# list comprehension

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([(i,j,k) for i in range(0,x+1,1) 
       for j in range(0,y+1,1) 
       for k in range(0,z+1,1) if i+j+k !=0])


############

n = int(input())
arr = map(int, input().split())
    
l = list(arr)
if n not in range(2,11,1):
    raise ValueError

for i in l:
    if i not in range (-100,101,1):
        raise ValueError
    
for i in sorted(l, reverse=True):
    if i == max(sorted(l, reverse=True)):
        continue
    else: print(i)
    break

### sort nested list by grades and by names (if more than 1) using lambda:
    
records = [["Adam", 20], ["Maria", 50], ['Anna',50], ["Lucy", 40]]

print(sorted(records, key = lambda x: (x[1], x[0])))

a= 5.375

print(round(a, 2))


"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and 
vice versa.
"""
############## list(word) == ['w', 'o', 'r', 'd'] #######################


def swap_case(s):
    if type(s) != str:
        raise ValueError
    elif not len(s) in range(1,1001,1):
        raise ValueError
    word = list(s)
    string = []
    for letter in word:
        if not letter.isalpha():
            string.append(letter)
            continue
        elif letter.islower():
            string.append(letter.upper())
        elif letter.isupper():
            string.append(letter.lower())
    string = ''.join(string)
    return string

swap_case('AmericA "Colorado!"')

# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    if type(first) != str or type(last) != str:
        raise ValueError
    elif not len(first) in range (11):
        raise ValueError
    elif not len(last) in range (11):
        raise ValueError
    print(f'Hello {first} {last}! You just delved into python.')
    
# replace letter in the string: 
    
def mutate_string(string, position, character):
    if not type(string) == str:
        raise ValueError
    elif not type(position) == int:
        raise ValueError
    elif not type(character) == str:
        raise ValueError
    s = list(string)
    s[position] = character
    string = ''.join(s)
    return string

#count the number of occurrencer of substring in string(incl. overlapping)

text = "ABCDCDC"

def count_substring(string, sub_string):
    
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count

count_substring(text, 'CDC')

# In Python, a string of text can be aligned left, right and center.
# .ljust(width), .center(width), .rjust(width)

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
 thickness = int(input())
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# wrap text

import textwrap

def wrap(string, max_width):
    if type(string)!= str:
        raise ValueError
    elif type(max_width) != int:
        raise ValueError
    elif len(string) not in range(1,1000,1):
        raise ValueError
    elif max_width not in range(1,len(string),1):
        raise ValueError 
    line = string[:max_width]
    string = string[max_width:]
    if len(string) > max_width:
        string = wrap(string, max_width)
    return line + '\n' + string
    
wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

#######
"""
Mr. Vincent works in a door mat manufacturing company. One day, he 
designed a new door mat with the following specifications:"""

#my solution
N=9

if not N in range(6,101, 1):
    raise ValueError
M = 3*N

c  = ".|."

#Top Cone
    
k=1
for i in range(int((N-1)/2)):
    print((c*k).center(M, "-"))
    k = k+2
    
#Middle Belt
print("WELCOME".center(M, "-"))

#Bottom Cone

k=7
for i in range(int((N-1)/2)):
    print((c*k).center(M, "-"))
    k = k-2

# alternative solution:
    
N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i * ".|.").center(M,"-"))
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))  

"""    
Given an integer, n, print the following values for each integer i from 
1 to n:
Decimal Octal Hexadecimal (capitalized) Binary The four values must be
printed on a single line in the order specified above for each from to . 
Each value should be space-padded to match the width of the binary value 
of . """

def print_formatted(number):

    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))
        
"""
You are given an integer, N. Your task is to print an alphabet rangoli of
 size N. (Rangoli is a form of Indian folk art based on creation of 
          patterns.)
Different sizes of alphabet rangoli are shown below: """

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
"""
You are asked to ensure that the first and last names of people begin with 
a capital letter in their passports. For example, alison heck should be 
capitalised correctly as Alison Heck. """

# Complete the solve function below.
import re
import os

def solve(s):
    result=[]
    name=re.split(r'(\s+)',s)

    for i in range(len(name)):
       result.append(str(name[i]).capitalize())
       
    return ''.join(str(ele) for ele in result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
"""
The Minion Game

Kevin and Stuart want to play the 'The Minion Game' """

### my solution

#s = "banana"

#s = input()

vowels = ['A', 'E', 'I', 'O', 'U']

consonants = [chr(i).upper() for i in range(ord('a'),ord('z')+1) 
              if chr(i).upper() not in vowels]
    
def find_and_cut(s, i):
    global words #remember to declare output as global
    words = []
    l = list(s.upper()[i:])
    length = len(l)
    for n in range(1,length+1,1):
        word = "".join(l[:n])
        words.append(word)
    return words


def minion_game(s):
    if not s.isalpha():
        raise ValueError
    elif not s.isupper():
        raise ValueError
    elif len(s) not in range (1, (10**6)+1, 1):
        raise ValueError
    vowel_words=[]
    cons_words=[]
    for i, letter in enumerate(s.upper()):
        if letter in vowels:
            vowel_words.extend(find_and_cut(s, i))
        elif letter in consonants:
            cons_words.extend(find_and_cut(s, i))
    if len(vowel_words) > len(cons_words):
        print(f'Kevin {len(vowel_words)}')
    elif len(vowel_words) == len(cons_words):
        print(f'Draw')
    else: print(f'Stuart {len(cons_words)}')
    
minion_game("NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN")

# alternative solution (without constraints, but passed all tests?!!)

def minion_game(string):
    k=0
    s=0
    vowels="AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vowels:
            k=k+len(string)-i
        else:
            s=s+len(string)-i    
    
    if k>s:
        print("Kevin",k)
    elif k==s:
        print("Draw")    
    else:
        print("Stuart",s)
        
#### SET ###############

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = input()

n = int(input())
b= input()


lis1 = a.split()
lis1 = list(map(int, lis1))
if len(lis1) !=m:
    raise ValueError
lis2 = b.split()
lis2 = list(map(int, lis2))
if len(lis2) !=n:
    raise ValueError

set1 = set(lis1)
set2 = set(lis2)

dif_a_b = set1.difference(set2)
dif_b_a = set2.difference(set1)
result = sorted(list(dif_a_b.union(dif_b_a)))

for i in result:
    print (i)
    
"""
Consider the following:

A string, s, of length n where s = c0c1. . . . cn-1.

An integer, k, where k is a factor of n. We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.

Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui."""

#my solution
def merge_the_tools(string, k):
    n = len(string)
    if n not in range (1,10**4+1):
        raise ValueError
    elif not 1<=k<=n:
        raise ValueError
    elif not n%k ==0:
        raise ValueError
    substring = []
    output=[]
    for l in range(0,(n-int(n/k))+1,int(n/k)):
        substring.append(string[l:l+int(n/k)])
    for text in substring:
        text_split=list(text)
        tj=[]
        for letter in text_split:
            if letter not in tj:
                tj.append(letter)
            else:
                continue
        sub_text="".join(tj)
        output.append(sub_text)
    for word in output:
        print(word)
 
#alternative solution (passed all tests)

def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0

merge_the_tools("AAABCADDE", 3)

"""
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B). 
"""

A = sorted(list(set(input())))

for a in A:
    if a not in range (1,30,1):
        raise ValueError

B = sorted(list(set(input())))
for b in B:
    if b not in range (1,30,1):
        raise ValueError

A = list(map(int, A))
B = list(map(int, B))

from itertools import product
print(sorted(list(product(A,B))))

