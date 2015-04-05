#imports
import base64
import bisect
import email
import hashlib
import http.client
import io
import os
import posixpath
import re
import socket
import sys
import time
import collections
import tempfile
import contextlib
import warnings
#imports

from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import (
    urlparse, urlsplit, urljoin, unwrap, quote, unquote,
    splittype, splithost, splitport, splituser, splitpasswd,
    splitattr, splitquery, splitvalue, splittag, to_bytes,
    unquote_to_bytes, urlunparse)

from urllib.response import addinfourl, addclosehook

# check for SSL
try:
    import ssl
except ImportError:
    _have_ssl = False
else:
    _have_ssl = True

__all__ = [
    # Classes
    'Request', 'OpenerDirector', 'BaseHandler', 'HTTPDefaultErrorHandler',
    'HTTPRedirectHandler', 'HTTPCookieProcessor', 'ProxyHandler',
    'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm',
    'AbstractBasicAuthHandler', 'HTTPBasicAuthHandler', 'ProxyBasicAuthHandler',
    'AbstractDigestAuthHandler', 'HTTPDigestAuthHandler', 'ProxyDigestAuthHandler',
    'HTTPHandler', 'FileHandler', 'FTPHandler', 'CacheFTPHandler', 'DataHandler',
    'UnknownHandler', 'HTTPErrorProcessor',
    # Functions
    'urlopen', 'install_opener', 'build_opener',
    'pathname2url', 'url2pathname', 'getproxies',
    # Legacy interface
    'urlretrieve', 'urlcleanup', 'URLopener', 'FancyURLopener',
]

__version__ = sys.version[:3]

_opener = None
def urlopen(url, data = None, timeout = socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile = None, capath = None, cadefault = False):
    global _opener
    if cafile or capath or cadefault:
        if not _have_ssl:
            raise ValueError('SSL support not available')
        context = ssl._create_stdlib_context(cert_regs = ssl.CRET_REQUIRED,
                                             cafile = cafile,
                                             capath = capath)
        https_handler = HTTPHandler(context = context, check_hostname = True)
        opener = buile_opener(https_handler)
    elif _opener is None:
        _opener = opener = build_opener()
    else:
        opener = _opener
    return opener.open(url, data, timeout)





#------------------------------HTTPHandler-----------------------------
class HTTPHandler(AbstractHTTPHandler):
    def http_open(self, req):
        return self.do_open(http.client.HTTPConnection, req)
    http_request = AbstractHTTPHandler.do_request_

if hasattr(http.client, 'HTTPSConnection'):

    class HTTPSHandler(AbstractHTTPHandler):
        def __init__(self, debuglevel = 0, context = None, check_hostname = None)

#-----------------------------------------------------------------------

class Request:
    def __init__(self, url, data = None, headers={},
                 origin_req_host = None, unverifiable = False,
                 method = None):
        self.full_url = url
        self.headers = {}
        self.unredirected_hdrs = {}
        self._data = None
        self.data = data
        self._tunnel_host = None
        for key, value in headers.items():
            self.add_header(key, value)
        if origin_req_host is None:
            origin_req_host = request_host(self)
        self.origin_reqhost = origin_req_host
        self.unverifiable = unverifiable
        if method:
            self.method = method

    

















            






















