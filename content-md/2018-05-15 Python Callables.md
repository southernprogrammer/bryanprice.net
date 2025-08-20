---
title: Python Callables
date: 2018-05-15T16:07:00-05:00
modified: 2018-05-15 16:07
category: Blog
tags: ["python"]
slug: python-callables
authors: Bryan Price
summary: Partials are great, but what happens when you know the parameters
---

# Python Callables

    that need to be in the back of the method call and not the front?

In a previous post, I talked about python partials. They provide a way
to make a new function from another with some parameters at the front
pre-filled. What can we do to fix this? Well there is a 3rd party
library called [funcy that provides an rpartial
method](https://stackoverflow.com/questions/7811247/how-to-fill-specific-positional-arguments-with-partial-in-python).
Or you could do something custom, like making a callable. You can make a
callable class by implementing the magic function \_\_call\_\_. This
lets you call an object instance like a method.

``` python
thing = MyCallableClass()
result = thing()
```

So now let\'s apply this concept to implement rpartial.

``` python
class RPartial:
    def __init__(self, method, *args):
        self.method = method
        self.args = args

    def __call__(self, *args):
        return self.method(*(args + self.args))

import os
r_join = RPartial(os.path.join, "my", "cool", "path")
print(r_join("C:\\")) # c:\my\cool\path is output
```

This is much more verbose than funcy\'s version of rpartial, but it does
serve well as an example of how you can use callables. You could
definitely make something more specific for your needs.
