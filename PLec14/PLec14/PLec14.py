from bs4 import BeautifulSoup
import json

#f = open('test.xml')
#xml = f.read()
#soup = BeautifulSoup(xml)
#for node in soup.findAll('node'):
#    print("Node : "+node.string)
#    print("Attr1 : "+node['attr1'])

#f.close()

#f = open('song.xml',encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml)
#for nodes in soup.test('song'):
#    for node in nodes:
#        print(node.string)

#for nodes in soup.findAll('song'):
#    print(nodes.title.string)
#    print(nodes.length.string)

#f.close()

#f = open('alcohol.xml',encoding = 'utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,'html.parser')
#for nodes in soup.alcohol('cate1'):
#    if nodes['tt'] == '안주':
#        print('Cate1 :'+nodes['tt'])
#        for node in nodes('cate2'):
#            print('\tCate2 :'+node['tt'])
#            for item in node('item'):
#                print('\t\t'+item.string)

##############################################################
#data = {1:'a',2:'b'}
#data2 = json.dumps(data,ensure_ascii=False)
#data3 = json.loads(data2)

#print(type(data2))
#print(type(data3))
#print(data2)

s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""

#jjjj = json.loads(s)
#print(s)
#print(jjjj['name'])
#print(jjjj['detail']['last'])
#print(jjjj['detail'])

class JsonObject:
    def __init__(self,d):
        self.__dict__ = d
    

data = json.loads(s,object_hook = JsonObject)
print(data.name)



