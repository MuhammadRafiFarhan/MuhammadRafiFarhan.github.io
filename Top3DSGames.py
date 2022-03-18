import json
import urllib.request
from selenium import webdriver
from datetime import datetime

this_time = datetime.now()
waktu = this_time.strftime("%d/%m/%y %H:%M:%S")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/games/score/metascore/all/3ds/filtered")

Best3DSGames = []
i = 1

for allgames in driver.find_elements_by_tag_name("tr"):
    print(allgames.text)
    for banner in allgames.find_elements_by_tag_name("a"):
        for img in banner.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))

            Best3DSGames.append(
                {"No": allgames.text.split("\n")[1],
                 "Title": allgames.text.split("\n")[2],
                 "Platform": allgames.text.split("\n")[3],
                 "Release_date": allgames.text.split("\n")[4],
                 "Rating": allgames.text.split("\n")[0],
                 'Waktu_scrapping':waktu,
                 "Image": img.get_attribute("src")
                 }
            )
hasil = open("D:\Tugas Scraping\scraping2\Top3DSGames.json", "w")
json.dump(Best3DSGames, hasil, indent = 6)
hasil.close()

driver.quit()