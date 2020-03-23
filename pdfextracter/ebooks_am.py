from selenium import webdriver
from bs4 import BeautifulSoup
import wget

homelink = "/home/john/Dsprojm/ALSA-Armenian_Language_Sentiment_Analysis-" + "/pdfextracter/pdfs"

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": homelink}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    "../drivers/chromedriver", options=chrome_options
)

driver.get('https://ebooks.am/login')
driver.find_element_by_xpath("//input[@name='username']").send_keys('yedix92044@mailernam.com')
driver.find_element_by_xpath("//input[@name='password']").send_keys('123456456123')
driver.find_element_by_xpath("//input[@type='submit']").click()

soup = BeautifulSoup(BeautifulSoup(driver.page_source,'html.parser').prettify(),'html.parser')
allbooks = [i.get('href') for i in soup.find_all("a") if 'book/' in i.get('href')]

for book in allbooks:
    driver.get('https://ebooks.am/'+book)
    driver.find_element_by_xpath("//a[contains(@href,'/download/')]").click()