#!/usr/bin/env python
# coding: utf-8

# # Say "Hello, World!" With Python

# In[1]:


print("Hello, World!")


# # Python If-Else

# In[ ]:


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if n%2==1:
        print('Weird')
    else:
        if n>=2 and n<=5:
                print("Not Weird")
        elif n>=6 and n<=20:
                print("Weird")
        else:
                print("Not Weird")


# # Arithmetic Operators

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# # Python: Division

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b) 
    print(a/b)


# # Loops

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)


# # Write a function

# In[ ]:


def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0):
        leap = True
    elif(year%400==0):
        leap = True
    else:
        leap=False
    
    return leap


# # Print Fuction

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")


# # List Comprehensions

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) 
    if (i+j+k!=n)])


# # Find the Runner-Up Score!

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])


# # Nested Lists

# In[ ]:


marksheet=[]
n=int(input())
for _ in range(n):
    name=input()
    score=float(input())
    marksheet.append([name,score])
#marksheet=[[name,score] for _ in range(0,n)]
second_lowest=sorted(set(score for name,score in marksheet))[1]
print("\n".join(name for name,score in sorted(marksheet) if score==second_lowest))


# # Finding the percentage

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name])/len(student_marks[query_name])
    print("%.2f" % avg)


# # Lists

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    M=[]
    for _ in range(N):
       line=input().split(" ")
       command=line[0]
       if(command == "insert"):
        M.insert(int(line[1]),int(line[2])) #insert(index,object)
       elif(command == "print"):
        print(M)
       elif(command == "remove"):
        M.remove(int(line[1]))
       elif(command == "append"):
        M.append(int(line[1]))
       elif(command == "sort"):
        M.sort()
       elif(command == "pop"):
        M.pop()
       elif(command == "reverse"):
        M.reverse()


# # Tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))


# # sWAP cASE

# In[ ]:


def swap_case(s):
    str=s.swapcase()
    return str


# # String Split and Join

# In[ ]:


def split_and_join(line):
    # write your code here
    s=line.split(" ")
    s="-".join(s)
    return s


# # What's Your Name?

# In[ ]:


def print_full_name(a, b):
    print("Hello "+a+" "+b+"! "+"You just delved into python.")


# # Mutations

# In[ ]:


def mutate_string(string, position, character):
    L=list(string)
    L[position]=character
    S="".join(L)
    return S


# # Find a String

# In[ ]:


def count_substring(string, sub_string):
    n=0
    List=[]
    for i in range(0,len(string)-len(sub_string)+1):  
       List.append(string[i:i+len(sub_string)])
    for j in range(len(List)):
        if(sub_string == List[j]):
            n=n+1
    return n


# # String Validators

# In[ ]:


if __name__ == '__main__':
    s = input()
    #1 any alphanumeric
    print(any(letter.isalnum() for letter in s))
    # 2 any alphabetical characters
    print(any(letter.isalpha() for letter in s))
    #3 any digits
    print(any(letter.isdigit() for letter in s))
    #4 any lowercase
    print(any(letter.islower() for letter in s))
    #5 any uppercase
    print(any(letter.isupper() for letter in s))


# # Text Alignment

# In[ ]:


#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
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


# # Text Wrap

# In[ ]:


def wrap(string, max_width):
    #1st method
    #return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    #range(start,stop,step)
    #2nd method
    lists = textwrap.wrap(string, width=max_width) 
    return "\n".join(lists)


# # Designer Door Mat

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
#center(width, fillchar)
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# # String Formatting

# In[ ]:


def print_formatted(number):
    # your code goes here
    w = len(str(bin(number).replace('0b','')))
    for i in range(1,number+1):
        b = bin(int(i)).replace('0b','').rjust(w, ' ')
        o = oct(int(i)).replace('0o','').rjust(w, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
        d = str(i).rjust(w, ' ')
        print(d,o,h,b)
    return 
#replace(old,new,max) max times


# # Alphabet Rangoli

# In[ ]:


import string 
letter=string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    #N->4N-3*2N-1 （Column*Row）
    List=[]
    for i in range(size):
       s="-".join(letter[i:size])
       List.append((s[::-1]+s[1:]).center(4*size-3,"-"))
    print("\n".join(List[:0:-1]+List))
    return


# # Capitalize!

# In[ ]:


# Complete the solve function below.
def solve(s):   
    return " ".join(l.capitalize() for l in s.split(" "))


# # The Minion Game

# def minion_game(string):
#     # your code goes here
#     vowels='AEIOU'
#     Staurt=0
#     Kevin=0
#     for i in range(len(string)):
#         if(string[i] in vowels):
#             Kevin+=(len(string)-i)
#         else:
#             Staurt+=(len(string)-i)
#     if(Kevin>Staurt):
#         print('Kevin',Kevin)
#     elif(Staurt>Kevin):
#         print("Stuart",Staurt)
#     else:
#         print("Draw")
#     return

# # Merge the Tools!

# In[ ]:


from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    L=[]
    i=0
    while i<len(string):
        L.append(string[i:i+k])
        i=i+k
    for j in range(len(L)):
       print("".join(OrderedDict.fromkeys(L[j])))
    return


# # Introduction to Sets

# In[ ]:


def average(array):
    # your code goes here
   return(sum(set(array))/len(set(array)))


# # Symmetric Difference

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
L=[]
a=set()
b=set()
for _ in range(4):
    L.append(input().split())
a.update(list(map(int,L[1])))
b.update(list(map(int,L[3])))
#c=a.difference(b).union(b.difference(a))
c=a.symmetric_difference(b)
c=list(c)
c.sort()
for num in c:
   print(num)


# # No Idea!

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
L=[]
H=0
a=set()
b=set()
for _ in range(4):
    L.append(input().split())
Arr=list(map(int,L[1]))

a.update(list(map(int,L[2])))
b.update(list(map(int,L[3])))
for num in Arr:
    if num in a:
        H+=1
    elif num in b:
        H-=1
print(H)


# # Set.add()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
for _ in range(int(input())):
    s.add(input())
print(len(s))


# # Set .discard(), .remove() & .pop()

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
L=[]
R=0
for i in range(int(input())):
    L.append(input().split())
for j in range (len(L)):
    if "pop" in L[j]:
        s.pop()
    elif "remove" in L[j]:
        s.remove(int(L[j][1]))
    elif "discard" in L[j]:
        s.discard(int(L[j][1]))
S=list(s)
for num in S:
    R+=int(num)
print(R)


# # Set .union() Operation

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set()
B=set()
F=int(input())
A.update(list(map(int,input().split(' '))))
S=int(input())
B.update(list(map(int,input().split(' '))))
C= A.union(B)
print(len(C))


# # Set .intersection() Operation

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set()
B=set()
F=int(input())
A.update(list(map(int,input().split(' '))))
S=int(input())
B.update(list(map(int,input().split(' '))))
C= A & B
print(len(C))


# # Set .difference() Operation

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set()
B=set()
F=int(input())
A.update(list(map(int,input().split(' '))))
S=int(input())
B.update(list(map(int,input().split(' '))))
C= A-B
print(len(C))


# # Set .symmetric_difference() Operation

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set()
B=set()
F=int(input())
A.update(list(map(int,input().split(' '))))
S=int(input())
B.update(list(map(int,input().split(' '))))
C= A^B
print(len(C))


# # Set Mutations

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set()
B=set()
L=[]
Num=0
F=int(input())
A.update(list(map(int,input().split(' '))))
S=int(input())
for i in range(S*2):
    L.append(input().split())
for j in range(len(L)):
    if "intersection_update" in L[j]:
       A.intersection_update(set(list(map(int,L[j+1]))))
    elif "update" in L[j]:
        A.update(set(list(map(int,L[j+1]))))
    elif "symmetric_difference_update" in L[j]:
        A.symmetric_difference_update(set(list(map(int,L[j+1]))))
    elif "difference_update" in L[j]:
        A.difference_update(set(list(map(int,L[j+1]))))
LN=list(A)
for num in (LN):
   Num+=int(num)
print(Num)


# # The Captain's Room

# In[ ]:


k = int(input())
L = list(map(int, input().split()))
listSum = sum(L)
#listsum所有元素的和1*5+2*5+3*5+4*5+5*5+6*5+8=21*5+8=113
setSum = sum(set(L))
#不重复元素的和 1+2+3+4+5+6+8=21+8=29
ans = (setSum * k - listSum) // (k - 1)
#（(21+8)*5 - (21*5+8) =8*4
print(ans)


# # Check Subset

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))


# # Check Strict Superset

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
print(all(a.issuperset(set(input().split())) for _ in range(int(input()))))

#A.issuperset(B)  A is the superset of B?
#a>b 


# # collections.Counter()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
shoes=Counter(map(int,input().split()))
N=int(input())
income = 0
for i in range(N):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)


# # DefaultDict Tutorial

# In[ ]:


from collections import defaultdict

n,m = map(int,input().split())

d = defaultdict(list)
for i in range(n):
    s = input()
    d[s].append(i+1)

for i in range(m):
    x = input()
    if x in d:
        print(' '.join(map(str,d[x])))
    else:
        print(-1)


# # Collections.namedtuple()

# In[ ]:


from collections import namedtuple
n = int(input())
sum = 0
stu = namedtuple('stu',input().split())
for i in range(n):
    x, y, z, t = input().split()
    s = stu(x,y,z,t)
    sum += float(s.MARKS)
aver = sum / n
print("%.2f" % aver)


# # Collections.OrderedDict()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    s = input().split()
    k = ' '.join(s[:-1])#不包含最后一位
    v = int(s[-1])#最后一位
    if k in od:
        od[k] += v
    else:
        od[k] = v
for i in od:
    print(i,od[i])


# # Word Order

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
book = OrderedDict()
for i in range(int(input())):
    str = input()
    if str not in book:
        book[str] = 1
    else:
        book[str] += 1
print(len(book))       
for i in book.keys():
    print(book[i], end =" ")


# # Collections.deque()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for i in range(int(input())):
    s=input().split()
    x=s[0]
    if(x=="append"):
        d.append(s[1])
    elif(x=="appendleft"):
        d.appendleft(s[1])
    elif(x=="pop"):
        d.pop()
    elif(x=="popleft"):
        d.popleft()
for item in d:
   print(item,end=" ") 


# # Piling Up!

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())
for case in range(T):
    n = int(input())
    ls = list(map(int,input().split()))
    pos = ls.index(min(ls))
    left = ls[:pos]
    right = ls[pos:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")


# # Company Logo

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    s = input()
    dic = collections.OrderedDict()
    for i in s:
        if not i in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    cnt = 3
    for i in sorted(dic.items(), key = lambda item : (-item[1], item[0])):
        if cnt > 0:
            print(*i)
            cnt -= 1


# # Calendar Module

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
M,D,Y=map(int,input().split())
import calendar
A=calendar.weekday(Y, M, D)
if(A==0):
    print("MONDAY")
elif(A==1):
    print("TUESDAY")
elif(A==2):
    print("WEDNESDAY")
elif(A==3):
    print("THURSDAY")
elif(A==4):
    print("FRIDAY")
elif(A==5):
    print("SATURDAY")
elif(A==6):
    print("SUNDAY")


# # Time Delta

# In[ ]:



import math
import os
import random
import re
import sys
import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    #Sun 10 May 2015 13:54:36 -0700
    d1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    d2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    d=d1-d2
    return(str(int(abs(d.total_seconds())))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


# # Exceptions

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a,b=input().split()
    try:
      print(int(a)//int(b))
    except ZeroDivisionError as e:
        print( "Error Code:",e)
    except ValueError as v:
        print ("Error Code:",v)


# # Zipped!

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
#N stu X sub
n, x = map(int, input().split()) 
sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 
for i in zip(*sheet): 
    print( sum(i)/len(i) )


# # Athlete Sort

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    L=sorted(arr,key=(lambda x:x[k]))
    for i in range(len(L)):
        print(" ".join(map(str,L[i])))
    


# # ginortS

# In[ ]:


import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')


# # Map and Lambda Function

# In[ ]:


cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])


# # Detect Floating Point Number

# In[ ]:


import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',input())))


# # Re.split()

# In[ ]:


regex_pattern = r"\W+"	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))


# # Group(), Groups() & Groupdict()

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)


# # Re.findall() & Re.finditer()

# In[ ]:


import re
v = "AEIOUaeiou"
c = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))


# # Re.start() & Re.end()

# In[ ]:


S = input()
k = input()
import re
pattern = re.compile(k)
#compile() 函数将一个字符串编译为字节代码。
r = pattern.search(S)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1)) 
    r = pattern.search(S,r.start() + 1)


# # Regex Substitution

# In[ ]:


import re
for i in range(int(input())):
     print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or',input()))


# # Validating Roman Numerals

# In[ ]:


regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# # Validating phone numbers

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
regex_pattern = r"^[789]\d{9}$"    
import re
for i in range(int(input())):
    print("YES" if re.match(regex_pattern, input()) else "NO")


# # Validating and Parsing Email Addresses

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
regex_pattern = r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"    
import re
import email.utils
for i in range(int(input())):
    uname, uemail = email.utils.parseaddr(input())
    if re.match(regex_pattern, uemail):
      print(email.utils.formataddr((uname,uemail)))


# # Hex Color Code

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    x=re.findall(r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})',input())
    for i in range(len(x)):
        print(x[i])


# # XML 1 - Find the Score

# In[ ]:


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    m=0
    for child in node.iter():
        m+=len(child.items())
    return m

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# # XML2 - Find the Maximum Depth

# In[ ]:


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1    
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# # HTML Parser - Part 1

# In[ ]:


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))


# # HTML Parser - Part 2

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
     def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)
        
     def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
  
  
 
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# # Detect HTML Tags, Attributes and Attribute Values

# In[ ]:


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr) ) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# # Validating UID

# In[ ]:


import re
N = int(input())
no_repeats = r'(?!.*(.).*\1)' 
two_plus_uppercase = r'(?=(?:.*[A-Z]+){2,})'
three_plus_digits = r'(?=(?:.*\d){3,})'
ten_alphanumeric = r'[\w]{10}'
filters = [no_repeats, two_plus_uppercase, three_plus_digits, ten_alphanumeric]

for i in range(0, N):
    uid = input()
    print('Valid') if all([re.match(f, uid) for f in filters]) else print      ('Invalid')


# # Validating Credit Card Numbers

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
start = r'^[4,5,6]' 
four_group=r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'
no_seperator = r'[^\s_]'
no_more_four_repeat = r"(?!.*(\d)(-?\1){3})"

filters = [start,four_group,no_seperator,no_more_four_repeat ]

for i in range(0, N):
    uid = input()
    print('Valid') if all([re.match(f, uid) for f in filters]) else print('Invalid')


# # Validating Postal Codes

# In[ ]:


regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# # Matrix Script

# In[ ]:


#!/bin/python3
#It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
print(re.sub(r'(\w)(\W)+(\w)',
          r'\1 \3',
          ''.join([u for t in zip(*matrix) for u in t])))


# # Standardize Mobile Number Using Decorators

# In[ ]:


def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



# # Decorators 2 - Name Directory

# In[ ]:


import operator

def person_lister(f):
    def inner(people):     
        return map(f, sorted(people, key=lambda x: int(x[2]))) 
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# # Arrays

# In[ ]:



def arrays(arr):
    L=numpy.array(arr,float)
    #return L[::-1]
    return numpy.flipud(L)
#numpy.flipud => reverse the array
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# # Shape and Reshape

# In[ ]:


import numpy

arr = input().strip().split(' ')
L=numpy.array(arr,int)
print(numpy.reshape(L,(3,3)))


# # Transpose and Flatten

# In[ ]:


import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())


# # Concatenate

# In[ ]:


import numpy

N,M,P=map(int,input().strip().split(' '))
L1=numpy.array([input().strip().split() for _ in range(N)],int)
L2=numpy.array([input().strip().split() for _ in range(M)],int)
print(numpy.concatenate((L1, L2), axis = 0))   


# # Zeros and Ones

# In[ ]:


import numpy
num=tuple(map(int,input().strip().split(' ')))
print(numpy.zeros(num, dtype = numpy.int))
print(numpy.ones(num, dtype = numpy.int))


# # Eye and Identity

# In[ ]:


import numpy
N,M=map(int,input().split())

print(str(numpy.eye(N,M)).replace('1',' 1').replace('0',' 0')) 


# # Array Mathematics

# In[ ]:


import numpy

N,M=map(int,input().split())
A=numpy.array([input().strip().split() for _ in range(N)],int)
B=numpy.array([input().strip().split() for _ in range(N)],int)

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
#A//B np.floor_divide(A,B) 
#A/B np.true_divide(A,B)
print(numpy.mod(A,B))
print(numpy.power(A,B))


# # Floor, Ceil and Rint

# In[ ]:


import numpy
numpy.set_printoptions(sign=' ')
L=numpy.array(input().strip().split(),float)
print(numpy.floor(L))
print(numpy.ceil(L))
print(numpy.rint(L))


# # Sum and Prod

# In[ ]:


import numpy

N,M=map(int,input().split())
L=numpy.array([input().strip().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(L,axis=0)))


# # Min and Max

# In[ ]:


import numpy

N,M=map(int,input().split())
L=numpy.array([input().strip().split() for _ in range(N)],int)
print(numpy.max(numpy.min(L,axis=1)))


# # Mean, Var, and Std

# In[ ]:


import numpy
numpy.set_printoptions(sign=" ",legacy='1.13')
N,M=map(int,input().split())
L=numpy.array([input().strip().split() for _ in range(N)],int)
print(numpy.mean(L,axis=1))
print(numpy.var(L,axis=0))
print(numpy.std(L,axis=None))


# # Dot and Cross

# In[ ]:


import numpy
N=int(input())
A=numpy.array([input().strip().split() for _ in range(N)],int)
B=numpy.array([input().strip().split() for _ in range(N)],int)
print(numpy.dot(A,B))


# # Inner and Outer

# In[ ]:


import numpy
A=numpy.array(input().strip().split(),int)
B=numpy.array(input().strip().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))


# # Polynomials

# In[ ]:


import numpy
A=numpy.array(input().strip().split(),float)
print(numpy.polyval(A,float(input())))


# # Linear Algebra

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
N=int(input())
A=numpy.array([input().strip().split() for _ in range(N)],float)
print(numpy.linalg.det(A))


# # Birthday Cake Candles 

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    return Counter(candles).most_common(1)[-1][-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Number Line Jumps

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    N=str()
    if(v1==v2):
        N="NO"
    elif((x1-x2)/(v2-v1)>0 and (x1-x2)%(v2-v1)==0):
        N="YES"
    else:
        N="NO"
    return N
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# # Viral Advertising

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    Num=2
    total=2
    for i in range(1,n):
       Num= Num*3//2
       #Num=P
       total+=Num
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Recursive Digit Sum

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the superDigit function below.
def superDigit(n, k):
    x = (int(n) * k) % 9
    return(x if x else 9)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Insertion Sort - Part 1

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    i = n-1
    val = arr[i]
    while(i>0 and val<arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    arr[i] = val
    print(*arr)
    return
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# # Insertion Sort - Part 2

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        print(*arr)
    return
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)







