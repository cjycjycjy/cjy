#encoding:cp949
import sys
import os
import pickle
import shutil
import time
import csv
class MidTest:
    s_num = 0
    name = ""
    data = {}
    fname = ""
    def __init__(self,s_num,name):
        self.s_num = s_num
        self.name = name


    def question1(self):
        print("�й� : "+str(self.s_num)+",  �̸� : "+self.name)
     
    def question2(self,data,n):
        self.data = data
        print(self.data)
        itemlist = []
        itemlist.append(data)
        temp = [itemlist[0].get("��"),itemlist[0].get("���׶�"),itemlist[0].get("�ϻ�"),itemlist[0].get("����"),]
        temp.sort()
        temp.reverse()
        print(temp)  
        
        

    def question3(self,fname): 
        s_list = []
        with open("./score/1��.txt", 'r') as myFile : 
            dataFromFile = csv.reader(myFile) 
            for currentRow in dataFromFile : 
                
                s_list.append(currentRow)
        with open("./score/2��.txt", 'r') as myFile : 
            dataFromFile = csv.reader(myFile) 
            for currentRow in dataFromFile :
                print(currentRow)              
                s_list.append(currentRow)
       
        #with open("./score/"+fname, 'w') as myfile : 
        #    w = csv.writer(myfile) 
        #    for i in s_list:
        #        w.writerows(i)
        f = open("./score/"+fname,'w')
        for i in s_list: 
              f.writelines(i)

              
      
            


    def question4(self,fname):
        try:
            s_list = []
            with open("./score/1��.txt", 'r') as myFile : 
                dataFromFile = csv.reader(myFile) 
                for currentRow in dataFromFile :                
                    s_list.append(currentRow)

            with open("./score/2��.txt", 'r') as myFile : 
                dataFromFile = csv.reader(myFile) 
                for currentRow in dataFromFile :              
                    s_list.append(currentRow)
            s_list.sort()

            with open("./score/"+fname, 'r') as myFile : 



        except FileNotFoundError e:
            print(e)



    def question5():
        print("Current Time : "+time.strftime("%Y.%m.%d. %I:%M:%S", time.localtime()))

greenjoa = MidTest("201011301","������")
greenjoa.question1()
data = {"��":4.5,"���׶�":4.0,"�ϻ�":4.6,"����":4.3}
greenjoa.question2(data,2)
greenjoa.question3("question3.txt")
greenjoa.question4("question4.txt")
MidTest.question5()

