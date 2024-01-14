import csv
import requests
from bs4 import BeautifulSoup as BS
import os

# get data from this url
url = 'https://www.businesstoday.in/latest/economy'
# request to fetch all the data
full_webpage = requests.get(url)
# parse it to html using beautiful soup
data = BS(full_webpage.content, "html.parser")
index = 1
# write the daa into a csv file (append mode)
with open("data.csv", 'a') as file:
    csv_writer = csv.writer(file)
    # financial news are in 'a' tag, so we find all 'a' tags
    # find it using inspect
    for link in data.find_all('a'):
        # when printing the 'a' tags we see that we have to class : none and <class 'bs4.element.NavigableString'>
        # print(type(link.string), " , ", link.string)
        # select class <class 'bs4.element.NavigableString'> and select strings that have length of 35 or more
        # because it has some redundant data(some news with one word)
        if str(type(link.string)) == "<class 'bs4.element.NavigableString'>" and len(link.string) > 35:
            temp_str = str(index) + ". " + link.string
            csv_writer.writerow([temp_str])
            index += 1
# remove redundant double quotes
with open("data.csv") as file:
    for row in file:
        text = row
        text = ''.join([i for i in text]).replace('"', '')
        x = open("final_data.csv", "a")
        x.writelines([text])

# remove redundant file
os.remove('data.csv')
