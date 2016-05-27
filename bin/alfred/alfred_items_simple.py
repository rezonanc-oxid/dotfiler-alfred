#!/usr/bin/env python

import sys
import fileinput

output="""
<?xml version="1.0"?>
<items>
{}
</items>
"""

items = fileinput.input()

items_output=[]

item_fmt='<item arg="{0}" valid="YES"><title>{1}</title></item>'

for item in items:
    a, b = item.strip().split("|")
    items_output.append(item_fmt.format(b, a))

items_output_string = "\n".join(items_output)

output_string = output.format(items_output_string)

print output_string
