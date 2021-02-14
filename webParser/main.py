from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
#import parsingFunctions

def login(driver, url, username, password):
    driver.get(url)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("user_pass").send_keys(password)
    driver.find_element_by_css_selector
    driver.find_element_by_class_name("btn-default").click()
    coursePage_html = driver.page_source
    return coursePage_html

def parsePage(linkText):
    print("Penis")

if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())

    print("Opening eClass Login Page")
    url = "https://eclass.srv.ualberta.ca/my/"
    username = "nibras"
    password = "uofaisbae21!"
    coursePage_html = login(driver, url, username, password)

    print("Obtaining Courses")
    courseTitlesSoup = BeautifulSoup(coursePage_html, "lxml")
    courseTitles = courseTitlesSoup.find_all("h3", class_ = "title")
    
    for i in range(0, len(courseTitles)):
        
        courseTitleText = courseTitles[i].text.split()[:2]

        linkTextSoup = courseTitles[i]
        linkText = linkTextSoup.find("a")["href"]
        
        print(f"Course: {courseTitleText[0]} {courseTitleText[1]}\nLink: {linkText}\n")
        #parsePage(linkText)
    


    #time.sleep(60)
    driver.quit()
