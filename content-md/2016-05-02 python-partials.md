---
title: Python Partials
date: 2016-05-02T11:23:00-05:00
modified: 2016-05-02 11:23
category: Blog
tags: ["Python"]
slug: python-partials
authors: bryan
summary: I discuss the usefulness of Partials in Python
---

# Python Partials

Have you ever heard of the concept of currying? If not, I\'m about to
blow your mind. Let\'s say that you have a method you want to use and it
takes two parameters. The only problem is that you only have one
parameter at the moment. You will have the next parameter later. You can
create an intermediate method from the other method that takes one
parameter and then use that method at the time of your choosing. In
Python, this is achieved by using a partial.

Let\'s say that you ran os.listdir, this method returns the unqualified
file names inside of a folder. The only problem is that I want the file
names fully qualified with it\'s entire path. So I should use
os.path.join on each of the items.

``` python
import os
from functools import partial
folder = "/your/path/to/whatever"
folder_join = partial(os.path.join, folder)
images = [x for x in os.listdir(folder) if x.endswith(".jpg")]
images = list(map(folder_join, images))
print(str(images))
```

If one.jpg, two.jpg, and three.jpg are in our folder, we would get this
output =\> \[\'/your/path/to/whatever/one.jpg\',
\'/your/path/to/whatever/two.jpg\',
\'/your/path/to/whatever/three.jpg\'\]
