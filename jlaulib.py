import urllib.request
import urllib.parse
import http.cookiejar

lib_login = 'http://202.198.5.136:8080/reader/redr_verify.php'

cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)

postDict = {
    'number':'2012002855',
    'passwd':'2012002855',
    'select':'cert_no',
    'returnUrl':''
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(lib_login, postData)
data = op.read()
print(data.decode())
"""
#-----------------------------GetLibNum-------------------------------#
class GetLibNum(object):
    def __init__(self, number, passwd):
        self.number = number
        self.passwd = passwd

    def makeCookie(self):
        self.cookiejar = http.cookiejar.CookieJar()
        self.cookiepro = urllib.request.HTTPCookieProcessor(self.cookiejar)
        opener = urllib.request.build_opener(cookiepro)
        self.op = opener.open(lib_login)
        
    def makePostData(self):
        postDict = {
            'number' : self.number,
            'passwd' : self.passwd,
            'select' : 'cert_no',
            'returnUrl' : ''
        }
        
        postData = urllib.parse.urlencode(postDict).encode()
        return postData
"""
























