#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:32:58 2018

@author: nikigokak
"""

from flask import Flask,render_template, request
from vsearch import search4letters

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
    return render_template('results.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search for letters on the web')
app.run(debug = True)
    