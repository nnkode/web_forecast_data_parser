from bs4 import BeautifulSoup
import requests
import json

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# request web page
r = requests.get('https://www.accuweather.com/en/us/los-angeles/90012/weather-forecast/347625', headers=headers)

# get the response text. in this case it is HTML
html = r.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

# print the HTML as text
#print(soup.body.get_text().strip())

# get the a tags in a list
a_tags = soup.find_all("a", class_ = "daily-list-item")
#print(a_tags[0])

list_items = []

# iterate over a tags
for item in a_tags:
    date_tag = item.find("div", class_ = "date")
    day_tag = item.find("p", class_ = "day")

    # get the <p> tag inside the date_tag with just the date in it
    p_date_tag = date_tag.find("p", class_ = None)

    temp_tag = item.find("div", class_= "temp")
    temp_hi_tag = temp_tag.find("span", class_ = "temp-hi")
    temp_low_tag = temp_tag.find("span", class_ = "temp-lo")

    phrase_tag = item.find("div", class_= "phrase")
    phrase_1_tag = phrase_tag.find("p", class_="no-wrap")

    #create new dict
    dict = {}

    dict["day"] = day_tag.text
    dict["date"] = p_date_tag.text
    dict["temp_hi"] = temp_hi_tag.text
    dict["temp_low"] = temp_low_tag.text
    dict["phrase"] = phrase_1_tag.text
   
    list_items.append(dict)

''' #initial development of the problem by using loops instead of dictionaries 

    # iterate over every child of date tag and put them in a list
    for child in date_tag.children:
        # because \n was getting added to the list
        if child.text != '\n':
            list_items.append(child.text)

    for child in temp_tag.children:
        # because \n was getting added to the list
        if child.text != '\n':
            list_items.append(child.text)

    for child in phrase_tag.children:
        # because \n was getting added to the list
        if child.text != '\n':
            list_items.append(child.text)
'''
#print(list_items)

# convert the list of strings to single string by json
dump = json.dumps(list_items,indent=2)

