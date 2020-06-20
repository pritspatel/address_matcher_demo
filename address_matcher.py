from fuzzywuzzy import fuzz
import csv


with open('data/file1.csv') as file1:
     reader = csv.DictReader(file1)
     for row in reader:
         addr1 = row['address']
         with open('data/file2.csv') as file2:
             reader2 = csv.DictReader(file2)
             for row in reader2:
                 addr2 = row['address']
                 ratio = fuzz.ratio(addr1,addr2)
                 if(ratio > 90):
                     print('Score : ' + str(ratio))
                     print('Found match : ' + addr2)