import requests

#postLoginURL = "https://login.ualberta.ca/module.php/core/loginuserpass.php"
postLoginURL = "https://login.ualberta.ca/saml2/idp/SSOService.php?spentityid=https%3A%2F%2Feclass.srv.ualberta.ca%2Fsp&amp;RelayState=https%3A%2F%2Feclass.srv.ualberta.ca%2Flogin%2Findex.php&amp;cookieTime=1613264113"
requestURL = "https://eclass.srv.ualberta.ca/my/"

payload = {
    "username": "nibras",
    "user_pass": "uofaisbae21!"
}

with requests.Session() as session:
    post = session.post(postLoginURL, data=payload)
    r = session.get(requestURL)
    print(r.text)