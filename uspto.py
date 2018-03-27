from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tqdm import tqdm
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

obj = {}
obj['+string+'] = []

def crawl(string):
	# string = "Bank of America"
	term1.send_keys(string)
	field1 = browser.find_element_by_xpath("//select[@name=\"FIELD1\"]/option[9]").click()
	term1.find_element_by_xpath("//input[@value ='Search']").click()



# 用頁數翻頁
soup = BeautifulSoup(browser.page_source, "html.parser")
# data_page = http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p='+page+'&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='+string+'&FIELD1=AANM&co1=AND&TERM2=&FIELD2=&d=PTXT

# site = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p='
# site_page_number = '\'+page+\''
# site_rest = '&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=\'+string+\'&FIELD1=AANM&co1=AND&TERM2=&FIELD2=&d=PTXT'
# site_url = site + site_page_number + site_rest

def get_ptno():
	for ele in browser.find_elements_by_xpath("/html/body/table/tbody/tr/td[2]/a"):
		addItem = {'patent number': ele.text}
		obj['+string+'].append(addItem)
		print(ele.text)

def dump_json():
	with open(''+string+'.json', 'w') as f:
		json.dump(obj, f, ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == "__main__":
	string = str(sys.argv[1])
	crawl(string)
	get_ptno()
	dump_json()