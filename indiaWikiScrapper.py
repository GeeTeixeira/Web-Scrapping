'''
These libraries are used to download and parse html code
'''

from bs4 import BeautifulSoup as sp 
from urllib.request import urlopen
import xml

'''These are being used to arrange the data collected'''

import string
import re
import csv

url= "https://en.wikipedia.org/wiki/States_and_union_territories_of_India" # URL to collect
url_open = urlopen(url) #webbrowser to open the page
url_read = url_open.read() #collects html code as str
soup = sp(url_read,"html.parser") #parses str to actual html code (soup is the variable with all of the html code)
container = soup.findAll("div",{"class":"mw-content-ltr"}) # soup.findAll will look through the html code for these divs and class
containers = container[0] #it separetes in containers you must find which container your information is located or make a loop to find it
container2 = containers.findAll("table", {"class":"wikitable sortable plainrowheaders"}) #continue looking for html container of the location
container3 = container2[0].findAll("tr") #found the table the next loop will iterate 
for i in container3: #in this for loop, the program iterates through the columns of the table in wikipedia
    col = i.text.split("\n") #grabs the text in the html and split by \n 
    tmpList = [] #resets temp list
    for x in col:
        if(x != "" and x != '—'): #ignores empty elements and append to temp list
            tmpList.append(x)
    f = open('indiaWiki.csv','a') #creates/open new file in append mode
    for n in tmpList: #iterates through temp list
        #print(n)
        try:
            f.write(n) #writes it to file
            f.write(',') #moves to next column
        except UnicodeEncodeError: #exception handler for Unicode error
            print("error:", n)
    f.write('\n') # moves to next row
f.close()

