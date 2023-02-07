import requests
from bs4 import BeautifulSoup
import openpyxl
import  re
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title="Dell_Lap"
sheet.append(["ProductName","Price"])
try:
    for a in range(1,13):

        req= requests.get(f"https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=740e60f6-cae4-4a9c-a6d0-83245064cb90&as-searchtext=lap&p%5B%5D=facets.brand%255B%255D%3DDELL&page={a}")
        soup = BeautifulSoup(req.content,"html.parser")
        main = soup.find_all("div",class_="_3pLy-c row")
        for i in main:
            ProductName=i.find("div",class_="_4rR01T").text
            Price = i.find("div",class_="_30jeq3 _1_WHN1").text
            Price = re.sub("\W","",Price)
            #print(ProductName,Price)
            sheet.append([ProductName,Price])
except:
    print("Error Occured")
excel.save("Flipkart.xlsx")
