#encoding:cp949
import re
def passwdCheck(passwd):
    if len(passwd) > 13 or len(passwd)<8:
        print("8�ڸ� �̻� 13�ڸ� ���Ϸ� �ۼ��ؾ���")
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
            print("���ĺ�,����,Ư�����ڰ� ���ԵǾ�� �մϴ�.")
        else:
            print("correct")

        
      

print("��й�ȣ �Է� :")
passwd = input()
passwdCheck(passwd)
