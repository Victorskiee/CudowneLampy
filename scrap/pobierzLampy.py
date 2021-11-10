from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.cudownelampy.pl"

productNames = []
links = []
categories = []
good = 0
bad = 0
Request = requests.get(url).text
soup = BeautifulSoup(Request,'html.parser')
divs = soup.find_all("div",{"class":"lamp-cats-single"})
iterator = 11
for div in divs:
	iterator = iterator -1
	if iterator < 0:
		break
	categories.append(div.find("a").get('href')[:-5])
	links.append(url + "/" + div.find("a").get('href'))

#print(len(links))
iterator = 0
for link in links:
	Request = requests.get(link).text
	soup = BeautifulSoup(Request,'html.parser')
	productsOneTheWebsite = soup.find_all("li",{"class":"productList-item"})
	#print(len(productsOneTheWebsite))
	singleProductlinks = []
	i = 180
	for productOneTheWebsite in productsOneTheWebsite:
		i = i - 1
		if i < 0:
			break
		singleProductlinks.append(url + "/" + productOneTheWebsite.find("a").get('href'))
	for singleProductlink in singleProductlinks:

		RequestV2 = requests.get(singleProductlink).text
		soup = BeautifulSoup(RequestV2,'html.parser')
		thisProduct = []

		try:
			name = soup.find("h1").text
			photo = soup.find("div",{"id":"body"})
			photo2 = url + "/" + photo.find("img").get('src')
			thisProduct.append("")
			price = soup.find("div",{"class":"col-xs-6 product-price"})
			price2 = price.find("strong").get('content')
			thisProduct.append("")

			description = soup.find("div",{"id":"productDescription"})
			desc = str(description)[68:]
			desc = desc[:-6]
			thisProduct.append(desc)

			thisProduct.append(categories[iterator])

			prod = {"productName":name,"photo":photo2,"price":price2,"description":desc, "category": categories[iterator]}

			productNames.append(prod)
			good = good + 1
		except:
			bad = bad + 1
			#desc = [i.string for i in desc]
			#print(description)
			#productNames.append(description)
		#products.append(productNames)
	iterator = iterator + 1

df = pd.DataFrame(productNames)
df.to_csv("scraped.csv", encoding="utf-8", header=True)
print("good scraps: " + str(good))
print("bad scraps: " + str(bad))

#print(productsOneTheWebsite)





