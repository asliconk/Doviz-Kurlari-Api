"""
verileri çektiğimiz internet siteleri
https://www.tcmb.gov.tr/kurlar/today.xml
https://docs.python.org/2/library/xml.etree.elementree.html

"""
import requests
import pip._vendor.requests 
import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "https://www.tcmb.gov.tr/kurlar/today.xml"
response = pip._vendor.requests.get(url=url)
print(response.text)
tree = ET.parse(urlopen(url))
root = tree.getroot()

liste = []
liste.append(root.findall('Currency'))

for i in liste[0]:
    currencyCode = i.get('Kod')
    banknoteBuying = i.find('BanknoteBuying').text
    banknoteSelling = i.find('BanknoteSelling').text
    ForexBuying = i.find('ForexSelling').text
    ForexSelling = i.find('ForexSelling').text 
    name = i.find("Isim").text
    
    if currencyCode =="USD":
            result = float(banknoteSelling) - float(banknoteBuying)
            print("Para birimi adi " + name)
            print("USD satis ", banknoteSelling)
            print("USD alis ", banknoteBuying)
            print("Banka alis satis arasindaki kur farki ->", str(result))
            print("*****************************************************")
            
    if currencyCode =="EUR":
            result = float(banknoteSelling) - float(banknoteBuying)
            print("Para birimi adi " + name)
            print("EUR satis ", banknoteSelling)
            print("EUR alis ", banknoteBuying)
            print("Banka alis satis arasindaki kur farki ->", str(result)) 
            print("*****************************************************")
            
    if currencyCode =="CHF":
            result = float(ForexSelling) - float(ForexBuying)
            print("Para birimi adi " + name)
            print("CHF satis ", ForexSelling)
            print("CHF alis ", ForexBuying)
            print("Banka alis satis arasindaki kur farki ->", str(result))
            print("*****************************************************")        
             
    if currencyCode =="QAR":
            result = float(ForexSelling) - float(ForexBuying)
            print("Para birimi adi " + name)
            print("QAR satis ", ForexSelling)
            print("QAR alis ", ForexBuying)
            print("Banka alis satis arasindaki kur farki ->", str(result))
            print("*****************************************************") 
            
              
            
       