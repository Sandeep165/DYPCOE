'''
You are given a list of integers having both negative and positive values, except for one integer which can be negative or positive.
 Create a function to find out that integer.

Examples
lonely_integer([1, -1, 2, -2, 3]) ➞ 3
# 3 has no matching negative appearance.

lonely_integer([-3, 1, 2, 3, -1, -4, -2]) ➞ -4
# -4 has no matching positive appearance.

lonely_integer([-9, -105, -9, -9, -9, -9, 105]) ➞ -9

'''

from unicodedata import name


def lonely_integer(lst):
    for i in lst:
        if -i not in lst:
            print(i)

# lonely_integer([-3, 1, 2, 3, -1, -4, -2])

'''
Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1,
 "o"s with 0, and "s"s with 5.
'''

string1 = "I love USA"
# print(string1.replace("USA","INDIA"))

def hack(string):
    print(string.replace("a","4"))

# hack("apple")
# 

def hacker_speack(x):
    print(x.replace("a","4").replace("e","3").replace("i","1").replace("o","0").replace("s","5"))

hacker_speack("become a coder")


'''
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and 
returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''
student = {
    "name" : "John",
    "age"  : 10
}


d1 = { "name" : "Sam"}
student.update(d1)
print(student)