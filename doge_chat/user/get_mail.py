from flask import render_template,send_file,Flask,request,abort
import os
app=Flask(__name__)
@app.route("/get_mail",methods=['POST','GET'])
def get_mail():
    if request.method == 'POST':
        send_mail =  request.values.get("send_mail")
        print(send_mail)
        return "ok"
app.run(host="0.0.0.0", port=5001, debug=True)
