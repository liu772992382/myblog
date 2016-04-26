#!/usr/bin/env python
#coding=utf8
from flask import Flask, request, render_template,redirect,make_response,flash,session
import flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'Article'
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(50))
    Tag = db.Column(db.String(50))
    Content = db.Column(db.String(10000))
    SubTime = db.Column(db.String(50))
