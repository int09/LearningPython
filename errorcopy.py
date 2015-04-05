import urllib.response
#__all__属性指定了当from module import *时会被导入的属性方法，如果没有指定，那么导入所有
__all__ = ['URLError', 'HTTPError', 'ContentTooShortError']

class URLError(OSError):
    def __init__(self, reason, filename = None):
        self.args = reason,
        self.reason = reason
        if filename is not None:
            self.filename = filename
#str被print函数输出，当向print函数中传入这个对象时，该函数被调用返回给print
    def __str__(self):
        return '<urlopen error %s>' % self.reason

class HTTPError(URLError, urllib.response.addinfourl):
    __super_init = urllib.response.addinfourl.__init__
    def __init__(self, url, code, msg, hdrs, fp):
        self.code = code
        self.msg = msg
        self.hdrs = hdrs
        self.fp = fp
        self.filename = url

        if fp is not None:
            self.__super_init(fp, hdrs, url, code)

    def __str__(self):
        return 'HTTP Error %s: %s' % (self.code, self.msg)

#把类中的方法当作属性来访问
    @property
    def reason(self):
        return self.msg

    @property
    def headers(self):
        return self.hdrs

    @headers.setter
    def headers(self, headers):
        self.hdrs = headers



#exception raised when downloaded size does not match content length
#当下载的大小与内容长度不匹配时抛出该错误
class ContentTooShortError(URLError):
    def __init__(self, message, content):
        URLError.__init__(self, message)
        self.content = content

