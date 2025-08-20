---
title: Python List Comprehension and Sets
date: 2015-01-29T05:18:00-06:00
author: bryan
category: Blog
tags: ["Python"]
slug: python-list-comprehension-and-sets
status: published
---

# Python List Comprehension and Sets

I work for a company that does GIS work, and over the past week or so
I\'ve been working on a script that does a lot of different things. One
of it\'s subroutines deletes data from Oracle.

First I was told (or I interpreted) it was safe to delete everything
from the Oracle connection. So this is similar to my first stab at the
code that deletes data from Oracle.

``` python
import arcpy

arcpy.env.workspace = r"c:\oracle_connection.sde" # file that holds all the connection info
for item in arcpy.ListTables() + arcpy.ListFeatureClasses() + arcpy.ListDatasets():
    arcpy.Delete_management(item)
```

One of the neat things about python is the ease at which lists can be
pulled together. Simply use the + operator!

The code above lists all tables, feature classes, and datasets. If
you\'re unfamiliar with ArcGIS, a feature class is simply a table that
has a shape related to each row. A dataset is a container for feature
classes.

When I ran the above code in my test environment, data was deleted from
some tables that were owned by a different user than what was specified
in the sde connection file. Apparently when tables, feature classes and
datasets are listed it\'s not just limited to the current user. This
could be particularly problematic if the connection user has permissions
to delete all tables. My solution was to only list tables that started
with the database user followed by a period.

``` python
import arcpy

arcpy.env.workspace = r"c:\oracle_connection.sde" # file that holds all the connection info
desc = arcpy.Describe(arcpy.env.workspace)
dbo = desc.connectionProperties.user.upper()

tables = [x.upper() for x in arcpy.ListTables() if x.upper().startswith(dbo + ".")]
feature_classes = [x.upper() for x in arcpy.ListFeatureClasses() if x.upper().startswith(dbo + ".")]
datasets = [x.upper() for x in arcpy.ListDatasets() if x.upper().startswith(dbo + ".")]

for item in tables + feature_classes + datasets:
    arcpy.Delete_management(item)
```

| Did you see that? \[x.upper() for x in arcpy.ListTables() if
  x.upper().startswith(dbo + \".\")\]
| This is what is known as a list comprehension. It\'s similar to C#\'s
  LINQ. If this were a C# list, this would be written as var tables =
  arcpy.ListTables().Select(x=\>x.ToUpper()).Where(x=\>x != dbo)

So what now? Well as it turns out we only wanted to delete pre-approved
tables and feature classes and we were not concerned with datasets. So I
added the tables and feature classes into configuration and I did
intersections with the lists.

``` python
import arcpy

def delete(tables, feature_classes):
    """@param tables: list of unqualified tables that we will drop"""
    """@param feature_classes: list of unqualified feature classes that we will drop"""
    """@type tables: [str]"""
    """@type feature_classes: [str]"""
    arcpy.env.workspace = r"c:\oracle_connection.sde" # file that holds all the connection info
    desc = arcpy.Describe(arcpy.env.workspace)
    dbo = desc.connectionProperties.user.upper()

    deletable_tables = [dbo + "." + x.upper() for x in tables]
    deletable_features = [dbo + "." + x.upper() for x in feature_classes]

    tables_in_db = [x.upper() for x in arcpy.ListTables() if x.upper().startswith(dbo + ".")]
    features_in_db = [x.upper() for x in arcpy.ListFeatureClasses() if x.upper().startswith(dbo + ".")]

    # if the table is in the list of preapproved tables
    # and the table actually exists
    # we want to delete it
    tables_to_delete = list(set(deletable_tables) & set(tables_in_db))
    features_to_delete = list(set(deletable_features) & set(features_in_db))

    for item in tables_to_delete + features_to_delete:
        arcpy.Delete_management(item)
```

So there you have it a real world problem solved by list comprehensions
and sets.
