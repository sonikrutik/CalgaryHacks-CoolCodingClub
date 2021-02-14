import mechanize
from bs4 import BeautifulSoup
import urllib3
import cookiejar


cj = cookiejar.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_refresh(False)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


br.open("https://login.ualberta.ca/module.php/core/loginuserpass.php")

br.select_form(nr=0)

br.form['username'] = 'nibras'
br.form['password'] = 'uofaisbae21!'
br.submit()

br.select_form(nr=0)
br.submit()

response = br.response().read()
print(response)