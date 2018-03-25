# from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

chromedriver = '/Users/Denny/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
soup = BeautifulSoup(browser.page_source, "html.parser")
browser.get('http://patft.uspto.gov/netahtml/PTO/search-bool.html')
# browser.get('http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='+str+'&FIELD1=ASNM&co1=AND&TERM2=&FIELD2=&d=PTXT')
term1 = browser.find_element_by_name("TERM1")
term1.clear

str = 'International Business Machines'
term1.send_keys(str)
term1.find_element_by_xpath("//input[@value ='Search']").click()

soup = BeautifulSoup(browser.page_source, "lxml")
while len(soup.select(".html body center[2] table tbody tr td a[1]")) > 0:
	for ele in browser.find_elements_by_xpath("/html/body/table/tbody/tr"):
	# /html/body/table/tbody/tr[3]/td[2]
		print(ele.text)
	browser.find_elements_by_xpath('/html/body/center[2]/table/tbody/tr/td/a[1]').click()
	soup = BeautifulSoup(browser.page_source, "lxml")


# browser.find_element_by_tag_name("input").click()
# browser.find_element_by_id("trm1").click()
