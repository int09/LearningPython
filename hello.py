#def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#        return -x

#try:
#    my_abs(1, 2)
#except TypeError:
#    print("This is a TypeError")


#def my_abs1(x):
#    if not isinstance(x, (int, float)):
#        raise TypeError('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x
    
#my_abs1('a')


#import math
#def move(x, y, step, angle = 0):
#    nx = x + step * math.cos(angle)
#    ny = y - step * math.sin(angle)
#    return nx, ny

#x, y = move(100, 100, 50, math.pi / 6)
#print(x, y)

#关键字参数的使用
#def person(name, age, **kw):
#    print('name:', name, 'age:', age, 'other:', kw)

#person('Jack', 30, gread = '3', suit = 'Jak')

#def calc(numbers):
#    sum = 0
#    for n in numbers:
#        sum += n * n
#    return sum

#print(calc([1, 3, 5, 7]))

#可变参数的使用
#def calc(*nums):
#    sum = 0
#    for n in nums:
#        sum += n * n
#    return sum

#print(calc(1, 2, 3))
#print(calc(1, 3, 5, 7))

#class Student(object):
#    def __init__(self, name, score):
#        self.name = name
#        self.score = score
#    def print_score(self):
#        print('%s: %s' %(self.name, self.score))

#me = Student('Jack', 89)
#me.print_score()

#在成员前加上'__'就将此成员声明为私有成员，私有成员不支持通过对象的直接访问
#class Student(object):
#    def __init__(self, name, score):
#        self.__name = name
#        self.__score = score
#    def print_score(self):
#        print('%s: %s' % (self.__name, self.__score))

#stu = Student('Jack', 90)
#stu.print_score()
#print(stu.__name)
#print(stu.__score)
#OK, 现在的Student类如果直接创建对象访问__name和__score成员，则会报错，并抛出
#AttributeError: 'Student' object has no attribute '__name'，这个异常

#对这两个成员的访问一般通过get和set方法来实现，但是可以在get和set方法中加入检查类型
#以及其他的附加语句使得程序更加健壮
"""
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError('__score is must a int or float')
        self.__score = score
    def get_name(self):
        return self.__name
    def set_name(self, name):
        if not isinstance(name, (str)):
            raise TypeError('__name is must a string')
        self.__name = name
"""
#提供了这样的机制是因为Python解释器将__name更名为_Student__name，你仍可以通过
#stu._Student__name这样的方式去访问它而不出任何错误
#stu = Student('Jack', 90)
#print(stu._Student__name)
#输出结果是   Jack
"""
class animal(object):
    def run(self):
        print('Animal running!!!')

class dog(animal):
    def run(self):
        print('dog is running!!!')
class cat(animal):
    def run(self):
        print('cat is running!!!')
"""
#tom = cat()
#tom.run()
#goffy = dog()
#goffy.run()

#子类与父类都有相同名字的方法，此处运行时调用了子类的方法，覆盖了父类的函数
#print(isinstance(tom, animal))
#print(isinstance(goffy, animal))
#def print_animal(*animal):
#    for ani in animal:
#       print(ani.run())

#print_animal(tom, goffy)

#通过接受animal的不论是继承其或者其类型的对象，都能通过运行时动态识别来准确调用方法
#传入一个animal对象输出animal对象定义的方法，dog对象输出dog对象的方法而不会输出animal

#dir()可以获得函数的全部属性和方法
#print(dir(animal))输出了如下的方法以及属性
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#'__subclasshook__', '__weakref__', 'run']
#

"""
from multiprocessing import Process
import os
#This is the code that the child process using
def run_proc(name):
    print('child process %s (%s)..' % (name, os.getpid()))
if __name__ == '__main__':
    print('parent process %s. '% os. getpid())
    p = Process(target = run_proc, args = ('test', ))
    print('process will start')
    p.start()
    p.join()
    print('process ended. ')
"""



#--------------------------------------------------------------------------------
#网络上某人写的一个用来获取piratebay视频资源的爬虫，其代码如下，逐行分析之
"""
# coding: utf8
import urllib2              #这个现在已经被包含到了urllib.request中
import re                   #正则表达式的模块
import pymongo              #提供对mongodb的调用

db = pymongo.Connection().test      #数据库的连接
url = 'http://piratebay.se/browse/200/%d/3'     #定义该URL
#compile这个正则表达式对象，将pattern写入这个对象
find_re = re.compile(r'<tr>.+?\(.+?">(.+?)</a>.+?class="detLink".+?">(.+?)</a>.+?
            <a href="(magnet:.+?)" .+?已上传 <b>(.+?)</b>, 大小 (.+?),', re.DOTALL)

# 定向爬去10页最新的视频资源
for i in range(0, 10):
    u = url % (i)           #format URL中的那个 %d ，用这个i来替代具体的页数
    # 下载数据
    html = urllib2.urlopen(u).read()    #用urllib2的urlopen打开这个URL然后read之
    # 找到资源信息
    for x in find_re.findall(html):     #findall方法将所有匹配的字串以列表形式返回
        values = dict(          #创建一个字典对象，并将其保存到数据库
            category = x[0],
            name = x[1],
            magnet = x[2],
            time = x[3],
            size = x[4]
        )
        # 保存到数据库
        db.priate.save(values)  #

print 'Done!'
"""































