#coding=utf-8
#!/usr/bin/env python
from flask import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
	return render_template('welcome.html', title="Welcome")

@app.route('/edit',methods=['GET','POST'])
def edit():
	if request.method=='GET':
		return render_template('edit.html',title="edit")
	else:
		print request.form
		return 'yes'
if __name__ == '__main__':
    app.run(debug=True)
