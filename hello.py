#coding=utf-8
#!/usr/bin/env python
from flask import *
from werkzeug.utils import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy
from model import *
from flask import Flask, request, render_template,redirect,make_response,flash,session,g,url_for
from time import *


@app.route('/',methods=['GET'])
@app.route('/<int:page>',methods=['GET'])
def hello_world(page = 1):
	paginate = Article.query.order_by(Article.Id.desc()).paginate(page, 5, False)
	return render_template('welcome.html', title="Welcome",articles=paginate)

@app.route('/edit',methods=['GET','POST'])
def edit():
	if request.method=='GET':
		return render_template('edit.html',title="edit")
	elif request.method=='POST':
		form = request.form
		print form
		t=localtime()
		print t
		g.article=Article()
		g.article.Title=form['Title']
		g.article.Content=form['Content']
		g.article.Tag=form['Tag']
		g.article.SubTime=str(t[0])+'-'+str(t[1])+'-'+str(t[2])
		print 1
		db.session.add(g.article)
		print 2
		db.session.commit()
		print 3
		db.session.close()
		return 'yes'
if __name__ == '__main__':
    app.run(debug=True)
