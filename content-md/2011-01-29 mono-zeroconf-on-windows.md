---
title: Mono Zeroconf on Windows
date: 2011-01-29T10:04:00-06:00
author: bryan
category: Project Updates
tags: [".NET", " Apple", " Bonjour", " CCS", " Java", " Mono", " Windows", " Zeroconf"]
slug: mono-zeroconf-on-windows
status: published
---

# Mono Zeroconf on Windows

If you know anything about my classroom control system that I built, you
know that the project requires Bonjour.  This is the technology Apple
uses to help you share your music on a network.  Computers discover one
another by publishing their address on a multicast port.  Because the
port is multicast the information gets sent to all computers on the
network (you must have a multicast router).  I used a library in java
called Bonaha that abstracted away a lot of the complexities of Apple's
Bonjour SDK.

I wanted a way to do the same thing in .NET because, well frankly I'd
like to make my classroom control system a more cohesive piece of
software and not the kludge that it is (in 2 different languages Java
and .NET and pieced together with Elmer's Glue©).

The obvious choice to keep up with the network state is Mono.Zeroconf. 
It's a project that's separate from the main Mono repository itself.  I
expected this software to work out of the gate.  It may work fine on
Linux using the Avahi provider; but with the Bonjour Provider on Windows
I had to do some modifications of the source to get it to run.  Luckily
there were others online that had already found the problems for me (but
the forum posts were in 2 different places and a little difficult to
find.), so for your convenience I am combining those bits of information
in this blog post.

First you'll need to do as
[Frankenspank](http://stackoverflow.com/users/313673/frankenspank)
suggested on
[this](http://stackoverflow.com/questions/599846/how-to-register-a-service-with-mono-zeroconf)
StackOverflow post.  You'll need to change the **UPort** Setter in
**Service.cs** file (in the Bonjour Provider Project) to be:

``` java
this.port=(ushort)IPAddress.HostToNetworkOrder((short) value);
```

Next you'll need to change the **OnResolveReply** method in the
**BrowseService.cs** file (again in the Bonjour Provider Project).

You'll need to change the second if statement from

``` java
if (AddressProtocol == AddressProtocol.Any || 
    AddressProtocol == AddressProtocol.IPv6)
```

to

``` java
if (AddressProtocol == AddressProtocol.IPv6)
```
