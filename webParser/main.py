import os
import requests
from bs4 import BeautifulSoup


# using the loginuserpass.php thing
# https://medium.com/better-programming/web-scraping-behind-authentication-with-python-be5f82eb85f0
import requests

headers = {
    'authority': 'login.ualberta.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'origin': 'https://login.ualberta.ca',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://login.ualberta.ca/module.php/core/loginuserpass.php?AuthState=_325281c3cb8b88f31bd408dd999ca3f3b7f166a85d%3Ahttps%3A%2F%2Flogin.ualberta.ca%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Feclass.srv.ualberta.ca%252Fsp%26RelayState%3Dhttps%253A%252F%252Feclass.srv.ualberta.ca%252Flogin%252Findex.php%26cookieTime%3D1613264195',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'clive-visitor-tid-162=WmEdltlJxcBwaifWpgOe73ReFRYVAPaGKDcUhj2Vjpx5JDteXwpGHfmui0S4sWCR; _hjid=6a45b435-a93d-4126-a98d-ff9b207fa5f5; programs#lang=en; km_ai=y91ZKrWAWDYO1VOUGfmiKGDXLe0%3D; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=1075005958%7CMCIDTS%7C18411%7CMCMID%7C52888316552888283521391011674776808552%7CMCAAMLH-1591302746%7C9%7CMCAAMB-1591302746%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1590705146s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1; amplitude_id_1d890e80ea7a0ccc43c2b06438458f50ualberta.ca=eyJkZXZpY2VJZCI6IjE2MDgzYjc4LTUzYWUtNDcxNy05OTU3LTAyNDFlY2Q1ZTM5YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MDY5Nzk1MDU5NiwibGFzdEV2ZW50VGltZSI6MTU5MDY5Nzk2MzY4NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjF9; s_pers=%20c19%3Dbpdg%253Air_etd%253Aarticle%7C1590699750894%3B%20v68%3D1590697950157%7C1590699750902%3B%20v8%3D1590697963773%7C1685305963773%3B%20v8_s%3DFirst%2520Visit%7C1590699763773%3B; amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmualberta.ca=eyJkZXZpY2VJZCI6ImQ0Mzg3MzJkLTEyMmYtNDM4OC1hOGEzLWMwYmRmNDFhNmQ2MFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MDk3MzY3NjA2MCwibGFzdEV2ZW50VGltZSI6MTU5MDk3MzcxNDY2MywiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6NTEsInNlcXVlbmNlTnVtYmVyIjo1MX0=; amplitude_id_408774472b1245a7df5814f20e7484d0ualberta.ca=eyJkZXZpY2VJZCI6ImFmMzNmNmJiLTVmN2EtNDRhMS1iMTVhLWVkMDA3YWMxODZiYSIsInVzZXJJZCI6bnVsbCwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTkwOTczNjc2MDgxLCJsYXN0RXZlbnRUaW1lIjoxNTkwOTczNzI4MzM3LCJldmVudElkIjoyMTUsImlkZW50aWZ5SWQiOjE3Miwic2VxdWVuY2VOdW1iZXIiOjM4N30=; _fbp=fb.1.1600373915872.2087452950; _vwo_uuid_v2=DA6C32B54CD75D7B0B9F4A58E7CA2A8F9|d53d9052835ea9ad9972d6494e85f1a4; fpestid=ZL-Fl0iLwNq_DMmnCBvl1MGFy-Ajn3AO2BkgrLPFJp_IFcKp5s5S4p32RJoh5a2gEfSssw; _gcl_au=1.1.2101063032.1607393098; _scid=a9fc5542-9cf0-497e-a9f7-2f3261ba629b; __utma=87648711.6914344.1589413640.1589413640.1608152244.2; __utmz=87648711.1608152244.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); coveo_visitorId=0bfb05dc-a11b-45b4-9641-7f3834b390e3; ABTasty=uid=jma4x2cq0yth5rx7&fst=1610344184265&pst=-1&cst=1610344184265&ns=1&pvt=1&pvis=1&th=657688.815850.1.1.1.1.1610344184486.1610344184486.1; calltrk_referrer=direct; calltrk_landing=https%3A//www-conferenceboard-ca.login.ezproxy.library.ualberta.ca/e-Library/default.aspx; optimizelyEndUserId=oeu1610588511532r0.621477888157391; optimizelySegments=%7B%22757067938%22%3A%22direct%22%2C%22778703350%22%3A%22false%22%2C%22781081607%22%3A%22gc%22%2C%22949601412%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; mp_fe42a3507c097e9a9d1e9f881d833cfb_mixpanel=%7B%22distinct_id%22%3A%20%22176fe8e7e1dc4-07ddcbc1b46844-31346d-1fa400-176fe8e7e1eba2%22%2C%22%24device_id%22%3A%20%22176fe8e7e1dc4-07ddcbc1b46844-31346d-1fa400-176fe8e7e1eba2%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fproquest-safaribooksonline-com.login.ezproxy.library.ualberta.ca%2Fredirect%3Fredirectpage%3D%252fbook%252fsoftware-engineering-and-development%252fobject%252f0596008678%26key%3D%26sessionid%3Db2fa94a3-f72f-4497-b858-b1d9f38c81f6%26ref%3DUndefined%26oref%3D-%26a%3D%26xmlid%3D0596008678%26portal%3Dproquest%22%2C%22%24initial_referring_domain%22%3A%20%22proquest-safaribooksonline-com.login.ezproxy.library.ualberta.ca%22%7D; _ce.s=v~ae0af364eacd65a9563a1b9fba16a674282828f1~vv~2~ir~1; km_lv=x; _sctr=1|1611471600000; __unam=94c97c-1720f86d95f-24935a0e-64; _ga_4813X07MBG=GS1.1.1612812694.11.1.1612812727.0; _ga=GA1.1.1134580913.1588884578; SimpleSAMLSessionID=7716d21eb9b1321af41415787816b8fa; SimpleSAMLAuthToken=_48da6546566e0106ebb0fa262608d01821ea8d815a',
}

data = {
  'AuthState': '_325281c3cb8b88f31bd408dd999ca3f3b7f166a85d:https://login.ualberta.ca/saml2/idp/SSOService.php?spentityid=https%3A%2F%2Feclass.srv.ualberta.ca%2Fsp&RelayState=https%3A%2F%2Feclass.srv.ualberta.ca%2Flogin%2Findex.php&cookieTime=1613264195',
  'raa': 'continue',
  'username': 'nibras',
  'password': 'uofaisbae21!'
}

#
#url = "https://login.ualberta.ca/module.php/core/loginuserpass.php?AuthState=_e10c0ea7a07129088a5db4203d261c05697e52947c%3Ahttps%3A%2F%2Flogin.ualberta.ca%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Feclass.srv.ualberta.ca%252Fsp%26RelayState%3Dhttps%253A%252F%252Feclass.srv.ualberta.ca%252Flogin%252Findex.php%26cookieTime%3D1613260401"
url2 = "https://eclass.srv.ualberta.ca/my/"
url1 = "https://login.ualberta.ca/module.php/core/loginuserpass.php"

#s = requests.Session()
#response = s.post(url, headers=headers, data=data)#, cookies=cookies)
requests.post(url1, headers=headers, data=data)
response = requests.get(url2)
#response = s.post(url, data=data, cookies=cookies, allow_redirects=False)#headers=headers)


"""
# tab must be open
# https://www.youtube.com/watch?v=BZMVoYhA7KU
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager
"""


soup = BeautifulSoup(response.text, "lxml")
courseTitles = soup.find_all("div")#, class_ = "course_title")
#courseTitles = soup.find_all("h1", class_ = "fs-headline1 ow-break-word mb8 grid--cell fl1")
print(courseTitles)


"""
# from main video about BeautifulSoup

coursePage_html = requests.get("https://eclass.srv.ualberta.ca/my/", auth=('nibras', 'uofaisbae21!')).text
#coursePage_html = requests.get("https://stackoverflow.com/questions/27790415/set-lxml-as-default-beautifulsoup-parser").text
soup = BeautifulSoup(coursePage_html, "lxml")
courseTitles = soup.find_all("div")#, class_ = "course_title")
#courseTitles = soup.find_all("h1", class_ = "fs-headline1 ow-break-word mb8 grid--cell fl1")
print(courseTitles)
"""


