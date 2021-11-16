from bs4 import BeautifulSoup
import requests
import pandas as pd
import random as rand

url = "https://www.cudownelampy.pl"

id1 = 1
categoriesTab =[]
combinations = []
productNames = []
links = []
categories = []
good = 0
bad = 0
Request = requests.get(url).text
soup = BeautifulSoup(Request, 'html.parser')
divs = soup.find_all("div", {"class": "lamp-cats-single"})
iterator = 11
for div in divs:
    iterator = iterator - 1
    if iterator < 0:
        break
    categories.append(str(div.find("a").get('href')[:-5]).rstrip("0123456789,"))
    links.append(url + "/" + div.find("a").get('href'))

iterator = 11
categoryID = 3
for link in links:
    iterator -= 1
    if iterator < 0:
        break
    Request = requests.get(link).text
    soup = BeautifulSoup(Request, 'html.parser')
    category_description = soup.find("div", {"id": "pageDescription"})
    try:
        p = category_description.find("p").text
    except:
        p = ""

    category_link_formated = str(link).split("/").pop()[:-5].split(",")[0].replace("_", " ").replace("-", " ").replace("pl ", "")
    categoriesStructure = {"id": categoryID, "Name": category_link_formated, "description": p}
    categoriesTab.append(categoriesStructure)
    categoryID += 1
    # print(category_description)

# print(len(links))
iterator = 0
counter = 0
for link in links:
    Request = requests.get(link).text
    soup = BeautifulSoup(Request, 'html.parser')
    productsOneTheWebsite = soup.find_all("li", {"class": "productList-item"})
    # print(len(productsOneTheWebsite))
    singleProductlinks = []
    i = 80
    for productOneTheWebsite in productsOneTheWebsite:
        i = i - 1
        if i < 0:
            break
        singleProductlinks.append(url + "/" + productOneTheWebsite.find("a").get('href'))
    for singleProductlink in singleProductlinks:
        counter += 1
        print(counter)
        RequestV2 = requests.get(singleProductlink).text
        soup = BeautifulSoup(RequestV2, 'html.parser')
        thisProduct = []

        try:
            product_amount = rand.randint(1, 10)
            name = soup.find("h1").text
            photo = soup.find("div", {"id": "body"})
            photo2 = url + "/" + photo.find("img").get('src')
            thisProduct.append("")
            price = soup.find("div", {"class": "col-xs-6 product-price"})
            price2 = price.find("strong").get('content')
            thisProduct.append("")

            description = soup.find("div", {"id": "productDescription"})
            desc = str(description)[68:]
            desc = desc[:-6]
            thisProduct.append(desc)

            category_formated = str(categories[iterator]).replace("_", " ").replace("-", " ").replace("pl ", "")
            thisProduct.append(category_formated)

            prod = {"id": id, "productName": name, "photo": photo2, "price": price2, "description": desc,
                    "category": category_formated, "amount": product_amount}

            productNames.append(prod)
            good = good + 1
        except:
            bad = bad + 1
        # desc = [i.string for i in desc]
        # print(description)
        # productNames.append(description)
    # products.append(productNames)
        try:
            tmp_id = 1
            id_attributes = soup.find("select", {"id": "attributes"}).findChildren()
            for id_attribute in id_attributes:
                product_amount = rand.randint(1, 10)
                attribute_ntp = "Color: color: 0"
                color = id_attribute.text + ": 0"
                if color == "Wybierz kolor: 0":
                    product_amount = 0
                prod = {"id": id1, "tmp_id": tmp_id, "attribute_ntp": attribute_ntp,  "color": color, "amount": product_amount}
                combinations.append(prod)
                tmp_id += 1
            id1 += 1
        except:
            id1 += 1
            continue

    iterator = iterator + 1

cat_descriptions = pd.DataFrame(categoriesTab)
cat_descriptions.to_csv("categories.csv", encoding="utf-8", header=True, sep="&")
comb = pd.DataFrame(combinations)
comb.to_csv("combinations.csv", encoding="utf-8", header=True, sep="&")
df = pd.DataFrame(productNames)
df.to_csv("products.csv", encoding="utf-8", header=True, sep="&")
print("good scraps: " + str(good))
print("bad scraps: " + str(bad))

# print(productsOneTheWebsite)
