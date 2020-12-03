from requests import get, delete, post, put, patch
from bs4 import BeautifulSoup
import json

url = "https://www.mebelshara.ru/contacts"
res = get(url)
res.status_code

soup = BeautifulSoup(res.text)

list = []
#city = {}
#city['key'] = 'value'
phone = []
latlon = []
itog_time = []

for i in soup.find_all("div", {"class":"city-item"}):
    #city.clear()
    k = i.find("h4", {"class":"js-city-name"}).text
    m = k 
    m = {}
    m["address"] = k
    
    for j in i.find("div",{"class":"shop-list"}):
        address = j.find("div", {"class":"shop-address"}).text
        a = address + k
        a = {}
        a["address"] = k + ", " + address
        
        lat = j.get("data-shop-latitude")
        lon = j.get("data-shop-longitude")
        latlon.append(float(lat))
        latlon.append(float(lon))
        a["latlon"] = latlon

        name = j.find("div", {"class":"shop-name"}).text
        a["name"] = name
        
        phonee = j.find("div", {"class":"shop-phone"}).text
        phone.append(phonee)
        a["phone"] = phone
        
        weekends = j.find("div", {"class":"shop-weekends"}).text
        new_weekends = weekends.replace("Время работы:", "")
        time = j.find("div", {"class":"shop-work-time"}).text
        if time == "Без выходных:" or "Без выходных":
            time_itog = "пн - вс " + new_weekends
        else :
            time_itog = new_weekends + " " + time
        itog_time.append(time_itog)
        a["working_hours"] = itog_time
        
                
        list.append(a)
        phone = []
        latlon = []
        itog_time = []

print(list)

with open('D:/website_1.json', 'w') as f:
    json.dump(list, f)