---
title: Coding Projects
date: 2008-04-27T22:54:00-05:00
author: bryan
slug: coding-projects
status: published
---

# Coding Projects

## Classroom Control System (CCS)

You may have heard about CCS in my blog post
[here](http://bryanprice.net/2009/07/31/ccs/), but here's a brief
description anyway.  CCS allows teachers to block websites and programs
on student computers (both blacklists and whitelists) as well as perform
other actions such as remote desktop.  The teacher software can be found
[here](http://files.bryanprice.net/CCS_Teacher_Installation_Extraction.exe)
and must be setup first.  The student software can be found
[here](http://files.bryanprice.net/CCS_Student_Installation_Extraction.exe)
and can be setup on multiple computers with the same configuration. 
Please visit the official project blog
[here](http://bryanprice.net/categories/ccs-project/).

## SageTV Rename

Many of you may remember that I wrote a script for BeyondTV ([BeyondTV
Renamer](http://bryanprice.net/coding-projects/)) that utilized a
command line tool that someone had written to create an XML file giving
detailed information about the given file.  My script compared the
airdate from this dumped XML file with airdates of matching shows on
TVRage.com to rename the files in such a way that XBMC or Boxee could
read the file and get the metadata (like show description and images).

Well today I'm releasing a script that I wrote that does something
similar for SageTV.  Technically speaking, it does not actually rename
the file.  It creates symlinks to the files named in such a way that
XBMC or Boxee can read the files and pickup the metadata.  And instead
of needing the command line tool, you need the SageTV Web Interface that
was written by Neilm.  By creating symlinks, it allows for only 1 true
copy of the file to exist and for the show to remain in SageTV and in
Boxee or XBMC.

[SageTV Rename](http://files.bryanprice.net/SageTVRename.zip)

## BTVRenamer

Okay, so here\'s the dilemma: [BeyondTV](http://www.snapstream.com/)
doesn\'t organize my TV shows in a way that [Boxee](http://Boxee.tv) or
[XBMC](http://xbmc.org/) can recognize my media.  So I wrote this
monster of a script.  All details should be available via the readme
file.  But it basically will reorganize your folder with the format
\"ShowName (YearStarted)ShowName.S##E## (EpisodeName).ext\". 
[BTVRenamer.zip](http://files.bryanprice.net/BTVRenamer.zip) Have fun
:-D
