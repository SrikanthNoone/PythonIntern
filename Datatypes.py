Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(type(10))
<class 'int'>
>>> print(3.14)
3.14
>>> print(type(10))
... 
<class 'int'>
>>> print(type(10))
<class 'int'>
>>> print(type(3.14))
<class 'float'>
>>> print(type(1+3j))
<class 'complex'>
>>> print(type("Ignitz"))
<class 'str'>
>>> print(type([1,2,3]))
<class 'list'>
>>> print(type('name':'Ignitz'))
SyntaxError: invalid syntax
>>> print(type({'name':'Ignitz'}))
<class 'dict'>
>>> print(type({9.4,3.14,2.7}))
<class 'set'>
>>> print(type((9.14,3.14,2.7)))
<class 'tuple'>
