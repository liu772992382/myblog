#!/usr/bin/env python
#coding=utf-8
from flask import *
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from model import *
from flask import Flask, request, render_template,redirect,make_response,flash,session,g,url_for
from time import *




@app.route('/',methods=['GET'])
@app.route('/<int:page>',methods=['GET'])
def hello_world(page = 1):
	atiLength=len(Article.query.all())
	paginate = Article.query.all()
	atiLength=len(Article.query.all())
	return render_template('welcome.html', title="Welcome",articles=paginate,Length=atiLength)

@app.route('/article',methods=['GET'])
@app.route('/article/<int:id0>',methods=['GET'])
def article(id0=1):
	article0=Article.query.filter(Article.Id==id0).all()[0]
	atiLength=len(Article.query.all())
	return render_template('article.html',article=article0,Length=atiLength)

@app.route('/edit',methods=['GET','POST'])
def edit():
	print session['admin']
	if 'admin' not in session or session['admin']=='' or session['admin']!='imgru':
		return redirect('/login')
	if request.method=='GET':
		return render_template('edit.html',title="edit")
	elif request.method=='POST':
		form = request.form
		t=localtime()
		g.article=Article()
		g.article.Title=form['Title']
		g.article.Content=form['Content']
		g.article.Tag=form['Tag']
		g.article.Digest=form['Digest']
		g.article.SubTime=str(t[0])+'-'+str(t[1])+'-'+str(t[2])
		db.session.add(g.article)
		db.session.commit()
		db.session.close()
		return redirect('/')

@app.route('/login',methods=['GET','POST'])
def login(Warnings=''):
	if request.method=='GET':
		return render_template('login.html')
	elif request.method=='POST':
		form=request.form
		p=db.session.query(User).filter(User.Username==form['Username']).first()
		if p!=None and p.Passwd==form['Passwd']:
			session['admin']=p.Username
			return redirect('/edit')
		else:
			return render_template('login.html',Warnings=u'账号或密码错误')

@app.route('/about',methods=['GET'])
def about():
	atiLength=len(Article.query.all())
	return render_template('about.html',Length=atiLength)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')
