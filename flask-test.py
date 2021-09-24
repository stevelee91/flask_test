from flask import Flask, render_template, request, redirect, url_for

import time
import random

app = Flask(__name__)


@app.route('/')
def sessions():
    return render_template("flask-test.html")

@app.route('/senddata', methods=['GET','POST']) 
def senddata(): 
    name = 'world' 

    if request.method == "POST":
        name = request.form.get("name")
        page = request.form.get("page")
        if page == "1":
            return redirect(url_for('page_1'))
    return render_template('senddata.html', name=name)

@app.route('/page_1', methods=['GET','POST'])
def page_1():
    return render_template('page1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')