from flask import render_template,send_file,Flask,request,abort
import pymongo
import os 
import requests
import threading
import time

import subprocess as sp
import shutil
from init import *
app=Flask(__name__)
FILE_PATH="file"
user={}
ip=[]
tree=""
def d():
    global user,FILE_PATH,ip
    while True:
        time.sleep(3600)
        if time.strftime('%H')=="24":
            user.clear()

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        global user,FILE_PATH,ip
        name= request.values.get("name")
        password = request.values.get("password")
        yz=request.values.get("yz")
        usertInfo = coll.find_one({'name': name, 'password': password})
        if usertInfo["name"] == name and usertInfo["password"] == password:
            user[yz]=name
            return f"您已登录成功{name}"
        else:
            return "登录失败"
@app.route("/register",methods=['POST','GET'])
def register():
    if request.method == 'POST':
        global user,FILE_PATH,ip
        name= request.values.get("name")
        password = request.values.get("password")
        if name not in alluser() and password not in allpassword():
            coll.insert_one({"name":name,"password":password})
            return "注册成功"
        else:
            return "注册失败"
@app.route("/get_ip",methods=['POST','GET'])
def get_ip():
    if request.method == 'POST':
        global user,FILE_PATH,ip
        yz= request.values.get("yz")
        ip_ = request.remote_addr
        print(ip_)
        if yz in user.keys():
           
            print(ip_ not in ip)
            if ip_ not in ip:
                ip.append(ip_)
            print(ip)
        return "111111111111111111111111111111111111111111111111111111111111111111111"
@app.route("/send",methods=['POST','GET'])
def send():
    if request.method == 'POST':
        global user,FILE_PATH,ip
        yz= request.values.get("yz")
        mail=request.values.get("mail")
        if yz in user.keys():
            name=user[yz]
            send_mail=f"{name}:{mail}"
            for i in ip :
                try:
                    print(i)
                    url=f"http://{i}:5001/get_mail"
                    data={"send_mail":send_mail}
                    r = requests.post(url,data=data)
                    print(r.text)
                except:
                    ip.pop(i)
            return "发送成功"
        else:
            return "发送失败"
t1 = threading.Thread(target=d)
t1.start()

if __name__=="__main__":
    # t1 = threading.Thread(target=d)
    # t1.start()
    # t2= threading.Thread(target=c)
    # t2.start()
    app.run(host="0.0.0.0", port=5000, debug=True)