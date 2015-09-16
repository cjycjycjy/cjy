import pickle
fileName = "test.txt"
fileName2 = "monica.txt"

with open(fileName,"r") as myFile, open(fileName2,"wb") as monica :
    #myFile.write("201011301 최종윤\n")
    #myFile.write("201011302 최종윤\n")
    #myFile.write("201011303 최종윤\n")
    #myFile.write("201011304 최종윤\n")
    #myFile.write("201011305 최종윤\n")
    #while True:
    #    content = myFile.readline()
    #    if not content: break
    #    print(content)
    data = []
    index = 0
    for content in myFile:
        (role,etc) = content.strip().split(":",1)  #strip() 공백 제거 (인자 하나 추가해서 횟수 제한)
        #if role == "Monica":
            #monica.write(etc)
            #monica.write("\n")
        data.append(role)
                
    
    pickle.dump(data,monica)

with open(fileName2,"rb") as monica :
     result = pickle.load(monica)
     print(result)
    