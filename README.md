# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:57:28 2019

@author: zhen9978
"""

import csv
import functools
import re


fullCsvWithUrl = "out.csv"
targetFileWithFormat = "depth.txt"
depFlatList = []
hyperlink_format = '<a href="{link}">{text}</a>'
link_text = functools.partial(hyperlink_format.format)


with open(targetFileWithFormat,"r+") as f:
    content = f.read().splitlines()
#    print(content)

for item in content:
    itemName = item.replace(" ","")
    depFlatList.append(itemName)

with open(fullCsvWithUrl) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for depInfo in csv_reader:
        depName = depInfo[0]
        if depName in depFlatList:
            index = depFlatList.index(depInfo[0])
            depUrl = depInfo[2]
            licType = depInfo[1]
            licUrl =  depInfo[3]
            
            depWithLink = link_text(link=depUrl, text=depName)
            licWithLink = link_text(link=licUrl, text=licType)
            replaceText = depWithLink + ", " + licWithLink
#            print(content[index])
#            print(depName)
            print(re.sub(r'\b'+ depName, "- "+replaceText, content[index]))

    
f.close()
    
