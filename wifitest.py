import urllib.request
import urllib.parse
import http.cookiejar
import re

wifi_login = 'http://202.198.3.86/login_W8_2.asp'

def testit(username, passwordx):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    
    postDict = {
        'username':str(username)
        'passwordx':str(passwordx)
        'Submit':''
    }

    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(wifi_login, postData)
    data = op.read().decode()
    log_ok = False
    is_login = re.compile
    
    
