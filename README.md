## Address Matcher Program

### Description

Purpose of this python program is to test out python lib
called 'fuzzywuzzy' to find best matching address.

### Requirements

1. Python 3.x


### How to run this program

1. This project has two sample csv files. file1.csv and file2.csv
   
2. Run command ``` python address_matcher.py```

When you will run this command, program reads the address from file1.csv and try to
find the best matching address from file2.csv. Current proram
is hard coded to check if ratio is 90 or higher then only it will
consider best match. Change it as per your need.

Reference of this program can be found in this article which explains it best.

https://www.datacamp.com/community/tutorials/fuzzy-string-python