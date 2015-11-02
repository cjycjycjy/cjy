#encoding:cp949
import re
def passwdCheck(passwd):
    if len(passwd) > 13 or len(passwd)<8:
        print("8자리 이상 13자리 이하로 작성해야함")
        return
    else:
        num = 0
        r = re.compile("[A-Za-z]")
        result = r.search(passwd)
        r2 = re.compile("[0-9]")
        result2 = r2.search(passwd)
        r3 = re.compile("[~!@#$%^&*]")
        result3 = r3.search(passwd)
        try:
            result.group()
        except:
            num = num+1
        
        try:
            result2.group()
        except:
            num = num+1
        
        try:
            result3.group()
        except:
            num = num+1

        print(num)
        if num != 0:
            print("알파벳,숫자,특수문자가 포함되어야 합니다.")
        else:
            print("correct")

        
      

print("비밀번호 입력 :")
passwd = input()
passwdCheck(passwd)
