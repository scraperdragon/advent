import requests
import cookie
def get_input(url):
    cookie_crumbs = cookie.cookie.partition('=') # ("session", "=", "...")
    cookie_dict = {cookie_crumbs[0]: cookie_crumbs[2]}
    return requests.get(url, cookies=cookie_dict).text
