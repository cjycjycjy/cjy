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
print(m.groups())print(m.groupdict())m = re.match(r"(\d+)\.?(\d+)?","24")print(m.groups())print(m.groups(0))p = re.compile(".+(?=:)")m = p.search("http://google.com")print(m.group())#os.chdir("C:\\")#print(os.getcwd())#################이부분 모르겠다 glob으로 배치파일 실행파일 제외하고 뽑아내기#p = re.compile('.*[.](?!bat$|exe$).*$')#s = glob.glob("*.*")#print(s)###########p = re.compile("(?<=abc)def")m = p.search("abcdef")print(m.group())email = "tony@tiremove_thisger.net"m = re.search("remove_this",email)result = email[:m.start()] + email[m.end():]print(result)text = """Ross: McFluff: 834.345.1254: 155 Elm Street
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

