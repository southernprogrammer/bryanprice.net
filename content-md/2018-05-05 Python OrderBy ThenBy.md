---
title: Python OrderBy ThenBy
date: 2018-05-05T13:24:00-05:00
modified: 2018-05-05 13:24
category: Blog
tags: ["python"]
slug: python-orderby-thenby
authors: Bryan Price
summary: C#\'s Linq can do .OrderBy and .ThenBy on an enumerable, can Python
---

# Python OrderBy ThenBy

    do something similar?

The other day I found a bug in a python file I had written. I ordered a
list by two attributes descending, when I really wanted to order the
list by one attribute descending and the other ascending.

For reference, I started off with something similar to the following
code. I\'m using tuples here instead of attributes off of an object, but
the premise remains.

``` python
lst = [(2, 3), (2, 2), (2, 5), (1, 6), (1, 4), (50, 1)]
lst.sort(reverse=True)
# if using an object the line would look similar to this lst.sort(key=lambda x: (x.first_attribute, x.second_attribute), reverse=True)
```

This is all fine, great, and wonderful, but I really needed to sort by
the first attribute descending and the second ascending. So how do we
accomplish this? We use cmp on the sort. A compare function takes 2
parameters and returns an integer. If the integer is negative, the sort
knows that the first item is should be favored, if 0 it should favor
neither, and if positive the second item should be favored.

``` python
lst = [(2, 3), (2, 2), (2, 5), (1, 6), (1, 4), (50, 1)]
lst.sort(cmp=lambda x, y: x[1] - y[1] if x[0] == y[0] else y[0] - x[0])
```

If you aren\'t familiar with lambda\'s they are just functions that take
in parameters and no return statement is needed. Everything right of the
colon is returned. So what\'s going on here? Well if the first values
are equal and x is less than y (x\[1\]-y\[1\] \< 0) we favor x
(ascending). Otherwise we just compare y\[0\] and x\[0\].

What about Python 3.0? It doesn\'t support cmp, but don\'t worry
there\'s a workaround. If you are in Python 3.2 you can utilize a method
called functools.cmp_to_key(). If you are between 3.0 and 3.2, you will
have to implement the method yourself. See
<https://docs.python.org/3/howto/sorting.html>.

``` python
import functools
lst = [(2, 3), (2, 2), (2, 5), (1, 6), (1, 4), (50, 1)]
lst.sort(key=functools.cmp_to_key(lambda x, y: x[1] - y[1] if x[0] == y[0] else y[0] - x[0]))
```

The key variable is also available in Python 2, but there you will
probably just use it as it\'s meant to be used: to tell what the key of
your sort is.

So how would you compare strings? You should use locale.strcoll

``` python
import functools
import locale
lst = [("b", 3), ("b", 2), ("b", 5), ("a", 6), ("a", 4), ("z", 1)]
lst.sort(key=functools.cmp_to_key(lambda x, y:  x[1] - y[1] if x[0] == y[0] else locale.strcoll(y[0], x[0])))
```

In C# it\'s really easy to do this kind of thing. Linq has an OrderBy,
OrderByDescending, ThenBy, and ThenByDescending methods. But even though
it\'s not as easy to do this in python, it\'s not really that difficult.
