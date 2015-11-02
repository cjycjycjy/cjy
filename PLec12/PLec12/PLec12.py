#encoding:cp949
import re
import os
import glob
import urllib
import urllib.request

str = '''Window
Unix
Linux
Solaris'''
p = re.compile('^.+',re.M)
print(p.findall(str))
print(p.search(str))

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)",
"Malcolm Reynolds")
print(m.group('first_name', 'last_name'))
print(m.groups())
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""

entries = re.split("\n",text)
result = [re.split(":?",entry,4) for entry in entries]
print(result)

with urllib.request.urlopen('http://www.naver.com/') as f:
    t = f.read().decode("utf-8")
    p = re.compile("(?<=<title>).+(?=<)")
    m = p.search(t)
    print(m)
