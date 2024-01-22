import requests
from bs4 import BeautifulSoup
import csv

rep = requests.get("https://lenouvelliste.com/")

tab_titles = []
tab_links = []
tab_img=[]
tab_descrip=[]

if rep.status_code == 200:
    tousText = rep.text
    soup = BeautifulSoup(tousText, "html.parser")

    titles = soup.find_all('title')
    if titles:
        for title in titles:
            tab_titles.append(title.text)

    links = soup.find_all('a', href=True)
    if links:
        for link in links:
            href = link['href']
            tab_links.append(href)

    images = soup.find_all('img', src=True)
    if images:
        for image in images:
            src = image['src']
            tab_img.append(src)

    descri = soup.find_all('meta', attrs={'name': 'description'})
    if descri:
        for descrip in descri:
            content = descrip.get('content', '')
            tab_descrip.append(content)

    with open('Fichier.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Type", "Contenu"])
        for title in tab_titles:
            csv_writer.writerow(["Title", title])
        for link in tab_links:
            csv_writer.writerow(["Lien", link])
        for image in tab_img:
            csv_writer.writerow(["Image", image])
        for descrip in tab_descrip:
            csv_writer.writerow(["Description", descrip])
else:
    print("Status_code != 200")
