import requests
import random
import hashlib
import threading
import time
#__INIT__
HASH=""
USER=""
ok=0
def p():
    global HASH,USER
    while True:
    
        if ok==1:
            url=f"http://192.168.1.62:5000/get_ip"
            data={"yz":HASH}
            r = requests.post(url,data=data)
        time.sleep(30) 
#__funciton__
def register(name,password):
    url = 'http://192.168.1.62:5000/register'
    data={"name":name,"password":password}
    r = requests.post(url,data=data)
    print(r.text)
def login(name,password):
    global HASH,USER,ok
    url = 'http://192.168.1.62:5000/login'
    num=random.randint(1, 114514)
    md5hash = hashlib.md5(str(num).encode('utf-8'))
    md5 = md5hash.hexdigest()
    HASH=md5
    data={"name":name,"password":password,"yz":md5}
    r=requests.post(url,data=data)
    print(r.text)
    if len(r.text)!=4:
        USER=r.text[6:len(r.text)]
        ok=1
        send(f"{USER}加入了聊天室")
def send(mail):
    global HASH,USER
    url = 'http://192.168.1.62:5000/send'
    data={"mail":mail,"yz":HASH}
    r = requests.post(url,data=data)
    print(r.text)


t1919= threading.Thread(target=p)
t1919.start()
#__view__
while True:
    if USER=="":
        shell=input("/doge_chat_shell/")
    else:
        shell=input(f"/doge_chat_shell/{USER}/")
    if shell=="register":
        name_r=input("name:")
        password_r=input("password:")
        register(name_r,password_r)
    elif shell=="login":
        name_l=input("name:")
        password_l=input("password:")
        login(name_l,password_l)
    elif shell=="send":
        mail=input("send_mail")
        send(mail)
    else:
        print("can_not_run")
        
