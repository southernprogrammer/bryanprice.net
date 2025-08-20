---
title: Python Magic Functions
date: 2015-05-07T21:33:00-05:00
author: bryan
category: Blog
tags: ["Python"]
slug: python-magic-functions
status: published
---

# Python Magic Functions

Python has many magic functions that will allow your classes to do all
kinds of fun stuff. You may want your object to act like a dictionary,
or a list, you may want to make sure str() prints your object a certain
way, or you may want to override operators. You can tell your object how
to act with the \"in\" clause and how to deconstruct when using the
\"with\" clause. There are so many other magic methods as well.

Here\'s a simple example of using magic functions

``` python
class OppositeMath():
    def __init__(self, num):
        self.num = num
    def __eq__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return self.num != num
    def __gt__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return self.num <= num
    def __ge__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return self.num < num     
    def __lt__(self, num):         
        if isinstance(num, OppositeMath):
             num = num.num
         return self.num >= num
    def __le__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return self.num > num
    def __add__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return OppositeMath(self.num - num)
    def __sub__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return OppositeMath(self.num + num)
    def __mul__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return OppositeMath(self.num / num)
    def __div__(self, num):
        if isinstance(num, OppositeMath):
            num = num.num
        return OppositeMath(self.num * num)
    def __truediv__(self, num):
        return self.__div__(num)
    def __str__(self):
        return str(self.num)
    def __int__(self):
        return int(self.num)
    def __long__(self):
        return long(self.num)
    def __float__(self):
        return float(self.num)

a = OppositeMath(2)
b = OppositeMath(4)

print(str(a + b)) # -2
print(str(a - b)) # 6
print(str(a * b)) # .5
print(str(a / b)) # 8
print(str(a > b)) # True
print(str(a < b)) # False
print(str(a == b)) # True
print(str(a >= b)) # True
print(str(a <= b)) # False
```

You can test this example with [repl.it](http://repl.it/nCh)

But look at what we can do now, we can do math backwards! Obviously
there are several other mathematical functions that should probably be
implemented as well like square root and such, but this is a nice start.

So let\'s look at \_\_add\_\_.

``` python
def __add__(self, num):
    if isinstance(num, OppositeMath):
        num = num.num
    return OppositeMath(self.num - num)
```

When a + b is run **a** will be the **self** that comes into the
\_\_add\_\_ method and **b** will be **num**. So the left hand side must
always be an OppositeMath. I check to see if the right hand side is an
OppositeMath, and if it is I do math on the OppositeMath\'s num
variable. I also return an OppositeMath object because we may want to do
more opposite math after returning the value! Every other magic function
is pretty similar for this example. I also implement str, float, int,
and long to tell the interpreter what to do if someone tries to cast an
OppositeMath to those types.

OppositeMath itself isn\'t very useful, but you could do something like
implement an event dispatcher that uses the magic functions iadd and
isub to take advantage of += and -=. You could have those operators add
and remove events.

Here\'s a good resource for more magic methods:
<http://www.rafekettler.com/magicmethods.html>.
