# -*- coding:utf-8 -*-

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Lowlp86' }
    posts= [
        {    'author'   : { 'nickname':'Lowlp87' },
               'body'   : 'Beautiful day in Portland!'
	},
	{
	     'author'   : { 'nickname':'Lowlp88' },
	       'body'   : 'The Avengers movie was so Cool!'
	}
    ]
    return render_template("index.html",
			   title= 'Home',
			   user = user,
			   posts= posts)
