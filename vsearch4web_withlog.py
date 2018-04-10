#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:32:58 2018

@author: nikigokak
"""

from flask import Flask,render_template, request , escape
from vsearch import search4letters

def log_request(req:'flask_request' , res: str)-> None:
    with open('vsearch.log', 'a') as log:
        # print(str(dir(req)) , res, file = log)
        print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')



app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return'Hello world from Flask!'

@app.route('/search4' , methods= ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request, results)

    return render_template('results.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = results,)

@app.route('/viewlog')
def view_the_log() -> 'str':
    contents = []
    with open('vsearch.log')as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title= 'View Log' ,
                           the_row_titles= titles,
                           the_data= contents,)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search for letters on the web')
app.run(debug = True)
    