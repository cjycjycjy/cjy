#encoding:cp949
import re

#p = re.compile('ab*')
#print(p)

#pattern = re.compile("o")
##result = pattern.search("dog")
#result = pattern.search("dog",2)
#pattern = re.compile("o")
#result = pattern.search("dog")
#print(result.group())
###########################################
#r = re.search(r"\\", "C:\\test")
#pattern = re.compile("\s*([a-zA-Z]+)\s+(\d+)+\s+([a-zA-Z]+)\s*");
##pattern = re.compile("([a-zA-Z]+)")
#result = pattern.search(str)
#print(result.group(1))
#print(result.group(2))
#print(result.group(3))
#print(result.group())

###################################################
#pattern = re.compile("o[gh]")
#result = pattern.fullmatch("og")

#result = pattern.fullmatch("ogre",0,2)
#result = pattern.fullmatch("doggie",1,3)

#print(result.group())
################################################
#pattern = re.compile("\W+")

#result = pattern.split('words, words, words.')
#result = pattern.split('words, words, words.',1)

#pattern = re.compile("x*")
#result = pattern.split('axbc')

###############################################

#str = '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)                       ####���Ͽ� ? ���̸� �ּ� ��Ī�� ã�´�. 
#print(result.group(1))

pattern = re.compile('([0-9]{6})\W([0-9]{7})')
result = pattern.fullmatch(str)                     ## �����ϰ� �Ϻ��ϰ� ��ġ�ؾ� �Ѵ� .- fullmatch()
print(result.group(1))
print(result.group(2))



