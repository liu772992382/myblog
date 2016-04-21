#coding=utf-8
#!/usr/bin/env python
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('welcome.html', title="Welcome")

if __name__ == '__main__':
    app.run()
