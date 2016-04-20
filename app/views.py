# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __init__ import app
from flask import render_template

@app.route('/')
def index():
    return "Hello World!"

