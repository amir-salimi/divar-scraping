
import requests
import time

from bs4 import BeautifulSoup
import requests.cookies

URL = "https://divar.ir/s/arak"


def url_get_data(link, advertisement):
    price_array = []
    price = None
    rent = None
    deposit = None
    ps = None
    rs = None
    ds = None
    card_page = requests.get(f"https://divar.ir{link}") # it request to each advertisement pages , for getting required data
    status = card_page.status_code
    each_soup = BeautifulSoup(card_page.content, "html.parser")
    # get title of each advertisement page
    title = each_soup.find(class_="kt-page-title__title kt-page-title__title--responsive-sized")
    # get description of each advertisement page 
    description = each_soup.find(class_="kt-description-row__text kt-description-row__text--primary")
    # get category of each advertisement page
    category = each_soup.find(class_="kt-breadcrumbs__action-text")
    # get advertisement detail of each advertisement page
    adver_detail = advertisement.find_all(class_="kt-post-card__description")
    # This is to get all the details of the advertisement and separate its price
    if adver_detail:
        for page in adver_detail:
            price_array.append(page.text)

        for i in price_array:
            if "تومان" in i:
                price = str(i)

                if "اجاره" in price :
                    rent = str(price)
                    # print(rent)

                if "ودیعه" in price:
                    deposit = str(price)
                    # print(deposit)
                price_array=[]

            if rent and deposit:
                rs = rent.split(" ")[1]
                ds = deposit.split(" ")[1]

            if price :
                ps = price.split(" ")[0]
        
            
    if rent and deposit is not None:
        return [title, description, category, ps, ds, rs]    
    else:
        return [title, description, category, ps, None, None]
    


def get_data():
    page = requests.get(URL) # it request to divar page and get all advertisement html content
    time.sleep(1)   # it make a delay to prevent too many request error
    if page.status_code == 429 : # it is for too many request error
        time.sleep(3)
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    for advertisement in soup.find_all(class_="post-list__widget-col-c1444"): # it get each advertisement from divar main page
        time.sleep(2)  # it make a delay to prevent too many request error
        link = advertisement.select_one('a').get("href") # it is for get all link of advertisement from divar main page
        data = url_get_data(link, advertisement)
        if data[0] and data[1] and data[2] and data[3]: # checking for valid data
            if data[4] and data[5] is not None:
                # if rent and deposit data exist it is running
                requests.get(f"http://0.0.0.0:8000/data/?title={data[0].text}&description={data[1].text}&category={data[2].text}&rent={data[5]}&deposit={data[4]}")
            else:

                requests.get(f"http://0.0.0.0:8000/data/?title={data[0].text}&description={data[1].text}&category={data[2].text}&price={data[3]}")
                
                

while True:
        data = get_data()
        


