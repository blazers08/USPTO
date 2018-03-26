from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import time
import sys

chromedriver = '/Users/Denny/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
soup = BeautifulSoup(browser.page_source, "html.parser")
browser.get('http://patft.uspto.gov/netahtml/PTO/search-bool.html')

term1 = browser.find_element_by_name("TERM1")
term1.clear
field1 = browser.find_element_by_name("FIELD1")
field1.clear

# def crawl(str):
str = "JPMorgan"
term1.send_keys(str)
field1 = browser.find_element_by_xpath("//select[@name=\"FIELD1\"]/option[9]").click()
term1.find_element_by_xpath("//input[@value ='Search']").click()

obj = {}
obj['patent'] = []


soup = BeautifulSoup(browser.page_source, "html.parser")


# while len(soup.select("#Next 50 Hits")) > 0:

for ele in browser.find_elements_by_xpath("/html/body/table/tbody/tr/td[2]/a"):
	addItem = {'patent number': ele.text}
	obj['patent'].append(addItem)
	print(ele.text)
# for ele1 in browser.find_elements_by_xpath("/html/body/table/tbody/tr/td[4]/a"):
# 	# /html/body/table/tbody/tr[3]/td[2]
# 	# /html/body/table/tbody/tr[2]/td[2]/a
# 	# /html/body/table/tbody/tr[3]/td[2]/a
# 	# /html/body/table/tbody/tr[2]/td[4]/a
# 	# /html/body/table/tbody/tr[4]/td[4]/a

# 	addItem = {'title': ele1.text}
# 	obj['patent'].append(addItem)
# 	print(ele.text)
# if len(browser.find_elements_by_xpath("/html/body/table/tbody/tr")) == 50:

	# next2 = browser.find_element_by_name("NextList2")
# browser.find_element_by_xpath("/html/body/form[1]/input[13]").click()
	# time.sleep(2)
	# soup = BeautifulSoup(browser.page_source, "lxml")

with open('patent.json', 'w') as f:
	json.dump(obj, f, ensure_ascii=False, sort_keys=True, indent=4)

# if __name__ == "__main__":
# 	str = str(sys.argv[1])
# 	crawl(str)

