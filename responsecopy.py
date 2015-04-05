import tempfile
#__all__ 用于在import * 语法时指定这个模块中被“全部”包含进去的属性和方法，没有在这个列表
#中的将不会被导入
__all__ = ['addbase', 'addclosehook', 'addinfo', 'addinfourl']

class addbase(tempfile._TemporaryFileWrapper):
    def __init__(self, fp):
        super(addbase, self).__init__(fp, '<urllib response>', delete = False)
        self.fp = fp

    def __repr__(self):
        return '<%s at %r whose fp = %r>' % (self.__class__.__name__,
                                             id(self), self.file)

    def __enter__(self):
        if self.fp.closed:
            raise ValueError("I/O operation on closed file")
        return self

    def __exit__(self, type, value, traceback):
        self.close()



class addclosehook(addbase):
    def __init__(self, fp, closehook, *hookargs):
        super(addclosehook, self).__init__(fp)
        self.closehook = closehook
        self.hookargs = hookargs

    def close(self):
        if self.closehook:
            self.closehook(*self.hookargs)
            self.closehook = None
            self.hookargs = None
        super(addclosehook, self).close()





























