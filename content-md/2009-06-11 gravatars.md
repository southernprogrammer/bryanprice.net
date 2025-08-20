---
title: Gravatars
date: 2009-06-11T11:16:00-05:00
author: bryan
category: Blog
tags: ["avatar", " webaccount", " blogging"]
slug: gravatars
status: published
---

# Gravatars

Wow, I never knew about Gravatars until just now.  Everyone needs to go
to Gravatar.com and register an avatar that can be used across the web
on many websites (including this one).  The avatar is associated with
your email address and if a website uses Gravatar it just checks to see
if you have one setup on Gravatar.com.  If you look at comments on this
site you will now see avatars.  This is a really amazing idea!

Now if you have a wordpress blog and you want to incorporate Gravatars
into your template, I suggest you use this line of code in your comment
template.

``` php
<?php
  echo get_avatar( $id_or_email, $size = '96', $default = '<path_to_url>' );
?>
```

Replace \$id_or_email with \$comment (this is what I used) or with
get_the_author_id() (it varies from theme to theme), replace XX with the
size you want the images (I use 50 pixels), and replace
\'\<path_to_url\>\' with the absolute location of a custom default
avatar (in the case that the commenter didn\'t have a gravatar set).  If
you want to use the default avatar set in the Wordpress settings
(Settings-\>Discussion) you need to remove the default argument
completely.

Hope this was educational, and remember to sign up for a Gravatar!
