# from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

chromedriver = '/Users/Denny/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
soup = BeautifulSoup(browser.page_source, "lxml")
browser.get('http://patft.uspto.gov/netahtml/PTO/search-bool.html')

term1 = browser.find_element_by_name("TERM1")
term1.clear
field1 = browser.find_element_by_name("FIELD1")
field1.clear

str = 'International Business Machines'
term1.send_keys(str)
field1 = browser.find_element_by_xpath("//select[@name=\"FIELD1\"]/option[9]").click()
term1.find_element_by_xpath("//input[@value ='Search']").click()

soup = BeautifulSoup(browser.page_source, "lxml")
# for a in soup.find_all('a', href=True):
#     print("Found the URL:", a['href'])
# while len(soup.select(".html body center[2] table tbody tr td a[1]")) > 0:
# 	for ele in browser.find_elements_by_xpath("/html/body/table/tbody/tr"):
# 	# /html/body/table/tbody/tr[3]/td[2]
# 		print(ele.text)
# browser.find_element_by_partial_link_text('Next').click()
time.sleep(2)
# 	soup = BeautifulSoup(browser.page_source, "lxml")


# browser.find_element_by_tag_name("input").click()
# browser.find_element_by_id("trm1").click()
