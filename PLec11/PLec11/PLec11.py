#encoding:cp949
import re

#p = re.compile('ab*')#Result = p.match('abbbb')#p = re.match('ab*','abbbb')
#print(p)

#pattern = re.compile("o")
##result = pattern.search("dog")
#result = pattern.search("dog",2)##print(result)#result.group()#######################################
#pattern = re.compile("o")
#result = pattern.search("dog")
#print(result.group())
###########################################
#r = re.search(r"\\", "C:\\test")#print(r.group())#r = pattern.match("og")#print(r.group())######################################## 멀티라인 스트링#str = '''sample1.#sample2.#sampl23.'''#p = re.compile('.*$',re.S)#result = p.search(str)#print(result.group())################################str=" abc 1234 xyz "
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
#result = pattern.split('axbc')#result = re.sub(r'\W','','a:b:c, d.')#print(result)

###############################################

#str = '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)                       ####패턴에 ? 붙이면 최소 매칭을 찾는다. 
#print(result.group(1))########################################################################str = "123456-1234511"

pattern = re.compile('([0-9]{6})\W([0-9]{7})')
result = pattern.fullmatch(str)                     ## 패턴하고 완벽하게 일치해야 한다 .- fullmatch()
print(result.group(1))
print(result.group(2))




